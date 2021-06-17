"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a
double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open
interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common
to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully
without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:
    MyCalendar();
    MyCalendar.book(10, 20); // returns true
    MyCalendar.book(15, 25); // returns false
    MyCalendar.book(20, 30); // returns true
    Explanation:
        The first event can be booked.  The second can't because time 15 is already booked by another event.
        The third event can be booked, as the first event takes every time less than 20, but not including 20.

Note:
    The number of calls to MyCalendar.book per test case will be at most 1000.
    In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

Hint #1
    Store the events as a sorted list of intervals. If none of the events conflict, then the new event can be added.
"""
from collections import deque
import bisect


class MyCalendar:

    def __init__(self):
        self.start_deq = deque([])
        self.end_deq = deque([])

    def book(self, start: int, end: int) -> bool:
        if not self.start_deq:
            self.start_deq.append(start)
            self.end_deq.append(end)
            return True

        after = bisect.bisect_left(self.start_deq, end)
        before = bisect.bisect(self.end_deq, start)

        if before == after:
            self.start_deq.insert(before, start)
            self.end_deq.insert(after, end)
            return True

        return False



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)



if __name__ == "__main__":
    # test cases
    obj = MyCalendar()
    tests = [
        [10, 20],
        [15, 25],
        [20, 30],
    ]
    tests2 = [
        [0, 4], [40, 46], [2, 6], [50, 56], [4, 8], [60, 66], [6, 10], [70, 76], [8, 12], [80, 86], [10, 14], [90, 96],
        [12, 16], [100, 106], [14, 18], [110, 116], [16, 20], [120, 126], [18, 22], [130, 136], [20, 24], [140, 146],
        [22, 26], [150, 156], [24, 28], [160, 166], [26, 30], [170, 176], [28, 32], [180, 186], [30, 34], [190, 196],
        [32, 36], [200, 206], [34, 38], [210, 216], [36, 40], [220, 226], [38, 42], [230, 236], [40, 44], [240, 246],
        [42, 46], [250, 256], [44, 48], [260, 266], [46, 50], [270, 276], [48, 52], [280, 286], [50, 54], [290, 296],
        [52, 56], [300, 306], [54, 58], [310, 316], [56, 60], [320, 326], [58, 62], [330, 336], [60, 64], [340, 346],
        [62, 66], [350, 356], [64, 68], [360, 366], [66, 70], [370, 376], [68, 72], [380, 386], [70, 74], [390, 396],
        [72, 76], [400, 406], [74, 78], [410, 416], [76, 80], [420, 426], [78, 82], [430, 436], [80, 84], [440, 446],
        [82, 86], [450, 456], [84, 88], [460, 466], [86, 90], [470, 476], [88, 92], [480, 486], [90, 94], [490, 496],
        [92, 96], [500, 506], [94, 98], [510, 516], [96, 100], [520, 526], [98, 102], [530, 536], [100, 104],
        [540, 546], [102, 106], [550, 556], [104, 108], [560, 566], [106, 110], [570, 576], [108, 112], [580, 586],
        [110, 114], [590, 596], [112, 116], [600, 606], [114, 118], [610, 616], [116, 120], [620, 626], [118, 122],
        [630, 636], [120, 124], [640, 646], [122, 126], [650, 656], [124, 128], [660, 666], [126, 130], [670, 676],
        [128, 132], [680, 686], [130, 134], [690, 696], [132, 136], [700, 706], [134, 138], [710, 716], [136, 140],
        [720, 726], [138, 142], [730, 736], [140, 144], [740, 746], [142, 146], [750, 756], [144, 148], [760, 766],
        [146, 150], [770, 776], [148, 152], [780, 786], [150, 154], [790, 796], [152, 156], [800, 806], [154, 158],
        [810, 816], [156, 160], [820, 826], [158, 162], [830, 836], [160, 164], [840, 846], [162, 166], [850, 856],
        [164, 168], [860, 866], [166, 170], [870, 876], [168, 172], [880, 886], [170, 174], [890, 896], [172, 176],
        [900, 906], [174, 178], [910, 916], [176, 180], [920, 926], [178, 182], [930, 936], [180, 184], [940, 946],
        [182, 186], [950, 956], [184, 188], [960, 966], [186, 190], [970, 976], [188, 192], [980, 986], [190, 194],
        [990, 996], [192, 196], [1000, 1006], [194, 198], [1010, 1016], [196, 200], [1020, 1026], [198, 202],
        [1030, 1036]
    ]

    for t in tests2:
        print(t)
        print(obj.book(*t), end="\n\n")



    # a = 0
    # b = 40
    # e = 1
    # li = [[]]
    # for i in range(200):
    #     c = [a, a + 3]
    #     d = [b, b + 5]
    #     f = [e, e + 1]
    #     li.append(c)
    #     li.append(d)
    #     li.append(f)
    #     # print([a, a + 4], end="")
    #     # print(obj.book(a, a + 4))
    #     # print([b, b + 6], end="")
    #     # print(obj.book(b, b + 6))
    #     a += 3
    #     b += 8
    #     e += 1

    # print(li)


    # print("[\"MyCalendar\",",end="")
    # for _ in range(len(li) - 1):
    #     print("\"book\",", end="")


#     print("[null,true,true,false,true,true,true,false,true,true,true,false,true,true,true,true,true,true,true,true,true,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,false,true,false,true,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,true,true,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,false,true,false,true,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,false,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true,true]"
#           == "[null,true,true,false,true,true,true,false,true,true,true,false,true,true,true,false,true,true,true,false,true,true,true,false,true,true,true,false,true,true,true,false,true,true,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true,false,true,false,true,false,true,true,true,false,true]")
#

# a = "[null,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false]"
# b = "[null,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,true,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,false,true,true,false,false,true,false,false,true,false,false,true,false,false,true,false,false,true,true,false,true,true,false,true,true,true,true,false]"
#
# print(len(a.split(",")))
# print(len(b.split(",")))
# print(a == b)

"""
["MyCalendar","book","book","book"]
[[],[10,20],[15,25],[20,30]]


