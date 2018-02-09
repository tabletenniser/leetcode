# -*- coding: utf-8 -*-
'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

 Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
Credits:
Special thanks to @stellari for adding this problem, creating these two awesome images and all test cases.
'''
from heapq import *

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        rising_edges =[]
        falling_edges =[]

        for b in buildings:
            rising_edges.append((b[0], b[2]))
            falling_edges.append((b[1], b[2]))
        rising_edges.sort()
        falling_edges.sort()

        q = []
        i, j = 0, 0
        prev_height = 0
        result = []
        while i < len(rising_edges) or j < len(falling_edges):
            if i >= len(rising_edges) or rising_edges[i][0] > falling_edges[j][0]:
                coordinate = falling_edges[j][0]
                q.remove(-falling_edges[j][1])
                heapify(q)
                j += 1
            else:
                coordinate = rising_edges[i][0]
                heappush(q, -rising_edges[i][1])
                i += 1
            cur_height = 0 if len(q) == 0 else -q[0]
            if cur_height != prev_height:
                if len(result) > 0 and result[-1][0] == coordinate:
                    result[-1][1] = max(result[-1][1], cur_height)
                else:
                    result.append([coordinate, cur_height])
                prev_height = result[-1][1]
        return result

s = Solution()
buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]
expected_key_pts = [ [2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0] ]
assert s.getSkyline(buildings) == expected_key_pts
assert s.getSkyline([[1,2,1],[1,2,2],[1,2,3]]) == [[1,3], [2,0]]
