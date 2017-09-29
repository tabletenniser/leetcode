'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        if len(intervals) <= 0:
            return res
        intervals.sort(cmp = lambda x,y: x.start - y.start)
        # print intervals[0].start, intervals[1].start
        start = intervals[0].start
        max_end = intervals[0].end
        i = 1
        while i < len(intervals):
            if intervals[i].start > max_end:
                res.append([start, max_end])
                start = intervals[i].start
                max_end = intervals[i].end
            max_end = max(max_end, intervals[i].end)
            i += 1
        res.append([start, max_end])
        return res

s = Solution()
print s.merge([Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)])
print s.merge([Interval(1,4), Interval(0,4)])
print s.merge([Interval(1,4), Interval(2,3)])
print s.merge([Interval(2,3), Interval(1,4)])
