import sys
import numpy as np
import matplotlib.pyplot as plt
y=[1.000000, 0.000000, 2.000000, 0.000000, 0.000000, 1.000000, 1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 2.000000, 0.000000, 1.000000, 0.000000, 1.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 1.000000, 2.000000, 0.000000, 2.000000, 2.000000, 2.000000, 2.000000, 4.000000, 1.000000, 0.000000, 2.000000, 0.000000, 0.000000, 1.000000, 1.000000, 1.000000, 1.000000, 2.000000, 5.000000, 1.000000, 3.000000, 4.000000, 4.000000, 1.000000, 1.000000, 3.000000, 1.000000, 3.000000, 3.000000, 2.000000, 0.000000, 7.000000, 6.000000, 0.000000, 6.000000, 1.000000, 3.000000, 5.000000, 2.000000, 4.000000, 7.000000, 3.000000, 4.000000, 1.000000, 8.000000, 6.000000, 3.000000, 2.000000, 6.000000, 6.000000, 3.000000, 8.000000, 1.000000, 11.000000, 7.000000, 6.000000, 7.000000, 4.000000, 8.000000, 5.000000, 11.000000, 3.000000, 15.000000, 9.000000, 6.000000, 13.000000, 10.000000, 10.000000, 12.000000, 16.000000, 9.000000, 12.000000, 14.000000, 13.000000, 13.000000, 15.000000, 10.000000, 19.000000, 16.000000, 24.000000, 29.000000, 24.000000, 26.000000, 32.000000, 31.000000, 41.000000, 36.000000, 43.000000, 43.000000, 46.000000, 45.000000, 40.000000, 54.000000, 44.000000, 58.000000, 71.000000, 61.000000, 68.000000, 68.000000, 68.000000, 79.000000, 71.000000, 92.000000, 85.000000, 104.000000, 86.000000, 86.000000, 80.000000, 89.000000, 117.000000, 106.000000, 111.000000, 126.000000, 107.000000, 120.000000, 131.000000, 154.000000, 144.000000, 132.000000, 144.000000, 147.000000, 161.000000, 170.000000, 181.000000, 169.000000, 187.000000, 201.000000, 210.000000, 204.000000, 205.000000, 203.000000, 237.000000, 258.000000, 267.000000, 272.000000, 261.000000, 289.000000, 311.000000, 331.000000, 352.000000, 357.000000, 388.000000, 423.000000, 414.000000, 390.000000, 425.000000, 488.000000, 446.000000, 449.000000, 473.000000, 544.000000, 490.000000, 544.000000, 556.000000, 563.000000, 599.000000, 639.000000, 593.000000, 619.000000, 669.000000, 682.000000, 679.000000, 710.000000, 709.000000, 782.000000, 755.000000, 792.000000, 785.000000, 796.000000, 860.000000, 813.000000, 861.000000, 887.000000, 956.000000, 926.000000, 942.000000, 993.000000, 983.000000, 1101.000000, 1048.000000, 1072.000000, 1128.000000, 1151.000000, 1176.000000, 1205.000000, 1250.000000, 1251.000000, 1295.000000, 1281.000000, 1375.000000, 1418.000000, 1423.000000, 1443.000000, 1504.000000, 1487.000000, 1491.000000, 1630.000000, 1713.000000, 1682.000000, 1720.000000, 1768.000000, 1765.000000, 1938.000000, 1964.000000, 2067.000000, 2137.000000, 2192.000000, 2308.000000, 2386.000000, 2518.000000, 2522.000000, 2580.000000, 2712.000000, 2881.000000, 2968.000000, 2860.000000, 2885.000000, 2843.000000, 2949.000000, 3052.000000, 3095.000000, 3146.000000, 3221.000000, 3287.000000, 3314.000000, 3388.000000, 3548.000000, 3610.000000, 3714.000000, 3731.000000, 3830.000000, 3943.000000, 4086.000000, 4126.000000, 4257.000000, 4262.000000, 4448.000000, 4567.000000, 4560.000000, 4810.000000, 4821.000000, 4968.000000, 5072.000000, 5196.000000, 5354.000000, 5367.000000, 5542.000000, 5879.000000, 5864.000000, 5999.000000, 6178.000000, 6449.000000, 6563.000000, 6851.000000, 7008.000000, 7182.000000, 7432.000000, 7619.000000, 7913.000000, 8124.000000, 8359.000000, 8829.000000, 9242.000000, 9500.000000, 9593.000000, 10226.000000, 10471.000000, 10659.000000, 10888.000000, 11322.000000, 11392.000000, 11915.000000, 11942.000000, 12362.000000, 12430.000000, 12812.000000, 12976.000000, 13203.000000, 13635.000000, 14100.000000, 14050.000000, 14759.000000, 14872.000000, 15179.000000, 15473.000000, 15887.000000, 16218.000000, 16557.000000, 16990.000000, 17536.000000, 18120.000000, 18511.000000, 18698.000000, 19364.000000, 19807.000000, 20403.000000, 20802.000000, 21303.000000, 22185.000000, 22610.000000, 23084.000000, 24020.000000, 24261.000000, 25037.000000, 25573.000000, 25864.000000, 27002.000000, 27845.000000, 28344.000000, 29616.000000, 29935.000000, 30981.000000, 31355.000000, 32402.000000, 33123.000000, 33743.000000, 34735.000000, 35705.000000, 36493.000000, 37017.000000, 38160.000000, 38977.000000, 39796.000000, 41416.000000, 42530.000000, 43772.000000, 45031.000000, 46319.000000, 47448.000000, 49491.000000, 50268.000000, 52023.000000, 53363.000000, 54135.000000, 55957.000000, 57198.000000, 58302.000000, 59891.000000, 61184.000000, 63367.000000, 65263.000000, 67127.000000, 69220.000000, 69848.000000, 72794.000000, 73999.000000, 76069.000000, 78782.000000, 81357.000000, 83608.000000, 86417.000000, 87888.000000, 90797.000000, 93333.000000, 96408.000000, 100180.000000, 104777.000000, 107377.000000, 110909.000000, 113267.000000, 116384.000000, 119851.000000, 123111.000000, 125421.000000, 128913.000000, 133619.000000, 138819.000000, 144032.000000, 148525.000000, 155317.000000, 160133.000000, 164635.000000, 169803.000000, 174475.000000, 181181.000000, 188685.000000, 196512.000000, 203664.000000, 211553.000000, 218575.000000, 228587.000000, 237252.000000, 244964.000000, 251867.000000, 258862.000000, 266931.000000, 274843.000000, 281795.000000, 290954.000000, 302067.000000, 309193.000000, 318728.000000, 326213.000000, 335637.000000, 344398.000000, 356149.000000, 369161.000000, 381633.000000, 395078.000000, 407921.000000, 419224.000000, 428365.000000, 438805.000000, 450744.000000, 457259.000000, 467636.000000, 475423.000000, 481418.000000, 490607.000000, 502621.000000, 510042.000000, 517976.000000, 520941.000000, 525833.000000, 530080.000000, 533170.000000, 541687.000000, 544509.000000, 549425.000000, 555749.000000, 562185.000000, 565850.000000, 572371.000000, 576460.000000, 583125.000000, 588314.000000, 592155.000000, 595330.000000, 602077.000000, 605103.000000, 611114.000000, 615168.000000, 619481.000000, 620106.000000, 622280.000000, 625892.000000, 634282.000000, 638399.000000, 644429.000000, 649365.000000, 657954.000000, 662004.000000, 665195.000000, 672869.000000, 679996.000000, 688291.000000, 691412.000000, 693109.000000, 697576.000000, 700010.000000, 710320.000000, 715259.000000, 717811.000000, 716820.000000, 712315.000000, 707454.000000, 707251.000000, 706489.000000, 707015.000000, 707553.000000, 707604.000000, 709418.000000, 707629.000000, 713327.000000, 718653.000000, 726146.000000, 731741.000000, 731865.000000, 731595.000000, 731277.000000, 733747.000000, 732731.000000, 732869.000000, 733847.000000, 732719.000000, 735284.000000, 733433.000000, 732630.000000, 732428.000000, 737607.000000, 737891.000000, 736567.000000, 733611.000000, 733728.000000, 730539.000000, 725931.000000, 723757.000000, 721333.000000, 713039.000000, 705941.000000, 698207.000000, 687629.000000, 684737.000000, 678874.000000, 673510.000000, 670137.000000, 665640.000000, 661901.000000, 656541.000000, 651616.000000, 643188.000000, 639199.000000, 636111.000000, 630296.000000, 622811.000000, 613713.000000, 607240.000000, 601718.000000, 595183.000000, 591817.000000, 588573.000000, 584802.000000, 580482.000000, 575290.000000, 570653.000000, 569408.000000, 569126.000000, 567957.000000, 565678.000000, 565213.000000, 564420.000000, 562392.000000, 561073.000000, 560257.000000, 560922.000000, 557727.000000, 557751.000000, 556189.000000, 553714.000000, 555100.000000, 554564.000000, 552675.000000, 551129.000000, 544710.000000, 541850.000000, 539518.000000, 540018.000000, 538343.000000, 532781.000000, 531331.000000, 529963.000000, 535773.000000, 541723.000000, 546981.000000, 546802.000000, 543133.000000, 539144.000000, 536030.000000, 525233.000000, 522207.000000, 517851.000000, 509730.000000, 496376.000000, 484046.000000, 476332.000000, 465768.000000, 460699.000000, 452840.000000, 446669.000000, 442288.000000, 435787.000000, 427457.000000, 423824.000000, 417638.000000, 411450.000000, 407884.000000, 400825.000000, 396173.000000, 389143.000000, 387409.000000, 384223.000000, 377032.000000, 373157.000000, 367844.000000, 364278.000000, 360422.000000, 356169.000000, 351585.000000, 344980.000000, 340589.000000, 335837.000000, 333910.000000, 327846.000000, 323794.000000, 320340.000000, 318077.000000, 316397.000000, 312110.000000, 305611.000000, 301632.000000, 296046.000000, 290860.000000, 287142.000000, 279759.000000, 276117.000000, 268327.000000, 262813.000000, 256665.000000, 250054.000000, 241747.000000, 234456.000000, 227009.000000, 218873.000000, 213113.000000, 207741.000000, 203472.000000, 198754.000000, 194287.000000, 189736.000000, 182890.000000, 177779.000000, 173364.000000, 168265.000000, 163188.000000, 160554.000000, 155181.000000, 150475.000000, 145919.000000, 142319.000000, 139393.000000, 135193.000000, 132435.000000, 129106.000000, 126632.000000, 125018.000000, 122817.000000, 120778.000000, 120051.000000, 118119.000000, 117197.000000, 113860.000000, 112040.000000, 109966.000000, 108086.000000, 104105.000000, 101210.000000, 98205.000000, 95895.000000, 93216.000000, 90956.000000, 88543.000000, 85941.000000, 83847.000000, 81540.000000, 79842.000000, 78261.000000, 76120.000000, 74196.000000, 72345.000000, 70172.000000, 67636.000000, 66104.000000, 65369.000000, 64052.000000, 63222.000000, 61460.000000, 60413.000000, 58575.000000, 57456.000000, 56562.000000, 54897.000000, 53766.000000, 52386.000000, 51006.000000, 49860.000000, 48358.000000, 47917.000000, 47024.000000, 46583.000000, 45207.000000, 43185.000000, 42570.000000, 41324.000000, 40623.000000, 39797.000000, 39282.000000, 38509.000000, 37939.000000, 36930.000000, 36005.000000, 35265.000000, 34443.000000, 34147.000000, 33217.000000, 32746.000000, 31392.000000, 30727.000000, 29909.000000, 28538.000000, 28063.000000, 27260.000000, 26723.000000, 25898.000000, 25423.000000, 24475.000000, 23892.000000, 23249.000000, 22653.000000, 21682.000000, 20876.000000, 20106.000000, 19635.000000, 18548.000000, 17877.000000, 17164.000000, 16590.000000, 16242.000000, 15415.000000, 15134.000000, 14644.000000, 14139.000000, 13780.000000, 13449.000000, 13077.000000, 12579.000000, 12516.000000, 11969.000000, 11801.000000, 11490.000000, 11285.000000, 10853.000000, 10529.000000, 9989.000000, 9926.000000, 9530.000000, 9269.000000, 9081.000000, 8596.000000, 8532.000000, 8336.000000, 7971.000000, 7806.000000, 7696.000000, 7302.000000, 7175.000000, 7016.000000, 6814.000000, 6611.000000, 6382.000000, 6284.000000, 6088.000000, 5783.000000, 5801.000000, 5503.000000, 5239.000000, 5057.000000, 4916.000000, 4626.000000, 4388.000000, 4131.000000, 3897.000000, 3733.000000, 3667.000000, 3511.000000, 3374.000000, 3208.000000, 3113.000000, 3089.000000, 2837.000000, 2824.000000, 2700.000000, 2484.000000, 2512.000000, 2438.000000, 2218.000000, 2203.000000, 2111.000000, 2036.000000, 1992.000000, 1938.000000, 1784.000000, 1796.000000, 1695.000000, 1659.000000, 1595.000000, 1517.000000, 1475.000000, 1458.000000, 1385.000000, 1329.000000, 1275.000000, 1271.000000, 1264.000000, 1180.000000, 1124.000000, 1108.000000, 1022.000000, 951.000000, 1016.000000, 948.000000, 926.000000, 865.000000, 854.000000, 878.000000, 814.000000, 793.000000, 699.000000, 738.000000, 722.000000, 692.000000, 651.000000, 686.000000, 610.000000, 572.000000, 565.000000, 559.000000, 565.000000, 535.000000, 486.000000, 525.000000, 454.000000, 471.000000, 430.000000, 462.000000, 396.000000, 408.000000, 390.000000, 396.000000, 370.000000, 367.000000, 338.000000, 334.000000, 300.000000, 311.000000, 277.000000, 299.000000, 274.000000, 254.000000, 255.000000, 239.000000, 265.000000, 238.000000, 222.000000, 201.000000, 228.000000, 184.000000, 195.000000, 177.000000, 172.000000, 185.000000, 168.000000, 168.000000, 134.000000, 140.000000, 152.000000, 136.000000, 137.000000, 100.000000, 125.000000, 127.000000, 107.000000, 112.000000, 106.000000, 99.000000, 92.000000, 101.000000, 89.000000, 82.000000, 75.000000, 65.000000, 88.000000, 65.000000, 66.000000, 55.000000, 65.000000, 69.000000, 61.000000, 82.000000, 65.000000, 55.000000, 57.000000, 47.000000, 46.000000, 36.000000, 54.000000, 41.000000, 28.000000, 33.000000, 45.000000, 37.000000, 36.000000, 28.000000, 49.000000, 27.000000, 41.000000, 33.000000, 23.000000, 27.000000, 26.000000, 25.000000, 24.000000, 23.000000, 19.000000, 22.000000, 15.000000, 8.000000, 18.000000, 15.000000, 14.000000, 17.000000, 12.000000, 11.000000, 12.000000, 9.000000, 13.000000, 7.000000, 11.000000, 7.000000, 6.000000, 5.000000, 5.000000, 6.000000, 8.000000, 10.000000, 3.000000, 7.000000, 8.000000, 3.000000, 8.000000, 2.000000, 7.000000, 1.000000, 6.000000, 7.000000, 4.000000, 1.000000, 4.000000, 2.000000, 5.000000, 6.000000, 4.000000, 4.000000, 2.000000, 3.000000, 4.000000, 3.000000, 5.000000, 2.000000, 4.000000, 2.000000, 3.000000, 4.000000, 3.000000, 1.000000, 1.000000, 3.000000, 1.000000, 3.000000, 3.000000, 0.000000, 0.000000, 2.000000, 0.000000, 0.000000, 2.000000, 2.000000, 1.000000, 0.000000, 2.000000, 2.000000, 1.000000, 2.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 1.000000, 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000, 1.000000, 2.000000, 1.000000, 0.000000, 1.000000, 1.000000, 1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 1.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 1.000000, 0.000000, 1.000000]
minVal=-33949524.000000
maxVal=33476684.000000
plotName=sys.argv[0]
plotName = plotName.replace('.py','.png')
numVals = len(y)
x = np.linspace(minVal, maxVal, numVals+1)[1:]
plt.semilogy(x,y, linewidth=0.5)
plt.title(plotName)
plt.ylabel("Frequency")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(plotName, dpi=300)
