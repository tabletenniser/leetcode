'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        result = 0
        for i in xrange(len(heights)):
            if len(stack) == 0 or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and heights[stack[-1]] >= heights[i]:
                    h = heights[stack[-1]]
                    stack.pop()
                    j = -1 if len(stack) == 0 else stack[-1]
                    result = max(result, h * (i-1-j))
                stack.append(i)
        while len(stack) > 0:
            h = heights[stack[-1]]
            stack.pop()
            j = -1 if len(stack) == 0 else stack[-1]
            result = max(result, h * (len(heights)-1-j))
        return result

    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(len(heights)):
            min_height = heights[i]
            for j in xrange(i+1, len(heights)):
                min_height = min(min_height, heights[j])
                result = max(result, (j-i+1)*min_height)
        return result


s = Solution()
# assert s.largestRectangleArea([1,3,4,2,0]) == 12
assert s.largestRectangleArea2([2,1,5,6,2,3]) == 10
assert s.largestRectangleArea2([6,2,5,4,5,1,6]) == 12
assert s.largestRectangleArea2([2,1,2,1]) == 4

assert s.largestRectangleArea([2,1,5,6,2,3]) == 10
assert s.largestRectangleArea([6,2,5,4,5,1,6]) == 12
assert s.largestRectangleArea([2,1,2,1]) == 4
