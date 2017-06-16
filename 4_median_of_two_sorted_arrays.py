"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
    Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n, m = len(nums1), len(nums2)
        # Always do binary search on the smaller array
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        elif n == 0:
            if m % 2 == 0:
                return (nums2[m/2-1]+nums2[m/2])/2.0
            else:
                return nums2[m/2]
        i_min, i_max = 0, n

        # Binary search on k1
        while True:
            k1 = (i_min+i_max)/2
            k2 = (m+n+1)/2-k1           # Gurantees that there are a total of (m+n+1)/2 numbers smaller than nums1[k1] in nums1 and nums2[k2] in nums2
            #print k1,k2,nums1[k1],nums2[k2]
            if k1 < n and nums1[k1] < nums2[k2-1]:
                i_min = k1 + 1
            elif k1 > 0 and nums1[k1-1] > nums2[k2]:
                i_max = k1 -1
            else:
                if k1 == 0:
                    lower = nums2[k2-1]
                elif k2 == 0:
                    lower = nums1[k1-1]
                else:
                    lower = max(nums1[k1-1], nums2[k2-1])

                if k1 == n:
                    upper = nums2[k2]
                elif k2 == m:
                    upper = nums1[k1]
                else:
                    upper = min(nums1[k1], nums2[k2])
                if (m+n)%2 == 0:
                    return (lower+upper)/2.0
                else:
                    return lower
        return -1
