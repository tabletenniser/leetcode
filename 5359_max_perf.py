'''

There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation:
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72


Constraints:

1 <= n <= 10^5
speed.length == n
efficiency.length == n
1 <= speed[i] <= 10^5
1 <= efficiency[i] <= 10^8
1 <= k <= n

'''
class Solution(object):
    def maxPerfRec(self, n, k):
        assert(n > 0 and k > 0)
        speed, efficiency = self.speed, self.efficiency
        if (n,k) in self.ht:
            return self.ht[(n,k)]
        result = None
        if n == 1:
            result = speed[0], efficiency[0]
        elif k == 1:
            cur_max_perf = 0
            for i in range(n):
                perf = speed[i-1] * efficiency[i-1]
                if perf > cur_max_perf:
                    cur_max_perf = perf
                    result = speed[i-1], efficiency[i-1]
        else:
            s_no_new_p, e_no_new_p = self.maxPerfRec(n - 1, k)
            perf_no_new_p = s_no_new_p * e_no_new_p

            s_less_p, e_less_p = self.maxPerfRec(n, k - 1)
            perf_less_p = s_less_p * e_less_p

            prev_s, prev_e = self.maxPerfRec(n - 1, k - 1)
            choose_s = prev_s + speed[n-1]
            choose_e = min(prev_e, efficiency[n-1])
            perf_choose_p = choose_s * choose_e

            if perf_choose_p > perf_no_new_p and perf_choose_p > perf_less_p:
                result = choose_s, choose_e
            elif perf_no_new_p > perf_choose_p and perf_no_new_p > perf_less_p:
                result = s_no_new_p, e_no_new_p
            else:
                result = s_less_p, e_less_p
        self.ht[(n, k)] = result
        return result

    def maxPerformance(self, n, speed, efficiency, k):
        self.speed = speed
        self.efficiency = efficiency
        self.ht = dict()
        max_s, max_e = self.maxPerfRec(n, k)

        return (max_s * max_e) % (10 ** 9 + 7)

s = Solution()
# speed = [2,10,3,1,5,8]
# efficiency = [5,4,3,9,7,2]
# print(s.maxPerformance(3, speed, efficiency, 2))
speed = [1,4,1,9,4,4,4]
efficiency = [8,2,1,7,1,8,4]
print(s.maxPerformance(7, speed, efficiency, 6))
print(s.ht)
