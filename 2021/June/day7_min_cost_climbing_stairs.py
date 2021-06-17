"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you
can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
    Input: cost = [10,15,20]
    Output: 15
    Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:
    Input: cost = [1,100,1,1,1,100,1,1,100,1]
    Output: 6
    Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
Hint #1
    Say f[i] is the final cost to climb to the top from step i. Then f[i] = cost[i] + min(f[i+1], f[i+2]).
"""
from typing import List


class Solution:
    # Two solutions I wrote, an iterative, and a recursive.
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:2] + ([-1] * (len(cost) - 2))
        if len(cost) > 2:
            for i in range(2, len(cost)):
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[len(cost) - 1], dp[len(cost) - 2])


    def minCostClimbingStairsRecursive(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        n = len(cost)

        def dfs(i):
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(dfs(i-1), dfs(i-2))
            return dp[i]

        return min(dfs(n-1), dfs(n-2))

# Test cases
obj = Solution()
tests = [
[10,15,20],
[1,100,1,1,1,100,1,1,100,1],
    [1,2],
    [2,1],
[719, 947, 761, 898, 953, 163, 813, 90, 260, 568, 509, 806, 273, 302, 750, 901, 997, 527, 64, 766, 755, 427, 817, 350, 412, 535, 435, 69, 309, 95, 298, 487, 84, 558, 78, 702, 123, 529, 640, 976, 338, 991, 126, 434, 18, 739, 824, 297, 135, 489, 503, 646, 146, 418, 861, 967, 299, 589, 934, 652, 66, 28, 376, 718, 413, 447, 637, 955, 552, 74, 5, 433, 654, 41, 90, 767, 217, 66, 234, 79, 732, 77, 417, 231, 869, 69, 572, 453, 650, 446, 773, 778, 281, 922, 15, 954, 79, 62, 282, 526, 275, 795, 988, 894, 637, 464, 491, 766, 66, 84, 391, 438, 596, 932, 589, 156, 839, 267, 885, 415, 209, 689, 566, 476, 654, 803, 467, 30, 350, 49, 443, 49, 545, 402, 487, 666, 518, 277, 563, 9, 458, 116, 771, 606, 358, 420, 358, 60, 289, 367, 557, 171, 642, 936, 908, 353, 646, 872, 714, 681, 798, 357, 819, 571, 257, 253, 877, 710, 925, 44, 891, 252, 412, 925, 816, 952, 137, 869, 215, 154, 716, 315, 515, 535, 462, 43, 474, 109, 864, 23, 669, 714, 843, 247, 22, 621, 800, 143, 642, 681, 359, 843, 57, 279, 354, 634, 520, 323, 236, 874, 809, 519, 227, 419, 617, 881, 792, 581, 545, 275, 114, 574, 361, 475, 128, 634, 710, 61, 636, 797, 702, 717, 565, 67, 954, 739, 616, 843, 674, 389, 192, 640, 25, 460, 169, 146, 659, 881, 377, 586, 175, 691, 639, 877, 541, 47, 120, 976, 599, 68, 639, 247, 446, 171, 325, 964, 206, 607, 837, 877, 713, 523, 678, 818, 92, 967, 625, 104, 558, 431, 970, 362, 428, 806, 976, 33, 730, 279, 310, 425, 878, 512, 355, 635, 313, 227, 209, 687, 965, 380, 912, 813, 308, 487, 492, 913, 550, 19, 125, 829, 178, 155, 502, 209, 214, 403, 735, 663, 836, 508, 381, 661, 238, 708, 411, 650, 31, 873, 984, 366, 180, 951, 774, 11, 156, 523, 904, 657, 265, 62, 22, 982, 515, 850, 398, 112, 385, 870, 742, 640, 796, 513, 974, 155, 161, 199, 398, 996, 360, 558, 910, 609, 355, 729, 403, 932, 337, 639, 744, 796, 596, 292, 223, 980, 525, 142, 911, 886, 614, 594, 716, 727, 749, 817, 692, 58, 820, 184, 751, 152, 812, 878, 574, 310, 588, 998, 183, 570, 373, 825, 634, 443, 719, 888, 745, 144, 49, 343, 249, 84, 1, 149, 370, 51, 463, 743, 81, 994, 243, 684, 403, 854, 857, 958, 901, 305, 901, 503, 952, 597, 751, 832, 23, 80, 823, 610, 301, 851, 208, 712, 233, 706, 963, 698, 345, 226, 411, 180, 627, 699, 633, 1, 496, 825, 412, 988, 4, 387, 165, 597, 243, 509, 641, 148, 466, 181, 237, 282, 46, 649, 197, 844, 258, 888, 750, 548, 509, 352, 4, 246, 590, 729, 858, 505, 975, 230, 119, 675, 317, 533, 595, 465, 847, 456, 498, 954, 805, 310, 470, 206, 65, 470, 509, 754, 42, 263, 813, 577, 252, 272, 48, 794, 569, 113, 603, 633, 113, 71, 846, 218, 698, 928, 565, 884, 483, 478, 859, 729, 7, 852, 293, 925, 901, 295, 173, 519, 441, 570, 185, 431, 540, 659, 850, 234, 471, 888, 950, 68, 598, 673, 632, 656, 147, 632, 604, 654, 481, 851, 51, 29, 2, 420, 245, 269, 841, 950, 249, 75, 753, 820, 634, 860, 324, 475, 895, 557, 848, 72, 304, 836, 913, 586, 456, 514, 17, 402, 743, 299, 473, 167, 225, 966, 783, 913, 744, 126, 969, 595, 244, 873, 672, 221, 704, 592, 398, 787, 915, 453, 526, 980, 753, 955, 273, 99, 800, 308, 71, 121, 387, 587, 472, 101, 6, 166, 740, 817, 323, 481, 243, 955, 756, 425, 146, 555, 107, 746, 680, 69, 254, 415, 806, 86, 458, 903, 216, 890, 535, 4, 917, 833, 564, 372, 606, 5, 244, 911, 360, 809, 50, 206, 802, 285, 750, 285, 784, 705, 302, 819, 513, 597, 35, 721, 948, 327, 252, 354, 168, 558, 187, 672, 834, 788, 275, 558, 352, 58, 363, 120, 427, 530, 811, 632, 969, 143, 211, 176, 115, 677, 671, 857, 834, 183, 296, 774, 922, 561, 91, 765, 109, 109, 830, 466, 19, 927, 436, 866, 58, 591, 831, 231, 683, 619, 726, 232, 89, 739, 611, 519, 954, 272, 377, 210, 604, 403, 243, 613, 610, 813, 953, 316, 92, 807, 585, 590, 876, 716, 546, 759, 59, 200, 506, 484, 647, 739, 214, 808, 727, 421, 599, 344, 792, 351, 868, 557, 632, 744, 454, 324, 672, 414, 596, 988, 238, 345, 796, 411, 810, 961, 926, 799, 64, 660, 549, 875, 773, 936, 669, 771, 314, 432, 332, 142, 699, 734, 981, 123, 827, 925, 173, 673, 83, 564, 735, 760, 498, 102, 383, 484, 134, 82, 615, 801, 211, 695, 757, 125, 774, 591, 414, 847, 525, 360, 538, 878, 113, 761, 786, 447, 256, 554, 754, 282, 664, 403, 34, 667, 496, 47, 33, 545, 193, 15, 659, 570, 934, 706, 4, 867, 638, 4, 398, 632, 644, 788, 584, 312, 938, 168, 168, 242, 956, 528, 87, 797, 742, 653, 663, 85, 78, 700, 502, 448, 956, 857, 993, 862, 929, 926, 632, 441, 841, 651, 419, 875, 739, 424, 358, 92, 649, 455, 141, 898, 968, 180, 358, 297, 156, 101, 829, 168],
[802, 512, 326, 387, 284, 857, 988, 718, 159, 240, 852, 338, 80, 90, 991, 477, 694, 349, 357, 25, 548, 182, 936, 186, 261, 500, 369, 433, 891, 487, 8, 995, 932, 309, 386, 342, 404, 485, 780, 171, 684, 179, 438, 377, 604, 964, 436, 10, 540, 87, 163, 388, 13, 109, 996, 713, 349, 20, 925, 138, 658, 305, 371, 833, 37, 248, 715, 819, 103, 544, 818, 382, 23, 668, 631, 209, 780, 387, 607, 874, 539, 682, 299, 51, 667, 747, 416, 206, 952, 542, 276, 492, 700, 213, 649, 615, 47, 808, 616, 310, 894, 708, 880, 256, 921, 837, 456, 634, 833, 226, 382, 366, 870, 13, 723, 974, 897, 928, 826, 253, 620, 839, 838, 330, 844, 663, 833, 645, 783, 649, 990, 530, 909, 778, 853, 597, 978, 38, 105, 110, 862, 866, 128, 256, 753, 923, 933, 574, 802, 69, 69, 578, 738, 650, 119, 776, 310, 784, 912, 964, 258, 26, 157, 370, 923, 799, 856, 763, 42, 789, 774, 567, 282, 972, 643, 329, 330, 987, 899, 161, 826, 512, 488, 847, 579, 529, 572, 101, 351, 93, 962, 548, 519, 260, 79, 325, 845, 276, 640, 147, 44, 386, 458, 68, 271, 186, 98, 476, 507, 325, 528, 923, 442, 351, 256, 778, 152, 457, 184, 701, 348, 644, 142, 501, 250, 42, 105, 977, 807, 669, 518, 516, 510, 833, 432, 934, 581, 200, 297, 902, 165, 524, 303, 961, 346, 218, 308, 831, 931, 65, 268, 120, 201, 291, 613, 306, 432, 415, 964, 957, 311, 836, 922, 543, 443, 264, 751, 192, 942, 654, 157, 480, 367, 189, 142, 567, 103, 548, 862, 792, 802, 530, 251, 958, 376, 295, 648, 787, 351, 72, 582, 623, 765, 324, 580, 825, 815, 949, 782, 732, 455, 469, 727, 128, 161, 429, 826, 21, 234, 86, 827, 296, 563, 145, 1, 462, 468, 940, 565, 987, 392, 399, 870, 778, 839, 35, 325, 653, 66, 932, 379, 60, 522, 420, 970, 595, 388, 915, 8, 777, 337, 841, 553, 492, 144, 903, 786, 805, 999, 528, 482, 322, 775, 547, 124, 955, 277, 392, 481, 938, 512, 166, 146, 752, 440, 19, 757, 300, 715, 453, 92, 895, 770, 408, 884, 270, 705, 364, 374, 372, 386, 981, 657, 185, 168, 712, 731, 518, 146, 401, 345, 781, 105, 561, 865, 156, 106, 676, 789, 553, 555, 184, 460, 775, 742, 494, 645, 955, 500, 704, 443, 702, 827, 104, 683, 656, 485, 470, 853, 610, 646, 78, 694, 720, 83, 174, 431, 272, 329, 8, 804, 431, 225, 806, 830, 985, 13, 243, 836, 256, 383, 393, 227, 605, 166, 634, 849, 525, 459, 27, 804, 755, 19, 465, 407, 990, 386, 678, 299, 198, 902, 208, 385, 374, 201, 864, 379, 149, 221, 754, 426, 578, 430, 675, 826, 813, 895, 5, 297, 432, 659, 208, 64, 51, 557, 735, 190, 503, 715, 835, 472, 749, 208, 95, 711, 568, 672, 774, 864, 99, 474, 154, 110, 253, 548, 887, 933, 597, 864, 909, 857, 584, 757, 930, 945, 596, 766, 492, 525, 95, 932, 0, 999, 570, 108, 70, 735, 910, 186, 236, 821, 881, 431, 251, 766, 781, 373, 667, 290, 151, 768, 974, 420, 142, 73, 221, 578, 253, 485, 696, 39, 611, 729, 277, 374, 237, 888, 929, 294, 18, 212, 710, 703, 740, 669, 207, 22, 827, 576, 519, 198, 398, 900, 28, 297, 461, 523, 88, 467, 721, 448, 440, 266, 450, 220, 229, 16, 467, 126, 38, 237, 611, 37, 228, 751, 683, 234, 737, 61, 844, 759, 277, 501, 748, 389, 857, 698, 87, 951, 189, 19, 333, 667, 756, 841, 759, 725, 192, 652, 378, 396, 818, 835, 85, 677, 598, 984, 781, 342, 184, 762, 148, 278, 482, 351, 375, 215, 286, 733, 292, 485, 40, 935, 165, 368, 389, 607, 600, 285, 726, 713, 638, 588, 285, 716, 300, 565, 232, 564, 386, 504, 715, 809, 329, 664, 244, 716, 743, 571, 750, 353, 755, 61, 941, 34, 297, 982, 648, 264, 266, 164, 928, 667, 549, 364, 700, 723, 30, 544, 898, 730, 358, 913, 696, 401, 873, 72, 498, 239, 659, 195, 537, 286, 707, 985, 10, 953, 623, 601, 652, 997, 633, 619, 156, 830, 709, 53, 514, 498, 983, 41, 856, 505, 259, 106, 998, 867, 843, 407, 365, 102, 905, 549, 16, 428, 278, 7, 490, 78, 253, 741, 847, 408, 811, 699, 933, 391, 721, 229, 560, 40, 361, 111, 29, 906, 394, 616, 344, 783, 970, 341, 144, 422, 330, 793, 408, 774, 935, 25, 607, 126, 685, 998, 15, 946, 369, 676, 864, 286, 50, 792, 257, 566, 960, 409, 808, 413, 552, 106, 872, 290, 992, 140, 827, 299, 992, 940, 126, 617, 85, 356, 331, 725, 19, 606, 590, 311, 760, 756, 969, 883, 88, 435, 632, 302, 339, 28, 306, 657, 577, 870, 402, 986, 781, 40, 199, 947, 919, 917, 723, 516, 7, 966, 958, 996, 552, 152, 731, 696, 560, 376, 872, 328, 995, 797, 372, 953, 744, 84, 587, 689, 861, 114, 781, 264, 935, 923, 821, 651, 843, 857, 310, 247, 87, 337, 932, 328, 113, 131, 339, 347, 332, 702, 976, 407, 73, 775, 601, 493, 854, 211, 754, 156, 572, 304, 889, 795, 858, 187, 652, 253, 926, 640, 47, 495, 952, 575, 928, 192, 9, 534],
]

for t in tests:
    print(t)
    # print(obj.minCostClimbingStairs(t), end="\n\n")


# from random import randint
#
# def test_gen(length):
#     return [randint(0, 999) for _ in range(length)]
#
# print(test_gen(901))
