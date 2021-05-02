"""
There are n different online courses numbered from 1 to n. You are given an array courses where
courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for duration i days
and must be finished before or on last Dayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.
Return the maximum number of courses that you can take.

Example 1:
    Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    Output: 3
    Explanation:
        There are totally 4 courses, but you can take 3 courses at most:
        First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the
        next course on the 101st day.
        Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take
        the next course on the 1101st day.
        Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
        The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2:
    Input: courses = [[1,2]]
    Output: 1
Example 3:
    Input: courses = [[3,2],[4,3]]
    Output: 0

Constraints:
    1 <= courses.length <= 104
    1 <= durationi, lastDayi <= 104
Hint #1
    During iteration, say I want to add the current course, currentTotalTime being total time of all courses taken till
    now, but adding the current course might exceed my deadline or it doesn’t.
    1. If it doesn’t, then I have added one new course. Increment the currentTotalTime with duration of current course.
 Hint #2
    2. If it exceeds deadline, I can swap current course with current courses that has biggest duration.
    * No harm done and I might have just reduced the currentTotalTime, right?
    * What preprocessing do I need to do on my course processing order so that this swap is always legal?
"""
from typing import List
import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses_by_end = sorted(courses, key=lambda x: (x[1], x[0]))
        heap = []
        curr_start = 0
        for course in courses_by_end:
            if curr_start + course[0] <= course[1]:
                curr_start += course[0]
                heapq.heappush(heap, -course[0])
            elif heap and course[0] < -heap[0]:
                r = -heapq.heappushpop(heap, -course[0])
                curr_start += course[0] - r

        return len(heap)


# Test cases
obj = Solution()

