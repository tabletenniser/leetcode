'''
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.
Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.
Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.

Example 1:
Input: n = 2, batteries = [3,3,3]
Output: 4
Explanation: 
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

Example 2:
Input: n = 2, batteries = [1,1,1,1]
Output: 2
Explanation: 
Initially, insert battery 0 into the first computer and battery 2 into the second computer. 
After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into the first computer and battery 3 into the second computer. 
After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
We can run the two computers simultaneously for at most 2 minutes, so we return 2.

Constraints:
1 <= n <= batteries.length <= 105
1 <= batteries[i] <= 109
'''
import heapq
class Solution:
    def maxRunTime(self, n: int, batteries) -> int:
        B = len(batteries)
        if B == n:
            return min(batteries)
        if n == 1:
            return sum(batteries)
        chosen_batteries = sorted(batteries, reverse=True)[:n]
        heapq.heapify(chosen_batteries)
        left_over_charge = sum(batteries) - sum(chosen_batteries)
        while left_over_charge > 0:
            assert len(chosen_batteries) == n, f'{chosen_batteries} len: {n}'
            print(chosen_batteries)
            least_battery = heapq.heappop(chosen_batteries)
            next_b = heapq.heappop(chosen_batteries)
            num = 1
            while next_b == least_battery:
                num += 1
                if len(chosen_batteries) == 0:
                    break
                next_b = heapq.heappop(chosen_batteries)
            diff = next_b - least_battery
            if diff == 0:
                assert num == n, f'{num} is not {n}'
                return least_battery + left_over_charge // num
            if left_over_charge >= diff * num:
                left_over_charge -= diff * num
                for _ in range(num+1):
                    heapq.heappush(chosen_batteries, next_b)
            else:
                return least_battery + left_over_charge // num
        return heapq.heappop(chosen_batteries)

n = 2
batteries = [3,3,3,3,3]
# n=2
# batteries=[1,1,1,1]
# n = 3
# batteries = [10,10,3,5]
# n = 3
# batteries = [10,5,5,5]
# n=3
# batteries=[10,10,6,9,3]
n=1
batteries=[53,96]
s = Solution()
res = s.maxRunTime(n, batteries)
print(res)
