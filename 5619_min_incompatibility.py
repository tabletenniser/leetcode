'''
'''
from itertools import combinations
class Solution:
    def minimumIncompatibility(self, nums, k: int) -> int:
        nums.sort()
        ss_size = len(nums) // k
        ht = {}
        res = 99999999999
        def rec(subsets, to_be_grouped):
            nonlocal res
            nonlocal ht
            incompat = sum([max(subset) - min(subset) for subset in subsets])
            if len(to_be_grouped) == 0:
                # print(subsets, incompat)
                res = min(res, incompat)
                return incompat
            # subsets.sort()
            # to_be_grouped.sort()
            if (tuple(to_be_grouped)) in ht:
                # print(subsets, to_be_grouped, incompat,ht[tuple(to_be_grouped)])
                res = min(res, incompat + ht[tuple(to_be_grouped)])
                return incompat + ht[tuple(to_be_grouped)]
            new_groups = list(combinations(to_be_grouped, ss_size))
            local_res = 99999999999
            if incompat > res:
                return local_res
            # print(subsets, to_be_grouped)
            for n_g in new_groups:
                if len(set(n_g)) != len(n_g):
                    continue
                tmp_nums = to_be_grouped[:]
                for n in n_g:
                    tmp_nums.remove(n)
                local_res = min(local_res, rec(subsets+[list(n_g)], tmp_nums))
            ht[tuple(to_be_grouped)] = local_res-incompat
            if local_res - incompat == 0:
                ht[tuple(to_be_grouped)] = 99999999999
            return local_res
        # res = rec([], nums)
        rec([], nums)
        return res if res != 99999999999 else -1

nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,11]
k=4
nums = [3,2,1,12,10,11,6,7,6,5,10,5]
k = 3
nums = [13,4,7,3,3,1,12,9,11,10,13,3,12,7]
k = 7
# nums = [6,3,8,1,3,1,2,2]
# k = 4
s = Solution()
print(s.minimumIncompatibility(nums, k))
