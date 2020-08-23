'''
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake which is full of water, there will be a flood. Your goal is to avoid the flood in any lake.

Given an integer array rains where:
rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.

Return an array ans where:
ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes. (see example 4)

Example 1:
Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.

Example 2:
Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
Example 3:
Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.

Example 4:
Input: rains = [69,0,0,0,69]
Output: [-1,69,1,1,-1]
Explanation: Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1] or [-1,x,y,69,-1] is acceptable where 1 <= x,y <= 10^9

Example 5:
Input: rains = [10,20,20]
Output: []
Explanation: It will rain over lake 20 two consecutive days. There is no chance to dry any lake.

Constraints:
1 <= rains.length <= 10^5
0 <= rains[i] <= 10^9
'''
class Solution:
    def sub(self, rains):
        res = []
        hs = dict()
        slow, fast = 0, 0
        while fast < len(rains):
            r = rains[fast]
            if r != 0:
                if r in hs:
                    while True:
                        if slow >= fast:
                            return []
                        r2 = rains[slow]
                        print(r,slow,r2)
                        if r2 == 0:
                            if slow > hs[r]:
                                res.append(r)
                                slow += 1
                                break
                            else:
                                res.append(1)
                        else:
                            res.append(-1)
                        slow += 1
                hs[r] = fast
            fast += 1
        # print(slow,res)
        while slow < len(rains):
            r = rains[slow]
            num = 1 if r == 0 else -1
            res.append(num)
            slow += 1
        return res

    def avoidFloodOLD(self, rains):
        res = self.sub(rains)
        if len(res) > 0:
            return res
        # res = self.sub(rains[::-1])
        # if len(res) > 0:
        #     return res[::-1]
        return []

    def avoidFlood(self, rains):
        dry_lands = []
        last_flood = dict()
        res = []
        for i,r in enumerate(rains):
            if r == 0:
                dry_lands.append(i)
                res.append(1)
            else:
                if r in last_flood:
                    print(i,r,dry_lands,last_flood,res)
                    dried = False
                    for j,dl in enumerate(dry_lands):
                        if dl > last_flood[r]:
                            res[dl] = r
                            last_flood[r] = i
                            del dry_lands[j]
                            dried = True
                            break
                    if not dried:
                        return []
                else:
                    last_flood[r] = i
                res.append(-1)
        return res

s = Solution()
# rains = [1,2,3,4]
# assert s.avoidFlood(rains) == [-1,-1,-1,-1]
# rains = [1,2,0,0,2,1]
# print(s.avoidFlood(rains))
# assert s.avoidFlood(rains) == [-1,-1,2,1,-1,-1]
# rains = [1,2,0,1,2]
# assert s.avoidFlood(rains) == []
# # rains = [69,0,0,0,69]
# # assert s.avoidFlood(rains) == []
# rains = [10,20,20]
# assert s.avoidFlood(rains) == []
# rains = [0,1,1]
# assert s.avoidFlood(rains) == []
# rains = [1,0,2,0,2,1]
# rains = [1,0,2,0,1,2]
# rains = [1,2,0,2,3,0,1]
# assert s.avoidFlood(rains) == [-1,-1,2,-1,-1,1,-1]
# rains = [1,2,0,2,3,0,1][::-1]
# assert s.avoidFlood(rains) == [-1,-1,2,-1,-1,1,-1][::-1]
# rains = [1,1,0,0]
# assert s.avoidFlood(rains) == []
rains = [2,3,0,0,3,1,0,1,0,2,2]
print(s.avoidFlood(rains))
