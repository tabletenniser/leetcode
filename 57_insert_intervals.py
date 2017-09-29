'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def is_overlap(self, i1, i2):
        return not(i1.start > i2.end or i2.start > i1.end)

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        min_start = newInterval.start
        max_end = newInterval.end
        res = []
        while i < len(intervals):
            if self.is_overlap(intervals[i], newInterval):
                min_start = min(min_start, intervals[i].start)
                max_end = max(max_end, intervals[i].end)
            else:
                res.append(intervals[i])
            i += 1

        i = 0
        while i < len(intervals) and intervals[i].start < min_start:
            i += 1
        res.insert(i, Interval(min_start, max_end))
        return res

s = Solution()
print s.insert([Interval(1, 2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12, 16)], Interval(4,9))
