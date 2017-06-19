"""
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
"""
class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        for i in xrange(len(arrays)):
            if arrays[i][0] < smallest:
                smallest = arrays[i][0]
                s_index = i
            if arrays[i][-1] > largest:
                largest = arrays[i][-1]
                l_index = i

        for i in xrange(len(arrays)):
            if s_index != i and arrays[i][-1] - smallest > result:
                result = arrays[i][-1] - smallest
            if l_index != i and largest - arrays[i][0] > result:
                result = largest - arrays[i][0]

        return result