["MyCalendar","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
[[], [0, 4], [40, 46], [2, 6], [50, 56], [4, 8], [60, 66], [6, 10], [70, 76], [8, 12], [80, 86], [10, 14], [90, 96], [12, 16], [100, 106], [14, 18], [110, 116], [16, 20], [120, 126], [18, 22], [130, 136], [20, 24], [140, 146], [22, 26], [150, 156], [24, 28], [160, 166], [26, 30], [170, 176], [28, 32], [180, 186], [30, 34], [190, 196], [32, 36], [200, 206], [34, 38], [210, 216], [36, 40], [220, 226], [38, 42], [230, 236], [40, 44], [240, 246], [42, 46], [250, 256], [44, 48], [260, 266], [46, 50], [270, 276], [48, 52], [280, 286], [50, 54], [290, 296], [52, 56], [300, 306], [54, 58], [310, 316], [56, 60], [320, 326], [58, 62], [330, 336], [60, 64], [340, 346], [62, 66], [350, 356], [64, 68], [360, 366], [66, 70], [370, 376], [68, 72], [380, 386], [70, 74], [390, 396], [72, 76], [400, 406], [74, 78], [410, 416], [76, 80], [420, 426], [78, 82], [430, 436], [80, 84], [440, 446], [82, 86], [450, 456], [84, 88], [460, 466], [86, 90], [470, 476], [88, 92], [480, 486], [90, 94], [490, 496], [92, 96], [500, 506], [94, 98], [510, 516], [96, 100], [520, 526], [98, 102], [530, 536], [100, 104], [540, 546], [102, 106], [550, 556], [104, 108], [560, 566], [106, 110], [570, 576], [108, 112], [580, 586], [110, 114], [590, 596], [112, 116], [600, 606], [114, 118], [610, 616], [116, 120], [620, 626], [118, 122], [630, 636], [120, 124], [640, 646], [122, 126], [650, 656], [124, 128], [660, 666], [126, 130], [670, 676], [128, 132], [680, 686], [130, 134], [690, 696], [132, 136], [700, 706], [134, 138], [710, 716], [136, 140], [720, 726], [138, 142], [730, 736], [140, 144], [740, 746], [142, 146], [750, 756], [144, 148], [760, 766], [146, 150], [770, 776], [148, 152], [780, 786], [150, 154], [790, 796], [152, 156], [800, 806], [154, 158], [810, 816], [156, 160], [820, 826], [158, 162], [830, 836], [160, 164], [840, 846], [162, 166], [850, 856], [164, 168], [860, 866], [166, 170], [870, 876], [168, 172], [880, 886], [170, 174], [890, 896], [172, 176], [900, 906], [174, 178], [910, 916], [176, 180], [920, 926], [178, 182], [930, 936], [180, 184], [940, 946], [182, 186], [950, 956], [184, 188], [960, 966], [186, 190], [970, 976], [188, 192], [980, 986], [190, 194], [990, 996], [192, 196], [1000, 1006], [194, 198], [1010, 1016], [196, 200], [1020, 1026], [198, 202], [1030, 1036]]

["MyCalendar","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
[[], [0, 3], [40, 45], [1, 2], [3, 6], [48, 53], [2, 3], [6, 9], [56, 61], [3, 4], [9, 12], [64, 69], [4, 5], [12, 15], [72, 77], [5, 6], [15, 18], [80, 85], [6, 7], [18, 21], [88, 93], [7, 8], [21, 24], [96, 101], [8, 9], [24, 27], [104, 109], [9, 10], [27, 30], [112, 117], [10, 11], [30, 33], [120, 125], [11, 12], [33, 36], [128, 133], [12, 13], [36, 39], [136, 141], [13, 14], [39, 42], [144, 149], [14, 15], [42, 45], [152, 157], [15, 16], [45, 48], [160, 165], [16, 17], [48, 51], [168, 173], [17, 18], [51, 54], [176, 181], [18, 19], [54, 57], [184, 189], [19, 20], [57, 60], [192, 197], [20, 21], [60, 63], [200, 205], [21, 22], [63, 66], [208, 213], [22, 23], [66, 69], [216, 221], [23, 24], [69, 72], [224, 229], [24, 25], [72, 75], [232, 237], [25, 26], [75, 78], [240, 245], [26, 27], [78, 81], [248, 253], [27, 28], [81, 84], [256, 261], [28, 29], [84, 87], [264, 269], [29, 30], [87, 90], [272, 277], [30, 31], [90, 93], [280, 285], [31, 32], [93, 96], [288, 293], [32, 33], [96, 99], [296, 301], [33, 34], [99, 102], [304, 309], [34, 35], [102, 105], [312, 317], [35, 36], [105, 108], [320, 325], [36, 37], [108, 111], [328, 333], [37, 38], [111, 114], [336, 341], [38, 39], [114, 117], [344, 349], [39, 40], [117, 120], [352, 357], [40, 41], [120, 123], [360, 365], [41, 42], [123, 126], [368, 373], [42, 43], [126, 129], [376, 381], [43, 44], [129, 132], [384, 389], [44, 45], [132, 135], [392, 397], [45, 46], [135, 138], [400, 405], [46, 47], [138, 141], [408, 413], [47, 48], [141, 144], [416, 421], [48, 49], [144, 147], [424, 429], [49, 50], [147, 150], [432, 437], [50, 51], [150, 153], [440, 445], [51, 52], [153, 156], [448, 453], [52, 53], [156, 159], [456, 461], [53, 54], [159, 162], [464, 469], [54, 55], [162, 165], [472, 477], [55, 56], [165, 168], [480, 485], [56, 57], [168, 171], [488, 493], [57, 58], [171, 174], [496, 501], [58, 59], [174, 177], [504, 509], [59, 60], [177, 180], [512, 517], [60, 61], [180, 183], [520, 525], [61, 62], [183, 186], [528, 533], [62, 63], [186, 189], [536, 541], [63, 64], [189, 192], [544, 549], [64, 65], [192, 195], [552, 557], [65, 66], [195, 198], [560, 565], [66, 67], [198, 201], [568, 573], [67, 68], [201, 204], [576, 581], [68, 69], [204, 207], [584, 589], [69, 70], [207, 210], [592, 597], [70, 71], [210, 213], [600, 605], [71, 72], [213, 216], [608, 613], [72, 73], [216, 219], [616, 621], [73, 74], [219, 222], [624, 629], [74, 75], [222, 225], [632, 637], [75, 76], [225, 228], [640, 645], [76, 77], [228, 231], [648, 653], [77, 78], [231, 234], [656, 661], [78, 79], [234, 237], [664, 669], [79, 80], [237, 240], [672, 677], [80, 81], [240, 243], [680, 685], [81, 82], [243, 246], [688, 693], [82, 83], [246, 249], [696, 701], [83, 84], [249, 252], [704, 709], [84, 85], [252, 255], [712, 717], [85, 86], [255, 258], [720, 725], [86, 87], [258, 261], [728, 733], [87, 88], [261, 264], [736, 741], [88, 89], [264, 267], [744, 749], [89, 90], [267, 270], [752, 757], [90, 91], [270, 273], [760, 765], [91, 92], [273, 276], [768, 773], [92, 93], [276, 279], [776, 781], [93, 94], [279, 282], [784, 789], [94, 95], [282, 285], [792, 797], [95, 96], [285, 288], [800, 805], [96, 97], [288, 291], [808, 813], [97, 98], [291, 294], [816, 821], [98, 99], [294, 297], [824, 829], [99, 100], [297, 300], [832, 837], [100, 101], [300, 303], [840, 845], [101, 102], [303, 306], [848, 853], [102, 103], [306, 309], [856, 861], [103, 104], [309, 312], [864, 869], [104, 105], [312, 315], [872, 877], [105, 106], [315, 318], [880, 885], [106, 107], [318, 321], [888, 893], [107, 108], [321, 324], [896, 901], [108, 109], [324, 327], [904, 909], [109, 110], [327, 330], [912, 917], [110, 111], [330, 333], [920, 925], [111, 112], [333, 336], [928, 933], [112, 113], [336, 339], [936, 941], [113, 114], [339, 342], [944, 949], [114, 115], [342, 345], [952, 957], [115, 116], [345, 348], [960, 965], [116, 117], [348, 351], [968, 973], [117, 118], [351, 354], [976, 981], [118, 119], [354, 357], [984, 989], [119, 120], [357, 360], [992, 997], [120, 121], [360, 363], [1000, 1005], [121, 122], [363, 366], [1008, 1013], [122, 123], [366, 369], [1016, 1021], [123, 124], [369, 372], [1024, 1029], [124, 125], [372, 375], [1032, 1037], [125, 126], [375, 378], [1040, 1045], [126, 127], [378, 381], [1048, 1053], [127, 128], [381, 384], [1056, 1061], [128, 129], [384, 387], [1064, 1069], [129, 130], [387, 390], [1072, 1077], [130, 131], [390, 393], [1080, 1085], [131, 132], [393, 396], [1088, 1093], [132, 133], [396, 399], [1096, 1101], [133, 134], [399, 402], [1104, 1109], [134, 135], [402, 405], [1112, 1117], [135, 136], [405, 408], [1120, 1125], [136, 137], [408, 411], [1128, 1133], [137, 138], [411, 414], [1136, 1141], [138, 139], [414, 417], [1144, 1149], [139, 140], [417, 420], [1152, 1157], [140, 141], [420, 423], [1160, 1165], [141, 142], [423, 426], [1168, 1173], [142, 143], [426, 429], [1176, 1181], [143, 144], [429, 432], [1184, 1189], [144, 145], [432, 435], [1192, 1197], [145, 146], [435, 438], [1200, 1205], [146, 147], [438, 441], [1208, 1213], [147, 148], [441, 444], [1216, 1221], [148, 149], [444, 447], [1224, 1229], [149, 150], [447, 450], [1232, 1237], [150, 151], [450, 453], [1240, 1245], [151, 152], [453, 456], [1248, 1253], [152, 153], [456, 459], [1256, 1261], [153, 154], [459, 462], [1264, 1269], [154, 155], [462, 465], [1272, 1277], [155, 156], [465, 468], [1280, 1285], [156, 157], [468, 471], [1288, 1293], [157, 158], [471, 474], [1296, 1301], [158, 159], [474, 477], [1304, 1309], [159, 160], [477, 480], [1312, 1317], [160, 161], [480, 483], [1320, 1325], [161, 162], [483, 486], [1328, 1333], [162, 163], [486, 489], [1336, 1341], [163, 164], [489, 492], [1344, 1349], [164, 165], [492, 495], [1352, 1357], [165, 166], [495, 498], [1360, 1365], [166, 167], [498, 501], [1368, 1373], [167, 168], [501, 504], [1376, 1381], [168, 169], [504, 507], [1384, 1389], [169, 170], [507, 510], [1392, 1397], [170, 171], [510, 513], [1400, 1405], [171, 172], [513, 516], [1408, 1413], [172, 173], [516, 519], [1416, 1421], [173, 174], [519, 522], [1424, 1429], [174, 175], [522, 525], [1432, 1437], [175, 176], [525, 528], [1440, 1445], [176, 177], [528, 531], [1448, 1453], [177, 178], [531, 534], [1456, 1461], [178, 179], [534, 537], [1464, 1469], [179, 180], [537, 540], [1472, 1477], [180, 181], [540, 543], [1480, 1485], [181, 182], [543, 546], [1488, 1493], [182, 183], [546, 549], [1496, 1501], [183, 184], [549, 552], [1504, 1509], [184, 185], [552, 555], [1512, 1517], [185, 186], [555, 558], [1520, 1525], [186, 187], [558, 561], [1528, 1533], [187, 188], [561, 564], [1536, 1541], [188, 189], [564, 567], [1544, 1549], [189, 190], [567, 570], [1552, 1557], [190, 191], [570, 573], [1560, 1565], [191, 192], [573, 576], [1568, 1573], [192, 193], [576, 579], [1576, 1581], [193, 194], [579, 582], [1584, 1589], [194, 195], [582, 585], [1592, 1597], [195, 196], [585, 588], [1600, 1605], [196, 197], [588, 591], [1608, 1613], [197, 198], [591, 594], [1616, 1621], [198, 199], [594, 597], [1624, 1629], [199, 200], [597, 600], [1632, 1637], [200, 201]]

"""

