/* -------------------------------------------------------------------------- 
 * This software is open source software available under the BSD-3 license.
 *
 * Copyright (c) 2017, Los Alamos National Security, LLC.
 * All rights reserved.
 *
 * Author:
 * - Hoby Rakotoarivelo
 */   
/* -------------------------------------------------------------------------- */
#ifndef _HALO_ENTROPY_ANALYZER_H_
#define _HALO_ENTROPY_ANALYZER_H_
/* -------------------------------------------------------------------------- */
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <mpi.h>

// helper functions
#include "json.hpp"
#include "timer.hpp"
#include "log.hpp"
#include "utils.hpp"
#include "strConvert.hpp"

// data loader
#include "dataLoaderInterface.hpp"
#include "HACCDataLoader.hpp"

// EDIT: process one parameter each time
/* -------------------------------------------------------------------------- */
class HaloEntropy {

  // Workflow
  // - load JSON param file
  // - load HACC data and store attributes
  // - test: show attributes
  // - compute Shannon entropy distribution
  // - generate gnuplot histogram script 
  // (!) make it self-contained

private:
  std::string json_path = "";                                        // JSON parameter file path
  DataLoaderInterface *ioMgr = nullptr;                              // HACC data loader
  
  // per halo attribute data
  std::vector<std::string> attributes;                               // [x,y,x,vx,vy,vx]
  std::unordered_map<std::string, std::string> type;                 // datatype of each attribute [float|double]
  std::unordered_map<std::string, int> size;                         // size of each attribute dataset (in bytes)
  std::unordered_map<std::string, int> nb_elems;                     // number of dataset elements for each attribute
  std::unordered_map<std::string, std::vector<int>> frequencies;     // dataset elems frequency distribution
  std::unordered_map<std::string, double> entropy;                   // computed shannon entropy for each attribute
 
  // MPI
  int my_rank = 0;
  int nb_ranks = 0;

public: 
  HaloEntropy() = delete; 
  HaloEntropy(HaloEntropy const&) = delete; 
  HaloEntropy(HaloEntropy&&) noexcept = delete; 
  HaloEntropy(std::string in_path, int in_rank, int in_nb_ranks);
  ~HaloEntropy();
 
  bool run();  // ok
  bool showAttributeData() const;
  bool computeFrequencies(std::string attrib); 
  bool computeShannonEntropy(std::string attrib);
  bool generateHistogram(std::string path) const;

};

/* -------------------------------------------------------------------------- */
inline HaloEntropy::HaloEntropy(std::string in_path, int in_rank, int in_nb_ranks) 
  : json_path(in_path),
    my_rank(in_rank),
    nb_ranks(in_nb_ranks)
{
  ioMgr = new HACCDataLoader();
  entropy.clear();
}

/* -------------------------------------------------------------------------- */
inline HaloEntropy::~HaloEntropy() {
  if (ioMgr != nullptr)
    delete ioMgr;
}

/* -------------------------------------------------------------------------- */
inline bool HaloEntropy::computeShannonEntropy(std::string attrib) {


  // TODO
}
/* -------------------------------------------------------------------------- */
inline bool HaloEntropy::run() {
  // basic checks 
  assert(nb_ranks > 0); 
  assert(ioMgr != nullptr);

  nlohmann::json json;
  std::ifstream file(json_path);
  std::stringstream debuglog;
  
  std::string filetype;
  std::string log_file;
  std::string input_hacc;
  std::string output_log;
  std::vector<std::string> attributes;

  try {
    // pass file to json parser
    file >> json;
  } catch(nlohmann::json::parse_error& e) {
    if (my_rank == 0) 
      std::cerr << "Invalid JSON file " << json_path << "\n" << e.what() << std::endl;
    return false;
  }

  // retrieve input file
  filetype = json["input"]["filetype"];
  input_hacc = json["input"]["filename"];
  if (filetype != "HACC") {
    if (my_rank == 0) 
      std::cerr << "Only HACC data is supported" << std::endl;
    return false;
  }

  // setup logs
  log_file = json["cbench"]["output"]["log-file"]; 
  output_log = "logs/"+ log_file +"_"+ std::to_string(my_rank);
  writeLog(output_log, debuglog.str());

  for (auto&& scalar : json["input"]["scalars"]) {
    attributes.push_back(scalar);
  }

  // set the IO manager
  if (json["input"].find("datainfo") != json["input"].end()) {
    auto const& datainfo = json["input"]["datainfo"];
    for (auto it = datainfo.begin(); it != datainfo.end(); ++it) {
      ioMgr->loaderParams[it.key()] = strConvert::toStr(it.value());
    }    
  }

  ioMgr->init(input_hacc, MPI_COMM_WORLD); 
  ioMgr->setSave(false); 
  MPI_Barrier(MPI_COMM_WORLD);

  // loop over all scalars and load each of them
  for (auto&& scalar: attributes) {
    debuglog << "\nLoading and running " << scalar << std::endl;
    if (ioMgr->loadData(scalar)) {
      // save infos for debug
      debuglog << ioMgr->getDataInfo();
      debuglog << ioMgr->getLog();

      // TODO: compute Shannon entropy distribution for this attribute

    } else {
      if (my_rank == 0)
        std::cerr << "Error while loading " << scalar << ", exiting now" << std::endl;
      return false;
    }
    appendLog(output_log, debuglog.str());
    // wait for other ranks to complete
    MPI_Barrier(MPI_COMM_WORLD);
  }

  // print some metadata on loaded HACC file


  // everything was fine at this point  
  return true;
}

/* -------------------------------------------------------------------------- */


#endif
