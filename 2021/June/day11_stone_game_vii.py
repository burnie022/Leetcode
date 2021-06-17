"""
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost
 stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the
 one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's
difference. Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the
difference in Alice and Bob's score if they both play optimally.

Example 1:
    Input: stones = [5,3,1,4,2]
    Output: 6
    Explanation:
        - Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
        - Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
        - Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
        - Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
        - Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
    The score difference is 18 - 12 = 6.

Example 2:
    Input: stones = [7,90,5,1,100,10,10,2]
    Output: 122

Constraints:
    n == stones.length
    2 <= n <= 1000
    1 <= stones[i] <= 1000
Hint #1
    The constraints are small enough for an N^2 solution.
Hint #2
    Try using dynamic programming.
"""
from typing import List
from itertools import accumulate


class Solution:
    # Running this code with very long lists results with stack overflow in terminal but accepted on Leetcode.
    # Memoization needed to be done in a 2D list instead of a dictionary to be accepted on Leetcode.
    def stoneGameVII(self, stones: List[int]) -> int:
        memo = [[0 for _ in range(len(stones))] for _ in range(len(stones))]
        sums = list(accumulate(stones[:]))

        def dfs(i=0, j=len(stones) - 1, add=True):
            if i == j:
                return 0
            if memo[i][j]:
                return memo[i][j]

            left = sums[j] - sums[i]
            right = sums[j - 1] - sums[i - 1] if i > 0 else sums[j - 1]
            if not add:
                left, right = -left, -right
            left += dfs(i + 1, j, not add)
            right += dfs(i, j - 1, not add)
            memo[i][j] = max(left, right) if add else min(left, right)

            return memo[i][j]

        return dfs()


        # DFS with memo works but far too slow for long lists. Redundantly recalculates sums at every dfs call
        # def dfsMemo(i=0, j=len(stones)-1, turn=0):
        #     if i == j:
        #         return 0
        #     if (i,j,turn%2) in memo:
        #         return memo[i,j,turn%2]
        #
        #     left, right = sum(stones[i+1:j+1]), sum(stones[i:j])
        #     if turn % 2 == 1:
        #         left, right = -left, -right
        #     left += dfsMemo(i+1, j, turn+1)
        #     right += dfsMemo(i, j-1, turn+1)
        #     memo[i,j,turn%2] = max(left,right) if turn % 2 == 0 else min(left, right)
        #
        #     return memo[i, j, turn%2]
        #
        # return dfsMemo()


        # # Works without memo. Slow.
        # def dfs_no_memo(i=0, j=len(stones)-1, turn=0, score=0):
        #     if i == j:
        #         return score
        #
        #     left, right = sum(stones[i+1:j+1]), sum(stones[i:j])
        #     a = dfs_no_memo(i+1, j, turn+1, score+left if turn % 2 == 0 else score-left)
        #     b = dfs_no_memo(i, j-1, turn+1, score+right if turn % 2 == 0 else score-right)
        #
        #     return max(a,b) if turn % 2 == 0 else min(a, b)


