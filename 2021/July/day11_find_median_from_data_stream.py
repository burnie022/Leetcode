"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value
and the median is the mean of the two middle values.
    - For example, for arr = [2,3,4], the median is 3.
    - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:

    - MedianFinder() initializes the MedianFinder object.
    - void addNum(int num) adds the integer num from the data stream to the data structure.
    - double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be
        accepted.

Example 1:
Input
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    [[], [1], [2], [], [3], []]
Output
    [null, null, null, 1.5, null, 2.0]

Explanation
    MedianFinder medianFinder = new MedianFinder();
    medianFinder.addNum(1);    // arr = [1]
    medianFinder.addNum(2);    // arr = [1, 2]
    medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    // arr[1, 2, 3]
    medianFinder.findMedian(); // return 2.0

Constraints:
    -10^5 <= num <= 10^5
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.

Follow up:
    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""
import bisect


class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        mid, is_even = (len(self.nums) // 2) - 1, len(self.nums) % 2 == 0
        return (self.nums[mid] + self.nums[mid+1]) / 2 if is_even else self.nums[mid]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# if __name__ == "__main__":
#     obj = Solution()
#     tests = [
#
#     ]
#
#     for t in tests:
#         print(t)
#         print(obj.(t), end="\n\n")

"""
["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[]]

["MedianFinder","addNum","addNum","findMedian","addNum","findMedian","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[],[1],[2],[],[5],[]]

["MedianFinder","addNum","addNum","findMedian","addNum","findMedian","addNum","addNum","findMedian","addNum","findMedian","addNum","addNum","findMedian","addNum","findMedian","addNum","addNum","findMedian","addNum","findMedian","addNum","addNum","findMedian","addNum","findMedian","addNum","addNum","findMedian","addNum","findMedian","addNum","addNum","findMedian","addNum","findMedian","addNum","addNum","findMedian","addNum","findMedian"]
[[],[1],[2],[],[3],[],[1],[2],[],[5],[],[1],[2],[],[3],[],[3],[3],[],[5],[],[4],[5],[],[4],[],[5],[8],[],[5],[],[7],[8],[],[11],[],[20],[12],[],[16],[]]

["MedianFinder","addNum","findMedian"]
[[],[3],[]]

["MedianFinder","addNum","addNum","findMedian"]
[[],[1],[2],[]]
"""