class Solution:
    def minCost(self, nums, x: int) -> int:
        minCost = sum(nums)
        print(minCost)
        curCost = nums.copy()
        shift = 1
        while shift < len(nums):
            saving = 0
            nextCost = curCost.copy()
            for i, n in enumerate(nums):
                next_i = (i+1) % len(nums)
                saving += max(curCost[next_i] - curCost[i], 0)
                nextCost[i] = min(curCost[next_i], curCost[i])
            print(curCost, minCost, saving)
            if saving > x:
                minCost = minCost - saving + x
                curCost = nextCost
            else:
                return minCost
        return minCost

s = Solution()
# print(s.minCost([1,3,2,3,1], 2))
print(s.minCost([1], 1))