if __name__ == "__main__":
    # Test cases
    obj = Solution()
    tests = [
        [5, 3, 1, 4, 2],
        [7, 90, 5, 1, 100, 10, 10, 2],
        [5, 5, 1, 2, 3, 5, 5],
        [5, 3, 1, 4, 5],
        [454, 989, 739, 904, 646, 100, 639, 449, 891, 46, 32, 483, 99, 311, 270, 224, 151, 188, 667, 513, 880, 758, 720,
         861, 460, 270, 461, 164, 46, 755, 409, 921, 913, 623, 959, 33, 671, 536, 716, 907, 377, 481, 871, 757, 644,
         402, 795, 904, 852, 591, 122, 564, 109, 661, 160, 530, 73, 835, 195, 622, 724, 443, 620, 531, 771, 152, 423,
         450, 944, 391, 757, 673, 886, 924, 161, 413, 899, 167, 356, 250, 548, 581, 403, 708, 685, 723, 363, 362, 980,
         395, 593, 926, 323, 126, 939, 150, 176, 316, 776, 136, 757, 495, 613, 252, 605, 203, 743, 50, 363, 867, 467,
         570, 269, 373, 919, 149, 75, 342, 658, 870, 723, 245, 587, 963, 172, 500, 361, 589, 812, 647, 515, 827, 334,
         740, 416, 436, 1000, 382, 65, 179, 233, 896, 910, 316, 419, 860, 48, 523, 562, 31, 520, 247, 152, 703, 326,
         182, 883, 199, 18, 278, 468, 191, 885, 32, 950, 510, 668, 47, 87, 485, 194, 803, 58, 77, 717, 245, 711, 836,
         633, 442, 874, 767, 27, 433, 815, 611, 580, 135, 834, 686, 551, 471, 27, 146, 99, 488, 484, 586, 25, 372, 931,
         734, 856, 231, 346, 925, 345, 692, 930, 295, 978, 786, 98, 720, 868, 952, 417, 364, 937, 502, 340, 803, 266,
         612, 611, 191, 165, 516, 506, 489, 917, 651, 135, 333, 564, 937, 787, 917, 619, 702, 622, 143, 238, 253, 901,
         401, 594, 861, 439, 439, 823, 986, 928, 329, 187, 339, 772, 551, 128, 845, 112, 418, 862, 127, 929, 905, 528,
         841, 85, 313, 111, 645, 169, 557, 683, 796, 677, 706, 758, 367, 773, 217, 400, 141, 140, 706, 144, 148, 817,
         855, 82, 400, 193, 10, 586, 448, 752, 901, 164, 761, 257, 909, 611, 288, 963, 713, 272, 81, 409, 249, 189, 531,
         359, 339, 173, 374, 854, 20, 180, 501, 359, 732, 197, 529, 422, 485, 135, 243, 672, 448, 7, 109, 141, 180, 222,
         910, 203, 445, 710, 509, 900, 980, 443, 172, 253, 272, 881, 519, 946, 852, 463, 570, 478, 260, 894, 930, 276,
         870, 493, 69, 2, 439, 61, 93, 510, 9, 442, 652, 94, 569, 666, 604, 967, 209, 641, 274, 784, 215, 557, 621, 665,
         962, 812, 304, 874, 115, 62, 785, 917, 116, 646, 57, 551, 389, 569, 749, 102, 561, 556, 4, 583, 832, 480, 104,
         345, 31, 907, 1000, 234, 129, 487, 483, 432, 491, 239, 550, 381, 641, 565, 939, 18, 541, 484, 828, 7, 904, 757,
         283, 808, 46, 764, 784, 115, 674, 170, 402, 952, 413, 616, 454, 623, 212, 864, 459, 729, 680, 134, 600, 834,
         922, 674, 266, 21, 772, 622, 172, 169, 611, 527, 25, 78, 178, 919, 505, 796, 445, 476, 944, 710, 733, 484, 866,
         175, 121, 778, 47, 269, 981, 755, 569, 586, 403, 364, 831, 602, 547, 294, 51, 681, 302, 319, 370, 573, 184,
         691, 953, 236, 248, 364, 636, 846, 763, 503, 29, 623, 744, 141, 410, 79, 309, 227, 127, 268, 861, 165, 644,
         451, 127, 491, 223, 880, 236, 251, 978, 622, 702, 63, 349, 448, 579, 637, 672, 416, 302, 222, 544, 412, 821,
         787, 17, 37, 906, 186, 599, 767, 233, 78, 191, 535, 909, 551, 727, 992, 297, 137, 838, 881, 58, 860, 36, 726,
         953, 245, 330, 261, 261, 118, 427, 632, 599, 431, 162, 409, 718, 102, 693, 131, 716, 988, 245, 266, 778, 752,
         189, 446, 927, 91, 924, 974, 701, 50, 974, 132, 769, 580, 98, 970, 669, 40, 258, 948, 764, 789, 455, 709, 893,
         76, 75, 502, 116, 829, 692, 120, 807, 207, 654, 399, 19, 620, 100, 289, 533, 658, 911, 563, 575, 705, 923, 736,
         822, 712, 322, 73, 63, 96, 54, 690, 456, 866, 243, 72, 178, 718, 172, 826, 822, 862, 305, 401, 308, 315, 930,
         852, 294, 913, 772, 697, 462, 169, 940, 870, 693, 454, 668, 226, 458, 735, 25, 864, 164, 864, 417, 449, 460,
         623, 517, 941, 504, 661, 186, 836, 907, 175, 437, 5, 37, 872, 625, 950, 13, 92, 58, 998, 205, 417, 107, 480,
         116, 787, 369, 751, 202, 725, 228, 933, 702, 895, 757, 100, 851, 411, 691, 526, 899, 537, 858, 480, 289, 773,
         187, 636, 556, 717, 656, 789, 506, 720, 739, 327, 33, 487, 10, 139, 995, 487, 811],
        [235, 977, 910, 5, 144, 508, 477, 375, 731, 744, 995, 877, 22, 847, 874, 221, 658, 819, 834, 161, 850, 829, 745,
         607, 61, 506, 639, 660, 55, 535, 378, 638, 786, 84, 38, 273, 163, 811, 980, 122, 268, 79, 73, 19, 595, 490,
         730, 416, 823, 105, 355, 590, 361, 848, 66, 527, 302, 994, 837, 710, 388, 451, 936, 556, 984, 222, 582, 293,
         512, 98, 407, 531, 462, 466, 350, 358, 580, 303, 140, 130, 974, 456, 314, 848, 829, 422, 929, 518, 840, 674,
         981, 710, 312, 432, 871, 676, 263, 50, 57, 429, 583, 245, 406, 687, 168, 740, 222, 823, 472, 696, 656, 480, 63,
         936, 632, 472, 175, 182, 902, 49, 944, 311, 465, 177, 315, 68, 813, 157, 1000, 761, 262, 42, 558, 264, 418,
         603, 773, 750, 905, 871, 761, 846, 93, 352, 326, 493, 55, 565, 270, 381, 595, 540, 746, 166, 141, 480, 219,
         841, 327, 399, 2, 607, 425, 328, 197, 667, 978, 921, 901, 95, 899, 513, 396, 422, 290, 327, 852, 601, 973, 541,
         632, 686, 224, 154, 331, 669, 604, 14, 307, 967, 869, 695, 7, 290, 976, 43, 413, 133, 570, 938, 252, 395, 921,
         819, 5, 459, 828, 839, 290, 51, 604, 746, 687, 575, 176, 144, 798, 762, 830, 162, 908, 518, 583, 574, 850, 588,
         291, 266, 632, 549, 621, 357, 659, 547, 945, 806, 202, 201, 241, 257, 290, 885, 716, 706, 927, 276, 470, 539,
         469, 861, 746, 25, 125, 668, 244, 22, 339, 99, 982, 170, 821, 633, 36, 826, 618, 489, 380, 570, 103, 321, 382,
         46, 295, 249, 577, 61, 787, 767, 535, 854, 582, 124, 330, 868, 406, 577, 776, 181, 115, 789, 966, 340, 679,
         170, 211, 585, 713, 273, 837, 118, 380, 332, 333, 162, 331, 19, 858, 646, 755, 328, 390, 145, 189, 917, 381,
         722, 437, 383, 864, 795, 756, 634, 592, 691, 370, 875, 255, 913, 581, 622, 204, 831, 813, 923, 542, 507, 710,
         695, 541, 60, 719, 216, 650, 636, 666, 317, 132, 856, 859, 817, 937, 183, 270, 351, 737, 912, 824, 343, 466,
         354, 438, 737, 833, 87, 243, 177, 971, 986, 46, 755, 604, 651, 522, 780, 612, 45, 335, 339, 895, 336, 587, 327,
         49, 407, 672, 115, 587, 219, 936, 904, 317, 826, 154, 223, 405, 613, 536, 314, 473, 775, 229, 499, 311, 950,
         696, 398, 713, 282, 839, 685, 249, 853, 5, 463, 229, 549, 199, 7, 559, 837, 293, 865, 741, 8, 634, 206, 621,
         524, 975, 791, 960, 918, 340, 861, 731, 63, 404, 562, 80, 657, 951, 827, 971, 635, 551, 51, 928, 930, 337, 513,
         905, 423, 452, 55, 737, 370, 519, 565, 223, 472, 41, 859, 659, 825, 932, 492, 466, 694, 119, 963, 1000, 235,
         44, 13, 772, 877, 805, 464, 645, 982, 122, 827, 97, 882, 57, 972, 162, 284, 966, 633, 232, 384, 616, 747, 439,
         997, 337, 999, 310, 9, 294, 354, 975, 670, 532, 211, 660, 851, 1, 637, 338, 613, 360, 224, 402, 727, 960, 685,
         230, 21, 60, 256, 798, 162, 637, 155, 67, 68, 984, 756, 297, 864, 237, 435, 647, 510, 269, 205, 350, 990, 147,
         317, 27, 317, 271, 862, 909, 473, 683, 745, 89, 554, 196, 40, 650, 546, 954, 841, 682, 643, 226, 789, 942, 241,
         821, 395, 712, 782, 670, 317, 776, 455, 727, 135, 562, 348, 8, 994, 961, 417, 3, 661, 667, 820, 699, 633, 219,
         163, 573, 207, 272, 818, 377, 103, 373, 560, 352, 947, 390, 298, 413, 892, 825, 361, 609, 224, 703, 25, 799,
         943, 505, 227, 389, 356, 523, 334, 156, 190, 116, 477, 424, 628, 719, 290, 680, 485, 64, 986, 890, 793, 553,
         225, 357, 846, 356, 543, 572, 600, 201, 579, 39, 872, 639, 272, 808, 949, 427, 269, 507, 162, 389, 757, 26,
         850, 598, 829, 112, 458, 902, 459, 452, 420, 372, 882, 219, 336, 317, 44, 967, 385, 36, 918, 955, 233, 680, 26,
         752, 81, 197, 739, 635, 592, 446, 788, 232, 307, 997, 320, 355, 789, 558, 304, 225, 74, 887, 257, 358, 53, 581,
         646, 744, 526, 327, 275, 609, 792, 152, 997, 511, 505, 451, 970, 703, 470, 856, 358, 664, 278, 767, 520, 587,
         656, 937, 104, 949, 524, 744, 961, 935, 336, 736, 766, 339, 691, 247, 137, 475, 736, 447, 704, 127, 911, 218,
         759, 649, 929, 57, 960, 592, 152, 836, 486, 732, 733, 511, 369, 693, 973, 603, 626, 63, 265, 451, 608, 14, 770,
         424, 962, 1, 485, 208, 506, 600, 770, 393, 798, 918, 98, 970, 562, 83, 459, 650, 199, 557, 843, 986, 580, 896,
         541, 211, 771, 331, 371, 444, 183, 376, 442, 974, 429, 300, 746, 528, 987, 509, 497, 655, 678, 130, 416, 963,
         984, 577, 559, 356, 594, 156, 320, 89, 196, 682, 801, 872, 523, 338, 537, 3, 542, 735, 301, 397, 28, 755, 139,
         102, 170, 61, 719, 170, 382, 352, 507, 313, 976, 632, 696, 868, 715, 153, 340, 317, 973, 886, 907, 623, 673,
         566, 994, 561, 309, 623, 527, 49, 15, 901, 338, 1, 119, 902, 950, 235, 905, 829, 620, 320, 164, 438, 971, 625,
         426, 665, 997, 145, 838, 877, 438, 567, 92, 215, 55, 313, 122, 892, 344, 29, 915, 218, 644, 580, 581, 989, 847,
         155, 741, 146, 513, 847, 150, 194, 968, 66, 238, 796, 901, 121, 39, 195, 903, 635, 847, 251, 528, 649, 483,
         993, 440, 204, 176, 787, 363, 363, 198, 545, 874, 847, 781, 253, 100, 957, 290, 923, 345, 246, 219, 468, 246,
         64, 956, 183, 391, 383, 193, 932, 206, 968, 946, 580, 538, 138, 93, 301, 596, 46, 224, 724, 36, 672, 64, 993,
         944, 442, 792, 266, 633, 120, 723, 338, 968, 823, 657, 864, 898, 861, 348, 277, 843, 840, 122, 766, 36, 81,
         553, 541, 877, 859, 615, 17, 578, 990],
        [2,3],
        [1,2,3],
        [3,2,3],
        [3, 3],
        [353, 577, 175, 42, 977, 675, 139, 760, 819, 926, 289, 287, 33, 766, 459, 312, 192, 631, 585, 395, 301, 839,
         535, 624, 683, 686, 545, 276, 546, 1000, 630, 912, 244, 370, 323, 63, 733, 410, 63, 13, 638, 807, 614, 628,
         140, 205, 401, 150, 104, 763, 302, 855, 445, 281, 823, 849, 86, 665, 503, 833, 409, 536, 762, 405, 767, 188,
         101, 843, 245, 532, 814, 8, 586, 150, 428, 7, 403, 606, 482, 620, 955, 614, 523, 490, 676, 618, 172, 271, 794,
         368, 596, 749, 721, 854, 431, 208, 730, 259, 221, 580, 509, 588, 725, 267, 529, 805, 456, 10, 993, 304, 143,
         748, 995, 625, 407, 246, 565, 6, 918, 169, 622, 155, 249, 407, 288, 924, 538, 232, 252, 6, 487, 341, 737, 473,
         851, 717, 107, 332, 768, 926, 229, 992, 684, 949, 530, 61, 679, 529, 492, 926, 187, 66, 767, 554, 714, 663,
         426, 184, 249, 825, 625, 731, 967, 956, 58, 764, 617, 565, 243, 91, 272, 260, 579, 271, 511, 931, 678, 761,
         878, 312, 482, 294, 263, 557, 287, 90, 506, 96, 878, 10, 153, 841, 836, 646, 434, 93, 840, 646, 305, 782, 379,
         407, 298, 292, 293, 241, 215, 484, 100, 292, 995, 595, 610, 164, 144, 228, 844, 219, 730, 195, 274, 88, 774,
         673, 267, 829, 727, 137, 638, 327, 359, 235, 957, 377, 497, 813, 311, 735, 293, 947, 244, 737, 791, 582, 823,
         845, 283, 595, 354, 737, 614, 104, 401, 800, 812, 988, 285, 892, 484, 213, 864, 534, 285, 677, 381, 222, 35,
         539, 303, 425, 725, 929, 125, 780, 623, 518, 193, 188, 72, 643, 95, 583, 893, 75, 947, 4, 765, 370, 1, 219,
         255, 436, 859, 889, 379, 435, 835, 419, 105, 398, 280, 819, 163, 476, 973, 183, 772, 515, 709, 590, 793, 82,
         270, 785, 300, 1, 381, 303, 87, 588, 984, 867, 995, 843, 432, 489, 100, 542, 20, 547, 314, 988, 234, 458, 595,
         560, 699, 642, 534, 878, 739, 946, 437, 149, 408, 333, 566, 133, 558, 638, 349, 568, 230, 137, 162, 283, 408,
         741, 433, 865, 377, 830, 613, 809, 529, 357, 264, 776, 777, 50, 581, 918, 99, 236, 361, 696, 310, 534, 461,
         455, 801, 269, 2, 209, 896, 922, 275, 661, 704, 301, 108, 273, 122, 136, 823, 425, 668, 641, 928, 234, 415,
         147, 898, 957, 760, 785, 841, 761, 425, 303, 84, 813, 80, 482, 782, 686, 847, 909, 751, 375, 938, 618, 431,
         829, 490, 928, 859, 359, 860, 398, 590, 76, 508, 772, 974, 620, 183, 40, 402, 187, 870, 520, 685, 71, 986, 193,
         267, 402, 197, 592, 880, 181, 716, 581, 972, 655, 395, 562, 920, 426, 401, 644, 567, 17, 727, 12, 450, 54, 705,
         185, 764, 827, 705, 327, 494, 454, 90, 239, 295, 968, 324, 431, 244, 2, 518, 884, 641, 180, 750, 693, 910, 653,
         219, 605, 600, 843, 407, 702, 19, 352, 398, 177, 203, 963, 459, 693, 662, 661, 992, 654, 987, 375, 785, 126,
         451, 152, 169, 574, 433, 852, 425, 53, 48, 456, 458, 631, 134, 764, 206, 586, 521, 654, 351, 115, 548, 785,
         843, 951, 754, 640, 540, 225, 482, 613, 408, 875, 44, 795, 770, 743, 533, 884, 299, 234, 49, 885, 229, 626,
         554, 561, 455, 107, 900, 727, 962, 837, 416, 440, 804, 354, 386, 184, 540, 645, 315, 574, 790, 255, 866, 294,
         571, 639, 873, 641, 55, 796, 681, 283, 366, 969, 543, 730, 108, 667, 635, 798, 784, 228, 107, 106, 969, 395,
         350, 467, 288, 998, 51, 215, 994, 980, 821, 293, 9, 995, 599, 732, 96, 921, 586, 491, 347, 504, 13, 392, 914,
         153, 782, 446, 748, 246, 227, 199, 760, 254, 242, 410, 677, 522, 355, 185, 540, 926, 633, 879, 230, 209, 414,
         944, 782, 955, 223, 401, 531, 811, 979, 369, 884, 717, 866, 592, 66, 387, 213, 574, 385, 162, 564, 818, 113,
         942, 316, 748, 931, 535, 874, 703, 176, 835, 47, 57, 579, 35, 782, 655, 3, 19, 403, 89, 124, 210, 827, 640, 48,
         345, 737, 610, 585, 953, 815, 417, 736, 853, 527, 840, 339, 836, 560, 114, 738, 125, 781, 871, 546, 792, 258,
         160, 245, 422, 356, 422, 320, 398, 409, 426, 189, 926, 832, 241, 895, 622, 821, 214, 597, 19, 493, 296, 445,
         218, 153, 490, 533, 978, 855, 269, 825, 555, 987, 554, 109, 541, 205, 441, 776, 548, 481, 405, 343, 936, 817,
         340, 647, 421, 925, 462, 42, 191, 200, 454, 787, 60, 967, 777, 809, 636, 480, 876, 473, 25, 977, 813, 378, 949,
         440, 297, 506, 557, 179, 307, 769, 224, 479, 950, 290, 644, 349, 114, 236, 820, 399, 247, 164, 418, 704, 250,
         905, 177, 647, 371, 446, 86, 183, 457, 976, 667, 130, 483, 442, 866, 57, 34, 607, 178, 384, 424, 219, 424, 161,
         737, 207, 859, 856, 946, 663, 227, 110, 820, 189, 189, 398, 949, 763, 617, 757, 213, 237, 931, 841, 586, 685,
         634, 156, 277, 227, 691, 626, 385, 116, 720, 385, 397, 944, 658, 633, 404, 505, 116, 915, 354, 889, 623, 259,
         849, 634, 278, 30, 715, 417, 595, 984, 829, 933, 183, 149, 372, 333, 269, 467, 250, 690, 497, 649, 250, 937,
         246, 428, 932, 357, 354, 80, 259, 53, 819, 340, 886, 776, 915, 717, 198, 750, 686, 471, 647, 822, 402, 656,
         720, 969, 566, 968, 454, 871, 25, 233, 216, 673, 414, 87, 640, 10, 807, 693, 312, 81, 234, 710, 587, 280, 216,
         103, 393, 794, 405, 669, 892, 50, 370, 805, 91, 276, 752, 330, 762, 932, 142, 831, 951, 165, 147, 719, 750,
         508, 350, 618, 983, 670, 35, 640, 135, 879, 14, 715, 65, 994, 380, 374, 242, 56, 846, 5, 390, 8, 492, 515, 48,
         917, 903, 125, 45, 456, 826, 209, 857, 380, 157, 233, 956, 632, 202, 162, 469],
        [359, 272, 421, 563, 929, 261, 487, 106, 398, 863, 547, 691, 766, 374, 117, 635, 803, 487, 11, 323, 931, 493,
         218, 831, 183, 706, 968, 196, 292, 332, 633, 741, 515, 69, 632, 949, 728, 38, 613, 817, 3, 706, 888, 14, 667,
         840, 249, 365, 385, 534, 31, 218, 229, 680, 957, 386, 598, 869, 647, 496, 379, 560, 706, 923, 201, 895, 137,
         436, 683, 915, 802, 751, 289, 711, 216, 706, 565, 404, 620, 831, 639, 369, 20, 760, 898, 784, 375, 40, 576,
         123, 958, 274, 488, 125, 986, 855, 274, 61, 582, 500, 376, 54, 792, 353, 110, 418, 533, 661, 257, 335, 869,
         403, 350, 499, 802, 229, 21, 636, 292, 326, 380, 956, 629, 790, 422, 354, 178, 900, 414, 429, 284, 242, 406,
         20, 474, 718, 50, 768, 437, 783, 803, 447, 983, 854, 133, 911, 647, 289, 85, 833, 42, 278, 698, 339, 960, 801,
         730, 252, 802, 505, 445, 375, 122, 458, 42, 499, 859, 453, 537, 387, 641, 591, 117, 799, 658, 863, 79, 994,
         124, 296, 547, 115, 148, 375, 545, 31, 942, 136, 393, 575, 217, 984, 650, 206, 782, 751, 949, 428, 320, 151,
         232, 559, 943, 19, 66, 391, 207, 73, 626, 708, 840, 622, 410, 738, 566, 387, 682, 836, 231, 226, 965, 172, 945,
         666, 658, 563, 942, 975, 914, 830, 597, 20, 64, 552, 723, 64, 354, 987, 438, 972, 674, 699, 498, 266, 56, 215,
         415, 583, 924, 908, 477, 405, 566, 384, 934, 493, 517, 295, 23, 183, 51, 369, 932, 145, 939, 726, 83, 747, 938,
         777, 99, 827, 754, 536, 720, 819, 724, 528, 211, 67, 184, 572, 384, 705, 648, 265, 530, 939, 574, 193, 423,
         387, 339, 17, 724, 22, 857, 354, 60, 53, 245, 529, 124, 744, 826, 833, 75, 580, 799, 957, 268, 177, 824, 906,
         986, 745, 210, 638, 798, 712, 102, 577, 400, 697, 314, 838, 61, 669, 655, 859, 157, 76, 4, 52, 841, 58, 695,
         277, 86, 770, 333, 777, 532, 731, 819, 770, 611, 435, 477, 119, 563, 624, 87, 173, 860, 155, 421, 944, 816,
         635, 104, 480, 262, 31, 273, 893, 370, 60, 525, 902, 158, 14, 690, 590, 14, 543, 732, 400, 971, 566, 202, 369,
         700, 706, 483, 835, 200, 9, 628, 752, 552, 805, 887, 558, 929, 116, 344, 654, 658, 108, 776, 718, 169, 352,
         689, 803, 388, 508, 660, 31, 857, 369, 720, 569, 851, 636, 952, 543, 686, 607, 73, 484, 747, 482, 822, 182,
         385, 631, 236, 625, 981, 584, 844, 378, 441, 840, 405, 417, 612, 321, 275, 189, 211, 10, 123, 681, 300, 845,
         412, 529, 278, 670, 346, 212, 696, 96, 296, 326, 958, 45, 88, 833, 301, 905, 693, 838, 697, 758, 479, 221, 463,
         254, 978, 866, 207, 772, 496, 991, 44, 587, 212, 225, 5, 873, 672, 199, 582, 816, 924, 713, 517, 208, 135, 292,
         779, 547, 606, 158, 269, 953, 260, 254, 608, 681, 117, 429, 23, 618, 530, 185, 630, 238, 660, 166, 189, 594,
         545, 763, 744, 637, 41, 671, 742, 560, 570, 806, 392, 669, 935, 284, 522, 576, 885, 636, 934, 706, 478, 592,
         519, 83, 367, 933, 424, 495, 451, 222, 324, 6, 813, 119, 418, 825, 397, 232, 322, 650, 860, 413, 536, 893, 396,
         742, 210, 471, 518, 124, 987, 699, 544, 494, 255, 793, 428, 905, 531, 342, 663, 762, 579, 239, 214, 290, 1000,
         21, 359, 855, 559, 70, 703, 954, 101, 542, 838, 256, 752, 583, 686, 165, 467, 729, 391, 568, 575, 920, 202,
         407, 341, 136, 104, 45, 175, 597, 875, 579, 731, 384, 335, 748, 325, 798, 363, 626, 153, 434, 155, 438, 107,
         244, 723, 614, 207, 768, 191, 875, 885, 835, 599, 373, 573, 575, 403, 477, 508, 105, 915, 299, 207, 355, 452,
         40, 965, 543, 874, 177, 758, 825, 295, 961, 399, 335, 775, 735, 388, 689, 8, 592, 197, 455, 80, 668, 205, 533,
         234, 56, 688, 637, 433, 935, 479, 568, 377, 495, 415, 250, 820, 641, 717, 156, 430, 723, 914, 816, 611, 823,
         503, 98, 218, 679, 355, 865, 199, 658, 766, 428, 312, 896, 247, 206, 544, 648, 854, 835, 849, 409, 223, 764,
         720, 528, 354, 570, 182, 944, 569, 950, 93, 515, 206, 174, 974, 643, 274, 330, 39, 549, 16, 879, 865, 494, 798,
         494, 801, 220, 402, 515, 773, 487, 512, 929, 346, 165, 935, 545, 150, 424, 659, 533, 480, 265, 78, 935, 586,
         794, 944, 580, 999, 509, 505, 625, 348, 381, 302, 428, 468, 935, 456, 746, 223, 39, 566, 243, 342, 458, 24,
         374, 569, 108, 286, 83, 963, 846, 824, 110, 179, 788, 569, 532, 214, 442, 535, 906, 266, 913, 806, 11, 421,
         241, 306, 781, 823, 748, 992, 200, 338, 787, 597, 439, 230, 114, 808, 980, 398, 255, 75, 437, 17, 659, 435,
         837, 81, 427, 546, 3, 421, 649, 578, 842, 637, 181, 943, 269, 503, 782, 776, 389, 931, 777, 157, 468, 392, 487,
         1, 917, 590, 60, 692, 108, 402, 31, 279, 547, 723, 141, 894, 458, 298, 416, 318, 596, 770, 583, 720, 272, 660,
         304, 940, 170, 743, 658, 848, 603, 335, 323, 559, 72, 980, 91, 782, 958, 981, 15, 46, 955, 856, 796, 719, 919,
         88, 213, 268, 595, 245, 393, 417, 324, 737, 22, 994, 209, 343, 596, 275, 666, 932, 398, 960],
    ]

    for t in tests:
        print(t)
        # print(obj.stoneGameVII(t), end="\n\n")


    # from random import randint
    # def test_gen(length):
    #     return [randint(1, 1000) for _ in range(length)]
    # print(test_gen(1000))
