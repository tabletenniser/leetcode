"""
621. Task Scheduler My SubmissionsBack To Contest
User Accepted: 213
User Tried: 384
Total Accepted: 218
Total Submissions: 833
Difficulty: Medium
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        t_list = [0 for _ in xrange(26)]
        for t in tasks:
            t_list[ord(t)-ord('A')] += 1
        t_list.sort()

        required_idles_tasks = (t_list[-1] - 1) * (n+1) + 1
        i = 1
        while (i+1 <= len(t_list) and t_list[-i] == t_list[-i-1]):
            required_idles_tasks += 1
            i += 1
        return max(required_idles_tasks, len(tasks))
