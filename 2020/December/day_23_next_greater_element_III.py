"""
Given a positive integer n, find the smallest integer which has exactly the same digits existing in
the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does
not fit in 32-bit integer, return -1.

Example 1:
    Input: n = 12
    Output: 21
Example 2:
    Input: n = 21
    Output: -1

Constraints:
    1 <= n <= 231 - 1
"""


def nextGreaterElement(n: int) -> int:
    r = list(str(n)[::-1])
    swap_index = 1
    done = False
    while swap_index < len(r) and not done:
        for i in range(swap_index):
            if r[swap_index] < r[i]:
                r[swap_index], r[i] = r[i], r[swap_index]
                if swap_index > 1:
                    affix = sorted(r[:swap_index])
                    r = affix[::-1] + r[swap_index:]
                done = True
                break
        swap_index += 1

    if not done:
        return -1
    r = int(''.join(r)[::-1])
    return r if r < 2147483648 else -1


# Test cases

tests = [
12,
31,
132,
    123,
    321,
2147483647,
2147483111,
502,
635,
258,
439,
284,
28,
792,
546,
667,
840,
367,
343,
223,
771,
666,
294,
831,
339,
556,
479,
766,
412,
615,
692,
557,
462,
370,
501,
297,
394,
419,
901,
883,
846,
772,
7,
82,
271,
752,
834,
57,
974,
901,
679,
283,
92,
171,
275,
263,
991,
160,
471,
879,
286,
660,
457,
157,
32,
825,
124,
760,
731,
699,
375,
850,
507,
243,
206,
354,
233,
378,
592,
122,
623,
63,
460,
566,
359,
937,
918,
521,
807,
500,
575,
110,
917,
869,
37,
936,
911,
368,
650,
818,
13,
460,
528,
894,
7,
293,
117,
1910472707,
861796199,
964715499,
1728843974,
496226000,
248025615,
1772751324,
1898832399,
1178295424,
210032509,
782564990,
912670106,
816607907,
2080035184,
1888560804,
1116881183,
6135737,
1825798364,
174763995,
2114129437,
1783021727,
498435084,
1242236292,
96254271,
640730284,
294618345,
1808846419,
1745908902,
568487384,
221617930,
598202252,
336431195,
1404253606,
1363814456,
780723502,
430112180,
1604968419,
925173909,
1803143195,
1865676690,
1354500294,
1162142101,
135148389,
828463952,
537927568,
2035051663,
218412903,
1114393098,
37950096,
255392757,
256454679,
1234734516,
1307455901,
648830280,
518337946,
1415449679,
277621783,
2026406091,
1017971620,
333413641,
1181235094,
51485248,
957410022,
874100943,
1586632224,
1179611965,
258932467,
75339940,
1790534740,
881274988,
815775971,
689195745,
1273833603,
653970628,
952959738,
482683381,
2047662131,
1132102706,
2069062415,
1918530183,
106795476,
2096120157,
737372374,
922271292,
1453007825,
1181113132,
360783808,
562471752,
2021725769,
1039977353,
888497837,
531966885,
2000749979,
888362,
409912232,
300882855,
241252873,
808173964,
24411510,
1538270138,
8648,
9939,
9387,
5594,
1930,
7694,
3061,
7041,
8096,
1197,
4646,
7254,
6029,
2777,
6394,
9280,
9986,
4963,
8201,
3707,
8960,
3063,
3779,
4398,
3958,
1809,
7660,
2067,
8727,
1571,
2329,
6130,
7253,
8988,
6440,
6570,
8184,
9458,
3903,
8001,
8730,
7378,
8511,
9153,
9317,
6052,
5144,
5535,
5097,
2793,
7621,
2273,
8878,
7327,
8237,
4699,
3610,
3846,
5887,
7236,
8253,
5022,
3058,
6092,
3484,
9370,
9175,
9156,
4565,
3462,
3773,
9469,
8617,
2354,
2629,
3704,
5732,
9840,
4850,
4900,
5552,
1318,
6063,
2160,
4339,
9468,
4895,
5721,
7064,
1968,
5746,
8032,
6826,
6156,
6990,
7701,
3347,
1120,
3938,
5121
]

for t in tests:
    print(t)
    # print(nextGreaterElement(t), end="\n\n")


# import random
#
# for _ in range(100):
#     r = random.randint(1000, 10000)
#     print(f"{r},")
