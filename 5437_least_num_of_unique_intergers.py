'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.


Constraints:

1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
'''
class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        ht = dict()
        reverse_lookup = dict()
        for num in arr:
            ht[num] = ht.get(num, 0) + 1
            cur_count = ht[num]
            if cur_count > 1:
                arr = reverse_lookup.get(cur_count - 1)
                arr.remove(num)
                reverse_lookup[cur_count - 1] = arr
            arr = reverse_lookup.get(cur_count, set())
            arr.add(num)
            reverse_lookup[cur_count] = arr
        # print(ht)
        # print(reverse_lookup)
        res = 0
        for key in sorted(reverse_lookup.keys()):
            count = len(reverse_lookup[key])
            # print(key,count,k,res)
            while k > 0 and count > 0 and k >= key:
                # print(k,count)
                k -= key
                count -= 1
            res += count
            # if k > 0:
            #     k = max(0, k - count)
            #     res += max(0, count-k)
            # else:
            #     res += count
        return res


s = Solution()
arr=[2,4,1,8,3,5,1,3]
k=3
# arr = [4,3,1,1,3,3,2]
# k = 3
res = s.findLeastNumOfUniqueInts(arr,k)
print(res)

