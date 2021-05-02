"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are
such that A[i] + B[j] + C[k] + D[l] is zero.
To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers
are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:
    Input:
        A = [ 1, 2]
        B = [-2,-1]
        C = [-1, 2]
        D = [ 0, 2]
    Output:
        2
    Explanation:
        The two tuples are:
            1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
            2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""
from typing import List


def fourSumCount(A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    sums_a, sums_b = {}, {}
    total = 0

    for i in range(len(A)):
        for j in range(len(A)):
            a, b = A[i] + B[j], C[i] + D[j]
            sums_a[a] = sums_a.get(a, 0) + 1
            sums_b[b] = sums_b.get(b, 0) + 1

    # print(sums_a, end="\n\n")
    # print(sums_b, end="\n\n")

    for s in sums_a.keys():
        if -s in sums_b:
            # total += max(sums_a[s], sums_b[-s])
            total += sums_a[s] * sums_b[-s]

    return total



# Test cases
import random

tests = [
    ([1,2], [-2,-1], [-1,2], [0,2]),
    ([1,2], [-2,1], [-1,2], [0,2]),
    ([0, -10, 6, 5, -5, 1, -2, -3, 10, 1, -3, 10, 3, -7, -2, 3, 3, -1, -10, 7],
        [-2, -5, 4, -2, 9, -8, 6, -10, -2, -7, -5, 0, 9, -7, 5, -8, 9, -3, 2, -1],
        [-8, 1, -10, -7, 9, 0, 9, 8, 9, 3, 9, 3, 1, -2, -4, -7, 3, 0, 10, -7],
        [10, 8, 1, 1, 0, -8, -9, 2, -9, -6, -6, -3, 0, 1, 0, 2, 8, -7, 6, -4],
     ),
    ([6, 1, 6, 20, 21, -21, -3, 2, -9, 17, 12, -23, -1, -20, 22, 2, -17, 22, 17, -21, -27, -2, 0, 18, 7, -27, 12, 3, 6, 16],
    [10, 14, -27, -3, 27, 26, 13, 28, -3, 24, -7, -12, -16, -29, 7, -29, 1, -12, 18, 2, 5, -1, -19, -18, -6, -7, 25, 13, -18, 26],
    [-30, -16, -12, 17, 28, 2, -21, 7, 27, -15, 22, -6, -17, 4, 20, 25, 23, -9, 16, -5, 11, -19, 14, -23, 25, -11, -14, -3, -7, 3],
    [7, 8, -17, -18, 27, -28, 21, 23, 28, 27, 10, -6, -19, 23, -10, -19, 25, 17, 0, -28, 6, 12, 19, -5, 13, 1, -1, -22, 17, -16]
    ),
    ([1344, -1431, 2882, 839, -697, -1095, 2342, 200, 72, -326, -221, 2731, 2191, 309, 2228, 1272, 71, -1044, -1919, 1158, -824, -8, -1625, 28, 261, 2831, -1372, -107, 927, 2966, -926, 2702, 2563, -17, 382, 2483, -1761, 2642, 2723, 1878, -1700, 2300, -267, -1734, 642, -1355, 1163, -238, -1876, 499, -1158, -868, -1699, 160, 1663, 1179, -1982, 1498, -982, -685, -828, -1693, 355, 600, 1276, 467, 1975, 2180, 1957, 2319, -265, -173, 2144, -1197, 2004, -1948, 883, 16, 2031, 1181, -1939, 416, -1132, 2550, 2636, 863, 222, 631, 432, -1677, -110, -758, 1933, 1386, 2729, -1263, -1640, -575, 846, -1332, -1177, 853, -156, 713, 2438, 682, -746, 81, 178, 222, -941, -1629, 1744, 794, 1986, -1808, 1998, -1357, 1561, 2528, 1157, -1108, -1950, -183, 2271, -943, 1933, 2952, 606, -1102, 1295, 2408, 1532, 2857, 2586, 2036, -88, 535, -1735, 1539, 1050, -306, -1409, 560, 2230, 2672, -878, 2536, -1102, -410, 466, -188, -433, -868, -1935, 1913, 846, 1448, 2595, -878, 1234, 2107, 259, -1877, 309, -1704, 1735, 364, -1153, -1767, 2122, 699, -1517, 580, 24, 2078, 2937, -1002, -873, 2055, -937, -730, 7, 1711, 1991, -1834, 152, -1574, 1281, 1800, -1736, -42, 2174, -839, 1549, -1455, 2864, -565, 2321, -1364, -1376, -522, -1123, 2739, -1302, 906, 1011, -881, 1462, -55, -1741, 2238, 2184, -1566, 2308, 758, 368, 1806, 2651, -271, -1943, -1955, -251, 2380, 1319, -1565, 7, -1790, 1214, -721, 395, -1308, 193, 1800, 823, 2816, -769, 873, 1578, -563, 2331, -1801, 2033, 2622, 1229, 291, 1167, -408, 528, -1152, -954, 1642, -1388, 1628, 2993, -1453, 1903, -1180, 1845, -1919, -1837, -1713, -421, 2288, -1171, 1043, 1724, 1578, 416, 271, 1438, 1493, 2508, -1500, -415, 450, 1520, 1, -1060, 1275, 639, 1412, 632, 2918, -1816, 1195, 2345, 987, 349, -1791, 1384, 2553, 920, 1697, -151, -1988, 2920, 1282, 2646, 2994],
    [-1820, 466, 1374, 2403, 2983, -1414, 278, 1485, 848, 1403, 312, -1672, -446, 46, -209, 950, -788, 1639, -1082, -1238, -828, -558, 1108, -111, -226, 1235, -788, -1385, 1435, 1085, 2398, 1664, 1292, -967, -1266, 1886, -1031, 40, 1932, 1816, -1229, 2686, 310, -415, -1937, 1846, 658, 2010, 2004, 2721, -43, 33, 1319, -516, 674, 1281, 2864, 856, -1453, 2664, -997, -123, 1214, 719, 2381, 2522, 402, 559, -822, 550, 883, 1193, 2462, 1669, 1632, 1452, 2983, 1228, 158, 1415, -1350, -21, -1899, 108, -535, -1504, -654, 1877, -61, 2939, 331, 1877, 444, 609, -194, 1915, 382, 807, 600, 1567, 2751, 1329, -495, 979, -1644, -1754, 2764, 1672, 2830, 911, -1444, -260, -480, 792, 268, 1858, -1690, -1050, 252, -1388, 1071, 1355, 1597, -1739, -29, -750, 662, -1382, 321, 993, -1778, -1793, 1095, 34, -1892, -1562, 2785, 732, 461, 2448, -965, 814, 1072, 73, -46, 329, 1211, 983, -1967, -681, 1932, -530, -1458, -1940, -481, 2440, 1166, 1964, 1143, -76, 2889, -1815, -871, -893, 2094, 2997, 666, -1297, -1105, 2248, -1110, 2431, -913, -578, 2852, 2998, 16, -916, -1308, 2366, 1393, 1641, 445, -563, -1077, 1216, 1576, 1870, 1826, 1312, 1220, 835, 2988, -1634, 2665, 1182, 1084, 1191, 2559, 1730, 1828, 1611, -808, 1483, 2439, -414, -1855, 2063, 1576, -622, 1363, -1631, -999, 1061, 1417, 180, -1016, 2731, -1914, -720, -6, -1016, 169, 2673, -14, 2272, -1609, 1657, 2237, 2039, 340, -1081, 651, 1057, 2363, 1855, 876, -187, -645, 478, 1784, -790, 1219, 278, 1752, 2776, 2344, 2309, -1922, 333, 17, -1515, 123, 2691, 2630, 970, 681, 2608, -1786, 2231, 2102, -757, 2250, -96, 1877, 1389, 1858, 1856, 1533, 459, -1329, 2080, -113, -1780, 1818, 1209, -1449, -1410, 1914, -2000, 865, 172, 1244, -950, 983, 2748, -396, 2624, 1367, -875, 812, 470, -1407, 1729, -412, -269, 1734, 2313, 1173, 2713],
    [1740, -259, -84, -899, -1691, -1490, 2426, 2378, 2431, 739, 1650, 2079, 346, -1811, -977, -1798, 1309, -247, -1692, 301, 1862, -919, 2890, 966, 1491, 2263, 2939, 964, -491, 1611, -170, -94, 2041, 2666, 1621, 1359, 2584, 2567, -837, -873, -1378, 558, 2480, -1940, 1563, 2176, -494, -137, 1165, -1195, 624, 497, 2538, 1428, -1438, -879, 72, 103, 2544, 2809, 2382, -578, 2820, -1536, -1456, -1057, -1252, -196, 521, -1857, -1361, -938, -975, -1971, 300, -1926, 260, 2375, 1818, -1249, -1082, -1145, 2789, 977, 2031, 2049, 1378, 1060, 2944, 2047, 2786, 2788, 1655, 2969, 2385, -1820, 2676, 1144, 912, -464, 1205, 1394, 1054, 1176, 1648, -437, 2324, 333, 1351, -1193, 440, -1074, 1888, 2557, -1462, 2826, -1861, 381, 352, 2071, 9, 1138, -1065, 2831, 1198, -1116, -834, 1150, -227, -1662, -577, -1811, 1796, -259, -736, 1152, -819, -1387, 381, 1850, 258, -1773, 152, -1786, 682, 1562, -356, -1593, -1294, -1447, -1463, -310, 1294, -1143, 1464, 2785, 1741, -391, -1197, 1151, 1161, -1612, 2430, -1740, 355, 624, -1508, -1440, 687, -1184, 1282, 2728, 2087, -1437, -379, 1255, 205, 1261, 2014, 713, 819, -1009, -547, 1243, 1866, 2362, 2985, 1134, 774, -1070, 1687, 2081, -1972, 431, 921, -734, 2553, 1187, -1605, -60, 272, -928, -758, -1979, -961, 1642, -1405, 559, 2875, -692, 1450, 1615, 2172, 555, 2635, 2277, 2067, 2843, -677, 41, -1861, -1674, 322, -163, 1940, 418, 953, -854, -63, 1951, 1189, -686, 2875, 1231, -373, 2639, 2303, -1624, 632, 2039, -239, -1923, 887, 1397, 966, 1176, 756, -411, -1723, 335, 1604, 2910, 1523, 1062, 1301, -1936, 2824, -717, -740, 1690, 2164, 677, -1902, 204, 1038, 1138, 2697, -1938, -1726, 1393, -1242, -1006, 1545, 2710, 1468, 1021, 1866, -1301, -1987, -1828, 1397, -1738, 2096, -171, -282, -478, -1758, 2305, 900, 1577, 1125, -550, 1238, -763, -1223, 2256, -2000, 2455, -1380, 1274],
    [1780, 2412, -1221, 1389, 1227, 2121, -1564, 2944, -1277, -899, 1920, 185, -1979, 542, -1045, 1601, 1473, 1181, -901, 2299, 2912, 953, 424, -852, -608, -1516, 2570, 970, 1463, -78, -866, -1007, 1787, -1273, -1914, 2557, 2234, -1494, -1526, -29, 1451, -1490, -360, 2697, -1912, 94, -917, -252, 1926, 647, 607, -441, 1202, -25, 2691, 643, 2748, 1043, 1274, 936, -206, 936, 2088, 158, 2529, 1964, -1942, -1930, 1379, 41, 1149, 166, 2029, -776, 795, -882, 864, -143, 327, 2386, -1304, 126, -1367, 2769, 284, 1073, 1486, 2212, -321, 2382, -91, -1712, 2270, -317, -303, -1404, -1264, 1466, -125, 2216, -1924, 1250, 659, 327, 410, 1262, 694, -1528, 686, 305, 1489, -1420, -840, -1484, 2924, 1914, -1375, -739, -1973, 1896, -1818, 565, 2489, -270, -1888, 58, 1202, 1143, -466, -1222, -943, 1740, 1000, 1257, 76, -359, 2154, -1973, 1189, 1648, 671, -1598, -1545, -399, 1215, -1931, -1925, -67, 103, 313, -1903, -5, 2774, 1123, -1117, 1766, -96, 277, -1343, 1429, -1168, 1669, 1859, 2439, 1288, -1183, 2272, -1077, -1388, 1877, 1152, 2754, 1197, -433, 30, -1541, -1672, -148, -950, 139, 1126, -1353, -956, -951, -1201, 571, -1663, -850, -49, 1542, 1193, 1279, 104, -1488, 2975, 988, 535, 1036, 244, 487, 1444, 1025, 690, 2533, -1889, 107, -1905, 596, -355, 2151, 2334, -1557, 472, 12, -1889, 1042, 887, -1215, 1328, 2966, -1813, -1907, 2531, 2106, 290, 2573, 1564, 1431, 2153, 640, 1224, -639, 2829, 1449, -1828, 1311, -789, -985, 849, 2418, 2219, 1313, 2309, -1930, -1822, -222, -884, -281, -1489, -1811, 212, -1477, -117, 2835, -1562, -1259, 982, -1602, 1192, -773, 690, 760, 1063, -418, 758, 2898, 2117, -1448, 193, 318, 2195, 717, -1898, -281, 1226, -993, 724, 782, 1119, 1401, -884, 772, 2936, 1963, -904, 1056, -447, -1473, 1666, 1936, -1528, 2419, 1338, 1261, 1253, -1132, -991, -681, 2460, 2526]
     )
]

for t in tests:
    print(*t)
    print(fourSumCount(*t), end="\n\n")


def genTests(len_n=20, lower_range=-10, upper_range=10):
    test = []
    for i in range(4):
        t = []
        for j in range(len_n):
            t.append(random.randint(lower_range, upper_range))
        print(t)
        # test.append(t)
    # return test

# print(genTests(300, -2000, 3000))



