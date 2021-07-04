'''
Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.



Example 1:

Input: stones = [5,3,1,4,2]
Output: 6
Explanation:
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.
Example 2:

Input: stones = [7,90,5,1,100,10,10,2]
Output: 122


Constraints:

n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000

'''
class Solution:
    def minimax(self, start, end, t_sum, maxDiff):
        # hashableStones = str(stones)
        if (start, end) in self.ht:
            return self.ht[(start, end)]
        if end - start <=0:
            return 0
        s1 = self.minimax(start + 1, end, t_sum - self.stones[start], not maxDiff)
        if maxDiff:
            s1 += t_sum - self.stones[start]
        else:
            s1 -= t_sum - self.stones[start]
        s2 = self.minimax(start, end - 1, t_sum - self.stones[end], not maxDiff)
        if maxDiff:
            s2 += t_sum - self.stones[end]
        else:
            s2 -= t_sum - self.stones[end]
        if maxDiff:
            res = max(s1,s2)
        else:
            res = min(s1, s2)
        # print(start, end, s1, s2, maxDiff, res)
        self.ct += 1
        self.ht[(start, end)] = res
        return res
    def stoneGameVII(self, stones) -> int:
        self.ht = dict()
        self.ct = 0
        t_sum = sum(stones)
        self.stones = stones
        res = self.minimax(0, len(stones) - 1,  t_sum, True)
        print(self.ct)
        return res

stones = [125,192,612,551,818,628,833,495,708,770,431,954,64,333,66,557,153,379,162,534,517,636,556,537,657,482,735,287,317,890,650,941,254,848,668,686,583,270,749,1,122,882,683,753,717,214,199,407,684,914,819,777,157,823,828,260,765,218,803,7,858,328,550,522,747,898,376,709,883,845,34,325,195,915,510,710,965,221,317,35,16,781,894,582,711,858,610,168,451,900,888,54,873,537,741,563,999,279,734,192,234,345,862,985,637,853,454,953,689,516,759,300,326,345,454,296,464,524,372,195,322,878,968,230,895,719,760,300,953,454,276,920,707,150,595,51,306,604,483,763,184,761,988,911,819,163,349,47,511,852,750,265,288,520,90,315,967,788,510,34,909,435,119,275,548,119,307,69,326,626,968,997,207,172,11,609,530,910,468,733,247,527,300,693,108,211,374,619,268,919,349,370,226,168,508,605,586,471,84,305,554,32,682,989,963,60,853,460,398,273,129,295,94,735,248,835,17,323,357,326,794,410,365,923,916,837,846,974,320,508,794,596,329,972,632,578,300,11,276,493,665,149,178,514,22,275,286,322,200,390,952,614,423,29,430,897,683,197,639,108,412,622,919,876,546,289,497,208,81,150,674,126,910,821,200,407,487,990,430,633,145,649,284,347,460,713,756,194,340,30,492,864,899,922,283,29,546,986,771,601,938,533,94,417,592,621,800,13,361,177,672,81,389,133,722,600,368,141,377,29,22,704,994,216,790,717,238,601,319,485,765,555,851,544,92,722,17,346,66,97,464,356,150,61,753,797,894,365,657,620,821,858,384,593,282,107,299,545,466,553,634,981,16,852,172,867,298,887,510,923,642,507,507,679,816,302,878,710,973,379,104,561,762,23,2,694,703,169,662,447,267,259,677,639,288,69,52,77,60,821,943,673,186,333,75,401,162,190,384,190,856,771,443,197,172,168,957,254,48,307,899,105,48,596,545,240,800,531,240,30,186,804,203,275,826,679,472,611,587,414,844,164,173,988,120,758,950,599,158,90,498,89,133,500,860,320,436,709,967,574,563,137,848,436,72,730,344,439,359,964,996,667,213,975,745,26,497,346,5,558,769,385,135,684,359,650,545,86,99,124,868,95,226,10,298,43,646,735,67,569,966,746,449,619,590,135,913,213,309,957,98,666,291,29,556,236,977,957,266,400,307,918,252,875,611,91,499,72,732,546,665,354,527,189,270,697,418,659,277,705,431,523,625,349,969,64,333,188,843,344,465,377,182,413,853,788,659,744,502,289,993,382,593,251,870,568,270,662,558,971,354,76,544,231,547,250,997,284,766,772,189,15,880,403,620,941,934,665,211,272,130,42,575,583,809,446,182,468,719,708,453,873,489,136,188,486,785,636,993,927,291,843,745,375,508,83,504,882,389,309,204,846]
# stones = [7,90,5,1,100,10,10,2]
print(len(stones))
s = Solution()
print(s.stoneGameVII(2*stones[:399]))
