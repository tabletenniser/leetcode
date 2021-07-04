'''
You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.
There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.
Return the minimum possible maximum working time of any assignment.

Example 1:
Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.

Example 2:
Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.

Constraints:
1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107
'''
class Solution:
    def dfs(self, jobs, workers):
        if len(jobs) == 0:
            res = max([sum(w) for w in workers])
            print(workers, res)
            self.c += 1
            return res
        for w in workers:
            if sum(w)+jobs[0] >= self.cur_best:
                continue
            w.append(jobs[0])
            cur = self.dfs(jobs[1:], workers)
            self.cur_best = min(cur, self.cur_best)
            del w[-1]
        return self.cur_best
    def getGreedyMin(self, jobs, k):
        workers = [0 for _ in range(k)]
        for j in jobs:
            workers[0] += j
            workers.sort()
        print('Greedy worker assignment: ', workers)
        return max(workers)

    def minimumTimeRequired(self, jobs, k: int) -> int:
        if k == 1:
            return sum(jobs)
        if k >= len(jobs):
            return max(jobs)
        jobs.sort(reverse=True)
        self.cur_best = self.getGreedyMin(jobs, k)
        self.c = 0
        workers = [[] for _ in range(k)]
        res = self.dfs(jobs, workers)
        print(self.c)
        return res

s = Solution()
jobs = [1,2,4,7,8]
k = 2
jobs = [254,256,256,254,251,256,254,253,255,251,251,255]
k = 10
jobs = [i for i in range(1,9)]
k = 6
print(s.minimumTimeRequired(jobs, k))
