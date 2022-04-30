'''
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array persons of size n, where persons[i] is the time that the ith person will arrive to see the flowers.
Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

Example 1:
Input: flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
Output: [1,2,2,2]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.
Example 2:
Input: flowers = [[1,10],[3,3]], persons = [3,3,2]
Output: [2,2,1]
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.

Constraints:
1 <= flowers.length <= 5 * 104
flowers[i].length == 2
1 <= starti <= endi <= 109
1 <= persons.length <= 5 * 104
1 <= persons[i] <= 109
'''
import bisect
class Solution:
    def fullBloomFlowers(self, flowers, persons):
        sorted_persons = sorted(persons)
        flowers.sort()
        f_i, p_i = 0, 0
        f_ends = []
        res_dict = dict()
        while f_i < len(flowers) or p_i < len(sorted_persons):
            if p_i>=len(sorted_persons) or (f_i < len(flowers) and flowers[f_i][0] <= sorted_persons[p_i]):
                # f_ends.append(flowers[f_i][1])
                bisect.insort_right(f_ends, flowers[f_i][1])
                # f_ends.append(flowers[f_i][1])
                f_i += 1
            else:
                # valid_flowers = list(filter(lambda x: x>=sorted_persons[p_i], f_ends))
                insertion_pt = bisect.bisect_left(f_ends, sorted_persons[p_i])
                res_dict[sorted_persons[p_i]] = len(f_ends) - insertion_pt
                p_i += 1
        print(res_dict)
        return [res_dict[p] for p in persons]

s = Solution()
flowers = [[1,6],[3,7],[9,12],[4,13]]
persons = [2,3,7,11]
res = s.fullBloomFlowers(flowers, persons)
assert res == [1,2,2,2], 'Error: {}'.format(res)