tests = [
    [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]],
    [[1, 2]],
    [[3, 2], [4, 3]],
    [[100, 200], [300, 600], [300, 800], [200, 1300], [400, 1600], [500, 2500], [600, 3000], [900, 3000], [1200, 4000],
     [1000, 1250],
     [2000, 3200], [900, 3500]],
    [[100, 200], [300, 600], [300, 800], [200, 1300], [400, 1600], [500, 2500], [600, 3000], [900, 3000], [1200, 4000],
     [1000, 1250],
     [2000, 3200], [900, 3500], [800, 2200], [300, 1600], [300, 1800], [200, 1300], [400, 4600], [2000, 5500],
     [600, 5000], [900, 6000], [1200, 6000], [1000, 6550], [2000, 7200], [900, 7000]],
    [[100, 200], [300, 600], [300, 800], [300, 900], [400, 1600], [200, 1300], [400, 1600], [500, 1600], [500, 2500],
     [600, 3000], [600, 3000], [900, 3000], [1000, 4000], [800, 4000], [700, 4000], [1200, 4000], [1300, 4000],
     [500, 4000], [600, 4000], [6500, 4000], [750, 4000], [850, 4000], [200, 4000], [950, 4000], [550, 4000],
     [1000, 1250], [310, 4250], [260, 5250], [360, 5050], [180, 3650], [250, 3250], [350, 4280], [700, 4650],
     [100, 3850], [310, 6250], [200, 5250], [380, 5050], [180, 3850], [250, 3650], [350, 4580], [700, 5950],
     [160, 4250], [260, 4250], [240, 5250], [300, 5050], [120, 3650], [220, 3250], [300, 4280], [300, 4650],
     [2000, 3200], [900, 3500], [800, 2200], [300, 1600], [300, 1800], [200, 1300], [400, 4600], [2000, 5500],
     [600, 5000], [900, 6000], [1200, 6000], [1000, 6550], [2000, 7200], [900, 7000], [100, 200], [300, 600],
     [300, 800], [300, 900], [400, 1600], [200, 1300], [400, 1600], [500, 1600], [500, 2500], [600, 3000], [600, 3000],
     [900, 3000], [1000, 4000], [800, 4000], [700, 4000], [1200, 4000], [1300, 4000], [500, 4000], [600, 4000],
     [6500, 4000], [750, 4000], [850, 4000], [200, 4000], [950, 4000], [550, 4000], [1000, 1250], [310, 4250],
     [260, 5250], [360, 5050], [180, 3650], [250, 3250], [350, 4280], [700, 4650], [100, 3850], [310, 6250],
     [200, 5250], [380, 5050], [180, 3850], [250, 3650], [350, 4580], [700, 5950], [160, 4250], [260, 4250],
     [240, 5250], [300, 5050], [120, 3650], [220, 3250], [300, 4280], [300, 4650], [2000, 3200], [900, 3500],
     [800, 2200], [300, 1600], [300, 1800], [200, 1300], [400, 4600], [2000, 5500], [600, 5000], [900, 6000],
     [1200, 6000], [1000, 6550], [2000, 7200], [900, 7000], [100, 200], [300, 600], [300, 800], [300, 900], [400, 1600],
     [200, 1300], [400, 1600], [500, 1600], [500, 2500], [600, 3000], [600, 3000], [900, 3000], [1000, 4000],
     [800, 4000], [700, 4000], [1200, 4000], [1300, 4000], [500, 4000], [600, 4000], [6500, 4000], [750, 4000],
     [850, 4000], [200, 4000], [950, 4000], [550, 4000], [1000, 1250], [310, 4250], [260, 5250], [360, 5050],
     [180, 3650], [250, 3250], [350, 4280], [700, 4650], [100, 3850], [310, 6250], [200, 5250], [380, 5050],
     [180, 3850], [250, 3650], [350, 4580], [700, 5950], [160, 4250], [260, 4250], [240, 5250], [300, 5050],
     [120, 3650], [220, 3250], [300, 4280], [300, 4650], [2000, 3200], [900, 3500], [800, 2200], [300, 1600],
     [300, 1800], [200, 1300], [400, 4600], [2000, 5500], [600, 5000], [900, 6000], [1200, 6000], [1000, 6550],
     [2000, 7200], [900, 7000], [100, 200], [300, 600], [300, 800], [300, 900], [400, 1600], [200, 1300], [400, 1600],
     [500, 1600], [500, 2500], [600, 3000], [600, 3000], [900, 3000], [1000, 4000], [800, 4000], [700, 4000],
     [1200, 4000], [1300, 4000], [500, 4000], [600, 4000], [6500, 4000], [750, 4000], [850, 4000], [200, 4000],
     [950, 4000], [550, 4000], [1000, 1250], [310, 4250], [260, 5250], [360, 5050], [180, 3650], [250, 3250],
     [350, 4280], [700, 4650], [100, 3850], [310, 6250], [200, 5250], [380, 5050], [180, 3850], [250, 3650],
     [350, 4580], [700, 5950], [160, 4250], [260, 4250], [240, 5250], [300, 5050], [120, 3650], [220, 3250],
     [300, 4280], [300, 4650], [2000, 3200], [900, 3500], [800, 2200], [300, 1600], [300, 1800], [200, 1300],
     [400, 4600], [2000, 5500], [600, 5000], [900, 6000], [1200, 6000], [1000, 6550], [2000, 7200], [900, 7000],
     [100, 200], [300, 600], [300, 800], [300, 900], [400, 1600], [200, 1300], [400, 1600], [500, 1600], [500, 2500],
     [600, 3000], [600, 3000], [900, 3000], [1000, 4000], [800, 4000], [700, 4000], [1200, 4000], [1300, 4000],
     [500, 4000], [600, 4000], [6500, 4000], [750, 4000], [850, 4000], [200, 4000], [950, 4000], [550, 4000],
     [1000, 1250], [310, 4250], [260, 5250], [360, 5050], [180, 3650], [250, 3250], [350, 4280], [700, 4650],
     [100, 3850], [310, 6250], [200, 5250], [380, 5050], [180, 3850], [250, 3650], [350, 4580], [700, 5950],
     [160, 4250], [260, 4250], [240, 5250], [300, 5050], [120, 3650], [220, 3250], [300, 4280], [300, 4650],
     [2000, 3200], [900, 3500], [800, 2200], [300, 1600], [300, 1800], [200, 1300], [400, 4600], [2000, 5500],
     [600, 5000], [900, 6000], [1200, 6000], [1000, 6550], [2000, 7200], [900, 7000], [100, 200], [300, 600],
     [300, 800], [300, 900], [400, 1600], [200, 1300], [400, 1600], [500, 1600], [500, 2500], [600, 3000], [600, 3000],
     [900, 3000], [1000, 4000], [800, 4000], [700, 4000], [1200, 4000], [1300, 4000], [500, 4000], [600, 4000],
     [6500, 4000], [750, 4000], [850, 4000], [200, 4000], [950, 4000], [550, 4000], [1000, 1250], [310, 4250],
     [260, 5250], [360, 5050], [180, 3650], [250, 3250], [350, 4280], [700, 4650], [100, 3850], [310, 6250],
     [200, 5250], [380, 5050], [180, 3850], [250, 3650], [350, 4580], [700, 5950], [160, 4250], [260, 4250],
     [240, 5250], [300, 5050], [120, 3650], [220, 3250], [300, 4280], [300, 4650], [2000, 3200], [900, 3500],
     [800, 2200], [300, 1600], [300, 1800], [200, 1300], [400, 4600], [2000, 5500], [600, 5000], [900, 6000],
     [1200, 6000], [1000, 6550], [2000, 7200], [900, 7000], [100, 4200], [300, 4600], [300, 4800], [300, 4900],
     [400, 5600], [200, 5300], [400, 5600], [500, 5600], [500, 6500], [600, 7000], [600, 7000], [900, 7000],
     [1000, 8000], [800, 8000], [700, 8000], [1200, 8000], [1300, 8000], [500, 8000], [600, 8000], [6500, 8000],
     [750, 8000], [850, 8000], [200, 8000], [950, 8000], [550, 8000], [1000, 5250], [310, 8250], [260, 9250],
     [360, 9050], [180, 7650], [250, 7250], [350, 8280], [700, 8650], [100, 7850], [310, 9750], [200, 9250],
     [380, 9050], [180, 7850], [250, 7650], [350, 8580], [700, 9950], [160, 8250], [260, 8250], [240, 9250],
     [300, 9050], [120, 7650], [220, 7250], [300, 8280], [300, 8650], [2000, 7200], [900, 7500], [800, 6200],
     [300, 5600], [300, 5800], [200, 5300], [400, 8600], [2000, 9500], [600, 9000], [900, 10000], [1200, 10000],
     [1000, 9450], [2000, 8800], [900, 9000], [100, 4200], [300, 4600], [300, 4800], [300, 4900], [400, 5600],
     [200, 5300], [400, 5600], [500, 5600], [500, 6500], [600, 7000], [600, 7000], [900, 7000], [1000, 8000],
     [800, 8000], [700, 8000], [1200, 8000], [1300, 8000], [500, 8000], [600, 8000], [6500, 8000], [750, 8000],
     [850, 8000], [200, 8000], [950, 8000], [550, 8000], [1000, 5250], [310, 8250], [260, 9250], [360, 9050],
     [180, 7650], [250, 7250], [350, 8280], [700, 8650], [100, 7850], [310, 9750], [200, 9250], [380, 9050],
     [180, 7850], [250, 7650], [350, 8580], [700, 9950], [160, 8250], [260, 8250], [240, 9250], [300, 9050],
     [120, 7650], [220, 7250], [300, 8280], [300, 8650], [2000, 7200], [900, 7500], [800, 6200], [300, 5600],
     [300, 5800], [200, 5300], [400, 8600], [2000, 9500], [600, 9000], [900, 10000], [1200, 10000], [1000, 9450],
     [2000, 8800], [900, 9000], [100, 4200], [300, 4600], [300, 4800], [300, 4900], [400, 5600], [200, 5300],
     [400, 5600], [500, 5600], [500, 6500], [600, 7000], [600, 7000], [900, 7000], [1000, 8000], [800, 8000],
     [700, 8000], [1200, 8000], [1300, 8000], [500, 8000], [600, 8000], [6500, 8000], [750, 8000], [850, 8000],
     [200, 8000], [950, 8000], [550, 8000], [1000, 5250], [310, 8250], [260, 9250], [360, 9050], [180, 7650],
     [250, 7250], [350, 8280], [700, 8650], [100, 7850], [310, 9750], [200, 9250], [380, 9050], [180, 7850],
     [250, 7650], [350, 8580], [700, 9950], [160, 8250], [260, 8250], [240, 9250], [300, 9050], [120, 7650],
     [220, 7250], [300, 8280], [300, 8650], [2000, 7200], [900, 7500], [800, 6200], [300, 5600], [300, 5800],
     [200, 5300], [400, 8600], [2000, 9500], [600, 9000], [900, 10000], [1200, 10000], [1000, 9450], [2000, 8800],
     [900, 9000], [100, 4200], [300, 4600], [300, 4800], [300, 4900], [400, 5600], [200, 5300], [400, 5600],
     [500, 5600], [500, 6500], [600, 7000], [600, 7000], [900, 7000], [1000, 8000], [800, 8000], [700, 8000],
     [1200, 8000], [1300, 8000], [500, 8000], [600, 8000], [6500, 8000], [750, 8000], [850, 8000], [200, 8000],
     [950, 8000], [550, 8000], [1000, 5250], [310, 8250], [260, 9250], [360, 9050], [180, 7650], [250, 7250],
     [350, 8280], [700, 8650], [100, 7850], [310, 9750], [200, 9250], [380, 9050], [180, 7850], [250, 7650],
     [350, 8580], [700, 9950], [160, 8250], [260, 8250], [240, 9250], [300, 9050], [120, 7650], [220, 7250],
     [300, 8280], [300, 8650], [2000, 7200], [900, 7500], [800, 6200], [300, 5600], [300, 5800], [200, 5300],
     [400, 8600], [2000, 9500], [600, 9000], [900, 10000], [1200, 10000], [1000, 9450], [2000, 8800], [900, 9000],
     [100, 4200], [300, 4600], [300, 4800], [300, 4900], [400, 5600], [200, 5300], [400, 5600], [500, 5600],
     [500, 6500], [600, 7000], [600, 7000], [900, 7000], [1000, 8000], [800, 8000], [700, 8000], [1200, 8000],
     [1300, 8000], [500, 8000], [600, 8000], [6500, 8000], [750, 8000], [850, 8000], [200, 8000], [950, 8000],
     [550, 8000], [1000, 5250], [310, 8250], [260, 9250], [360, 9050], [180, 7650], [250, 7250], [350, 8280],
     [700, 8650], [100, 7850], [310, 9750], [200, 9250], [380, 9050], [180, 7850], [250, 7650], [350, 8580],
     [700, 9950], [160, 8250], [260, 8250], [240, 9250], [300, 9050], [120, 7650], [220, 7250], [300, 8280],
     [300, 8650], [2000, 7200], [900, 7500], [800, 6200], [300, 5600], [300, 5800], [200, 5300], [400, 8600],
     [2000, 9500], [600, 9000], [900, 10000], [1200, 10000], [1000, 9450], [2000, 8800], [900, 9000], [100, 4200],
     [300, 4600], [300, 4800], [300, 4900], [400, 5600], [200, 5300], [400, 5600], [500, 5600], [500, 6500],
     [600, 7000], [600, 7000], [900, 7000], [1000, 8000], [800, 8000], [700, 8000], [1200, 8000], [1300, 8000],
     [500, 8000], [600, 8000], [6500, 8000], [750, 8000], [850, 8000], [200, 8000], [950, 8000], [550, 8000],
     [1000, 5250], [310, 8250], [260, 9250], [360, 9050], [180, 7650], [250, 7250], [350, 8280], [700, 8650],
     [100, 7850], [310, 9750], [200, 9250], [380, 9050], [180, 7850], [250, 7650], [350, 8580], [700, 9950],
     [160, 8250], [260, 8250], [240, 9250], [300, 9050], [120, 7650], [220, 7250], [300, 8280], [300, 8650],
     [2000, 7200], [900, 7500], [800, 6200], [300, 5600], [300, 5800], [200, 5300], [400, 8600], [2000, 9500],
     [600, 9000], [900, 10000], [1200, 10000], [1000, 9450], [2000, 8800], [900, 9000], [100, 7800], [300, 8200],
     [300, 8400], [300, 8500], [400, 9200], [200, 8900], [400, 9200], [500, 9200], [500, 9900], [600, 9400],
     [600, 9400], [900, 9400], [1000, 8400], [800, 8400], [700, 8400], [1200, 8400], [1300, 8400], [500, 8400],
     [600, 8400], [6500, 8400], [750, 8400], [850, 8400], [200, 8400], [950, 8400], [550, 8400], [1000, 8850],
     [310, 8150], [260, 7150], [360, 7350], [180, 8750], [250, 9150], [350, 8120], [700, 7750], [100, 8550],
     [310, 6150], [200, 7150], [380, 7350], [180, 8550], [250, 8750], [350, 7820], [700, 6450], [160, 8150],
     [260, 8150], [240, 7150], [300, 7350], [120, 8750], [220, 9150], [300, 8120], [300, 7750], [2000, 9200],
     [900, 8900], [800, 9800], [300, 9200], [300, 9400], [200, 8900], [400, 7800], [2000, 6900], [600, 7400],
     [900, 6400], [1200, 6400], [1000, 5850], [2000, 5200], [900, 5400], [100, 7800], [300, 8200], [300, 8400],
     [300, 8500], [400, 9200], [200, 8900], [400, 9200], [500, 9200], [500, 9900], [600, 9400], [600, 9400],
     [900, 9400], [1000, 8400], [800, 8400], [700, 8400], [1200, 8400], [1300, 8400], [500, 8400], [600, 8400],
     [6500, 8400], [750, 8400], [850, 8400], [200, 8400], [950, 8400], [550, 8400], [1000, 8850], [310, 8150],
     [260, 7150], [360, 7350], [180, 8750], [250, 9150], [350, 8120], [700, 7750], [100, 8550], [310, 6150],
     [200, 7150], [380, 7350], [180, 8550], [250, 8750], [350, 7820], [700, 6450], [160, 8150], [260, 8150],
     [240, 7150], [300, 7350], [120, 8750], [220, 9150], [300, 8120], [300, 7750], [2000, 9200], [900, 8900],
     [800, 9800], [300, 9200], [300, 9400], [200, 8900], [400, 7800], [2000, 6900], [600, 7400], [900, 6400],
     [1200, 6400], [1000, 5850], [2000, 5200], [900, 5400], [100, 7800], [300, 8200], [300, 8400], [300, 8500],
     [400, 9200], [200, 8900], [400, 9200], [500, 9200], [500, 9900], [600, 9400], [600, 9400], [900, 9400],
     [1000, 8400], [800, 8400], [700, 8400], [1200, 8400], [1300, 8400], [500, 8400], [600, 8400], [6500, 8400],
     [750, 8400], [850, 8400], [200, 8400], [950, 8400], [550, 8400], [1000, 8850], [310, 8150], [260, 7150],
     [360, 7350], [180, 8750], [250, 9150], [350, 8120], [700, 7750], [100, 8550], [310, 6150], [200, 7150],
     [380, 7350], [180, 8550], [250, 8750], [350, 7820], [700, 6450], [160, 8150], [260, 8150], [240, 7150],
     [300, 7350], [120, 8750], [220, 9150], [300, 8120], [300, 7750], [2000, 9200], [900, 8900], [800, 9800],
     [300, 9200], [300, 9400], [200, 8900], [400, 7800], [2000, 6900], [600, 7400], [900, 6400], [1200, 6400],
     [1000, 5850], [2000, 5200], [900, 5400], [100, 7800], [300, 8200], [300, 8400], [300, 8500], [400, 9200],
     [200, 8900], [400, 9200], [500, 9200], [500, 9900], [600, 9400], [600, 9400], [900, 9400], [1000, 8400],
     [800, 8400], [700, 8400], [1200, 8400], [1300, 8400], [500, 8400], [600, 8400], [6500, 8400], [750, 8400],
     [850, 8400], [200, 8400], [950, 8400], [550, 8400], [1000, 8850], [310, 8150], [260, 7150], [360, 7350],
     [180, 8750], [250, 9150], [350, 8120], [700, 7750], [100, 8550], [310, 6150], [200, 7150], [380, 7350],
     [180, 8550], [250, 8750], [350, 7820], [700, 6450], [160, 8150], [260, 8150], [240, 7150], [300, 7350],
     [120, 8750], [220, 9150], [300, 8120], [300, 7750], [2000, 9200], [900, 8900], [800, 9800], [300, 9200],
     [300, 9400], [200, 8900], [400, 7800], [2000, 6900], [600, 7400], [900, 6400], [1200, 6400], [1000, 5850],
     [2000, 5200], [900, 5400], [100, 7800], [300, 8200], [300, 8400], [300, 8500], [400, 9200], [200, 8900],
     [400, 9200], [500, 9200], [500, 9900], [600, 9400], [600, 9400], [900, 9400], [1000, 8400], [800, 8400],
     [700, 8400], [1200, 8400], [1300, 8400], [500, 8400], [600, 8400], [6500, 8400], [750, 8400], [850, 8400],
     [200, 8400], [950, 8400], [550, 8400], [1000, 8850], [310, 8150], [260, 7150], [360, 7350], [180, 8750],
     [250, 9150], [350, 8120], [700, 7750], [100, 8550], [310, 6150], [200, 7150], [380, 7350], [180, 8550],
     [250, 8750], [350, 7820], [700, 6450], [160, 8150], [260, 8150], [240, 7150], [300, 7350], [120, 8750],
     [220, 9150], [300, 8120], [300, 7750], [2000, 9200], [900, 8900], [800, 9800], [300, 9200], [300, 9400],
     [200, 8900], [400, 7800], [2000, 6900], [600, 7400], [900, 6400], [1200, 6400], [1000, 5850], [2000, 5200],
     [900, 5400], [100, 7800], [300, 8200], [300, 8400], [300, 8500], [400, 9200], [200, 8900], [400, 9200],
     [500, 9200], [500, 9900], [600, 9400], [600, 9400], [900, 9400], [1000, 8400], [800, 8400], [700, 8400],
     [1200, 8400], [1300, 8400], [500, 8400], [600, 8400], [6500, 8400], [750, 8400], [850, 8400], [200, 8400],
     [950, 8400], [550, 8400], [1000, 8850], [310, 8150], [260, 7150], [360, 7350], [180, 8750], [250, 9150],
     [350, 8120], [700, 7750], [100, 8550], [310, 6150], [200, 7150], [380, 7350], [180, 8550], [250, 8750],
     [350, 7820], [700, 6450], [160, 8150], [260, 8150], [240, 7150], [300, 7350], [120, 8750], [220, 9150],
     [300, 8120], [300, 7750], [2000, 9200], [900, 8900], [800, 9800], [300, 9200], [300, 9400], [200, 8900],
     [400, 7800], [2000, 6900], [600, 7400], [900, 6400], [1200, 6400], [1000, 5850], [2000, 5200], [900, 5400],
     [100, 5700], [300, 6100], [300, 6300], [300, 6400], [400, 7100], [200, 6800], [400, 7100], [500, 7100],
     [500, 8000], [600, 8500], [600, 8500], [900, 8500], [1000, 9500], [800, 9500], [700, 9500], [1200, 9500],
     [1300, 9500], [500, 9500], [600, 9500], [6500, 9500], [750, 9500], [850, 9500], [200, 9500], [950, 9500],
     [550, 9500], [1000, 6750], [310, 9750], [260, 9250], [360, 9450], [180, 9150], [250, 8750], [350, 9780],
     [700, 9850], [100, 9350], [310, 8250], [200, 9250], [380, 9450], [180, 9350], [250, 9150], [350, 9920],
     [700, 8550], [160, 9750], [260, 9750], [240, 9250], [300, 9450], [120, 9150], [220, 8750], [300, 9780],
     [300, 9850], [2000, 8700], [900, 9000], [800, 7700], [300, 7100], [300, 7300], [200, 6800], [400, 9900],
     [2000, 9000], [600, 9500], [900, 8500], [1200, 8500], [1000, 7950], [2000, 7300], [900, 7500], [100, 5700],
     [300, 6100], [300, 6300], [300, 6400], [400, 7100], [200, 6800], [400, 7100], [500, 7100], [500, 8000],
     [600, 8500], [600, 8500], [900, 8500], [1000, 9500], [800, 9500], [700, 9500], [1200, 9500], [1300, 9500],
     [500, 9500], [600, 9500], [6500, 9500], [750, 9500], [850, 9500], [200, 9500], [950, 9500], [550, 9500],
     [1000, 6750], [310, 9750], [260, 9250], [360, 9450], [180, 9150], [250, 8750], [350, 9780], [700, 9850],
     [100, 9350], [310, 8250], [200, 9250], [380, 9450], [180, 9350], [250, 9150], [350, 9920], [700, 8550],
     [160, 9750], [260, 9750], [240, 9250], [300, 9450], [120, 9150], [220, 8750], [300, 9780], [300, 9850],
     [2000, 8700], [900, 9000], [800, 7700], [300, 7100], [300, 7300], [200, 6800], [400, 9900], [2000, 9000],
     [600, 9500], [900, 8500], [1200, 8500], [1000, 7950], [2000, 7300], [900, 7500], [100, 5700], [300, 6100],
     [300, 6300], [300, 6400], [400, 7100], [200, 6800], [400, 7100], [500, 7100], [500, 8000], [600, 8500],
     [600, 8500], [900, 8500], [1000, 9500], [800, 9500], [700, 9500], [1200, 9500], [1300, 9500], [500, 9500],
     [600, 9500], [6500, 9500], [750, 9500], [850, 9500], [200, 9500], [950, 9500], [550, 9500], [1000, 6750],
     [310, 9750], [260, 9250], [360, 9450], [180, 9150], [250, 8750], [350, 9780], [700, 9850], [100, 9350],
     [310, 8250], [200, 9250], [380, 9450], [180, 9350], [250, 9150], [350, 9920], [700, 8550], [160, 9750],
     [260, 9750], [240, 9250], [300, 9450], [120, 9150], [220, 8750], [300, 9780], [300, 9850], [2000, 8700],
     [900, 9000], [800, 7700], [300, 7100], [300, 7300], [200, 6800], [400, 9900], [2000, 9000], [600, 9500],
     [900, 8500], [1200, 8500], [1000, 7950], [2000, 7300], [900, 7500], [100, 5700], [300, 6100], [300, 6300],
     [300, 6400], [400, 7100], [200, 6800], [400, 7100], [500, 7100], [500, 8000], [600, 8500], [600, 8500],
     [900, 8500], [1000, 9500], [800, 9500], [700, 9500], [1200, 9500], [1300, 9500], [500, 9500], [600, 9500],
     [6500, 9500], [750, 9500], [850, 9500], [200, 9500], [950, 9500], [550, 9500], [1000, 6750], [310, 9750],
     [260, 9250], [360, 9450], [180, 9150], [250, 8750], [350, 9780], [700, 9850], [100, 9350], [310, 8250],
     [200, 9250], [380, 9450], [180, 9350], [250, 9150], [350, 9920], [700, 8550], [160, 9750], [260, 9750],
     [240, 9250], [300, 9450], [120, 9150], [220, 8750], [300, 9780], [300, 9850], [2000, 8700], [900, 9000],
     [800, 7700], [300, 7100], [300, 7300], [200, 6800], [400, 9900], [2000, 9000], [600, 9500], [900, 8500],
     [1200, 8500], [1000, 7950], [2000, 7300], [900, 7500], [100, 5700], [300, 6100], [300, 6300], [300, 6400],
     [400, 7100], [200, 6800], [400, 7100], [500, 7100], [500, 8000], [600, 8500], [600, 8500], [900, 8500],
     [1000, 9500], [800, 9500], [700, 9500], [1200, 9500], [1300, 9500], [500, 9500], [600, 9500], [6500, 9500],
     [750, 9500], [850, 9500], [200, 9500], [950, 9500], [550, 9500], [1000, 6750], [310, 9750], [260, 9250],
     [360, 9450], [180, 9150], [250, 8750], [350, 9780], [700, 9850], [100, 9350], [310, 8250], [200, 9250],
     [380, 9450], [180, 9350], [250, 9150], [350, 9920], [700, 8550], [160, 9750], [260, 9750], [240, 9250],
     [300, 9450], [120, 9150], [220, 8750], [300, 9780], [300, 9850], [2000, 8700], [900, 9000], [800, 7700],
     [300, 7100], [300, 7300], [200, 6800], [400, 9900], [2000, 9000], [600, 9500], [900, 8500], [1200, 8500],
     [1000, 7950], [2000, 7300], [900, 7500], [100, 5700], [300, 6100], [300, 6300], [300, 6400], [400, 7100],
     [200, 6800], [400, 7100], [500, 7100], [500, 8000], [600, 8500], [600, 8500], [900, 8500], [1000, 9500],
     [800, 9500], [700, 9500], [1200, 9500], [1300, 9500], [500, 9500], [600, 9500], [6500, 9500], [750, 9500],
     [850, 9500], [200, 9500], [950, 9500], [550, 9500], [1000, 6750], [310, 9750], [260, 9250], [360, 9450],
     [180, 9150], [250, 8750], [350, 9780], [700, 9850], [100, 9350], [310, 8250], [200, 9250], [380, 9450],
     [180, 9350], [250, 9150], [350, 9920], [700, 8550], [160, 9750], [260, 9750], [240, 9250], [300, 9450],
     [120, 9150], [220, 8750], [300, 9780], [300, 9850], [2000, 8700], [900, 9000], [800, 7700], [300, 7100],
     [300, 7300], [200, 6800], [400, 9900], [2000, 9000], [600, 9500], [900, 8500], [1200, 8500], [1000, 7950],
     [2000, 7300], [900, 7500], [100, 9500], [300, 9900], [300, 9900], [300, 9800], [400, 9100], [200, 9400],
     [400, 9100], [500, 9100], [500, 8200], [600, 7700], [600, 7700], [900, 7700], [1000, 6700], [800, 6700],
     [700, 6700], [1200, 6700], [1300, 6700], [500, 6700], [600, 6700], [6500, 6700], [750, 6700], [850, 6700],
     [200, 6700], [950, 6700], [550, 6700], [1000, 9450], [310, 6450], [260, 5450], [360, 5650], [180, 7050],
     [250, 7450], [350, 6420], [700, 6050], [100, 6850], [310, 4450], [200, 5450], [380, 5650], [180, 6850],
     [250, 7050], [350, 6120], [700, 4750], [160, 6450], [260, 6450], [240, 5450], [300, 5650], [120, 7050],
     [220, 7450], [300, 6420], [300, 6050], [2000, 7500], [900, 7200], [800, 8500], [300, 9100], [300, 8900],
     [200, 9400], [400, 6100], [2000, 5200], [600, 5700], [900, 4700], [1200, 4700], [1000, 4150], [2000, 3500],
     [900, 3700], [100, 9500], [300, 9900], [300, 9900], [300, 9800], [400, 9100], [200, 9400], [400, 9100],
     [500, 9100], [500, 8200], [600, 7700], [600, 7700], [900, 7700], [1000, 6700], [800, 6700], [700, 6700],
     [1200, 6700], [1300, 6700], [500, 6700], [600, 6700], [6500, 6700], [750, 6700], [850, 6700], [200, 6700],
     [950, 6700], [550, 6700], [1000, 9450], [310, 6450], [260, 5450], [360, 5650], [180, 7050], [250, 7450],
     [350, 6420], [700, 6050], [100, 6850], [310, 4450], [200, 5450], [380, 5650], [180, 6850], [250, 7050],
     [350, 6120], [700, 4750], [160, 6450], [260, 6450], [240, 5450], [300, 5650], [120, 7050], [220, 7450],
     [300, 6420], [300, 6050], [2000, 7500], [900, 7200], [800, 8500], [300, 9100], [300, 8900], [200, 9400],
     [400, 6100], [2000, 5200], [600, 5700], [900, 4700], [1200, 4700], [1000, 4150], [2000, 3500], [900, 3700],
     [100, 9500], [300, 9900], [300, 9900], [300, 9800], [400, 9100], [200, 9400], [400, 9100], [500, 9100],
     [500, 8200], [600, 7700], [600, 7700], [900, 7700], [1000, 6700], [800, 6700], [700, 6700], [1200, 6700],
     [1300, 6700], [500, 6700], [600, 6700], [6500, 6700], [750, 6700], [850, 6700], [200, 6700], [950, 6700],
     [550, 6700], [1000, 9450], [310, 6450], [260, 5450], [360, 5650], [180, 7050], [250, 7450], [350, 6420],
     [700, 6050], [100, 6850], [310, 4450], [200, 5450], [380, 5650], [180, 6850], [250, 7050], [350, 6120],
     [700, 4750], [160, 6450], [260, 6450], [240, 5450], [300, 5650], [120, 7050], [220, 7450], [300, 6420],
     [300, 6050], [2000, 7500], [900, 7200], [800, 8500], [300, 9100], [300, 8900], [200, 9400], [400, 6100],
     [2000, 5200], [600, 5700], [900, 4700], [1200, 4700], [1000, 4150], [2000, 3500], [900, 3700], [100, 9500],
     [300, 9900], [300, 9900], [300, 9800], [400, 9100], [200, 9400], [400, 9100], [500, 9100], [500, 8200],
     [600, 7700], [600, 7700], [900, 7700], [1000, 6700], [800, 6700], [700, 6700], [1200, 6700], [1300, 6700],
     [500, 6700], [600, 6700], [6500, 6700], [750, 6700], [850, 6700], [200, 6700], [950, 6700], [550, 6700],
     [1000, 9450], [310, 6450], [260, 5450], [360, 5650], [180, 7050], [250, 7450], [350, 6420], [700, 6050],
     [100, 6850], [310, 4450], [200, 5450], [380, 5650], [180, 6850], [250, 7050], [350, 6120], [700, 4750],
     [160, 6450], [260, 6450], [240, 5450], [300, 5650], [120, 7050], [220, 7450], [300, 6420], [300, 6050],
     [2000, 7500], [900, 7200], [800, 8500], [300, 9100], [300, 8900], [200, 9400], [400, 6100], [2000, 5200],
     [600, 5700], [900, 4700], [1200, 4700], [1000, 4150], [2000, 3500], [900, 3700], [100, 9500], [300, 9900],
     [300, 9900], [300, 9800], [400, 9100], [200, 9400], [400, 9100], [500, 9100], [500, 8200], [600, 7700],
     [600, 7700], [900, 7700], [1000, 6700], [800, 6700], [700, 6700], [1200, 6700], [1300, 6700], [500, 6700],
     [600, 6700], [6500, 6700], [750, 6700], [850, 6700], [200, 6700], [950, 6700], [550, 6700], [1000, 9450],
     [310, 6450], [260, 5450], [360, 5650], [180, 7050], [250, 7450], [350, 6420], [700, 6050], [100, 6850],
     [310, 4450], [200, 5450], [380, 5650], [180, 6850], [250, 7050], [350, 6120], [700, 4750], [160, 6450],
     [260, 6450], [240, 5450], [300, 5650], [120, 7050], [220, 7450], [300, 6420], [300, 6050], [2000, 7500],
     [900, 7200], [800, 8500], [300, 9100], [300, 8900], [200, 9400], [400, 6100], [2000, 5200], [600, 5700],
     [900, 4700], [1200, 4700], [1000, 4150], [2000, 3500], [900, 3700], [100, 9500], [300, 9900], [300, 9900],
     [300, 9800], [400, 9100], [200, 9400], [400, 9100], [500, 9100], [500, 8200], [600, 7700], [600, 7700],
     [900, 7700], [1000, 6700], [800, 6700], [700, 6700], [1200, 6700], [1300, 6700], [500, 6700], [600, 6700],
     [6500, 6700], [750, 6700], [850, 6700], [200, 6700], [950, 6700], [550, 6700], [1000, 9450], [310, 6450],
     [260, 5450], [360, 5650], [180, 7050], [250, 7450], [350, 6420], [700, 6050], [100, 6850], [310, 4450],
     [200, 5450], [380, 5650], [180, 6850], [250, 7050], [350, 6120], [700, 4750], [160, 6450], [260, 6450],
     [240, 5450], [300, 5650], [120, 7050], [220, 7450], [300, 6420], [300, 6050], [2000, 7500], [900, 7200],
     [800, 8500], [300, 9100], [300, 8900], [200, 9400], [400, 6100], [2000, 5200], [600, 5700], [900, 4700],
     [1200, 4700], [1000, 4150], [2000, 3500], [900, 3700]],
]

for t in tests:
    # print(t)
    print(obj.scheduleCourse(t))
