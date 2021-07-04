'''
We have n buildings numbered from 0 to n - 1. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

You are given an array requests where requests[i] = [fromi, toi] represents an employee's request to transfer from building fromi to building toi.

All buildings are full, so a list of requests is achievable only if for each building, the net change in employee transfers is zero. This means the number of employees leaving is equal to the number of employees moving in. For example if n = 3 and two employees are leaving building 0, one is leaving building 1, and one is leaving building 2, there should be two employees moving to building 0, one employee moving to building 1, and one employee moving to building 2.

Return the maximum number of achievable requests.

Example 1:
Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
Output: 5
Explantion: Let's see the requests:
From building 0 we have employees x and y and both want to move to building 1.
From building 1 we have employees a and b and they want to move to buildings 2 and 0 respectively.
From building 2 we have employee z and they want to move to building 0.
From building 3 we have employee c and they want to move to building 4.
From building 4 we don't have any requests.
We can achieve the requests of users x and b by swapping their places.
We can achieve the requests of users y, a and z by swapping the places in the 3 buildings.
Example 2:
Input: n = 3, requests = [[0,0],[1,2],[2,1]]
Output: 3
Explantion: Let's see the requests:
From building 0 we have employee x and they want to stay in the same building 0.
From building 1 we have employee y and they want to move to building 2.
From building 2 we have employee z and they want to move to building 1.
We can achieve all the requests.
Example 3:
Input: n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
Output: 4

Constraints:
1 <= n <= 20
1 <= requests.length <= 16
requests[i].length == 2
0 <= fromi, toi < n
'''
from collections import defaultdict
class Solution:
    def rec(self, f, t, requests):
        print(f,t,requests)
        for i, r in enumerate(requests):
            if r is None:
                continue
            new_f, new_t = r
            if new_f in t and new_t not in t:
                requests[i] = None
                if new_t == f:
                    return new_f
                t.add(new_t)
                rec_res = self.rec(f, t, requests)
                if rec_res == new_t:
                    return new_f
                else:
                    t.remove(new_t)
                    requests[i] = r
                    if rec_res is not None:
                        return rec_res
        return None

    def maximumRequests(self, n: int, requests) -> int:
        for i, r in enumerate(requests):
            print(i,r)
            if r is None:
                continue
            f,t = r
            requests[i] = None
            if f == t:
                continue
            else:
                if self.rec(f, set([t]), requests) is None:
                    requests[i] = r
        print(requests)
        return requests.count(None)
        # ht = defaultdict(list)
        # for r in requests:
        #     ht[r[0]].append(r[1])
        # print(ht)

    def maximumRequests_BAD(self, n: int, requests) -> int:
        outs = [0 for _ in range(n)]
        ins = [0 for _ in range(n)]
        for f, t in requests:
            outs[f] += 1
            ins[t] += 1
        res = 0
        for f,t in zip(ins, outs):
            # print(f,t,res)
            res += min(f, t)
        return res

n = 5
requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
n = 4
requests = [[0,3],[3,1],[1,2],[2,0]]
n = 3
requests = [[0,0],[1,2],[2,1]]
n = 3
requests = [[0,0],[1,1],[0,0],[2,0],[2,2],[1,1],[2,1],[0,1],[0,1]]
n = 3
requests = [[2,0],[2,1],[1,0],[0,2],[1,2]]
r = 4
requests = [[0,3],[3,1],[0,1],[3,2],[2,0],[1,0],[1,0],[1,2],[2,0],[1,3],[3,0]]
s = Solution()
print(s.maximumRequests(n, requests))
