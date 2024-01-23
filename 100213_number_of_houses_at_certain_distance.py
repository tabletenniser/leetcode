"""
You are given three positive integers n, x, and y.
In a city, there exist houses numbered 1 to n connected by n streets. There is a street connecting the house numbered i with the house numbered i + 1 for all 1 <= i <= n - 1 . An additional street connects the house numbered x with the house numbered y.
For each k, such that 1 <= k <= n, you need to find the number of pairs of houses (house1, house2) such that the minimum number of streets that need to be traveled to reach house2 from house1 is k.
Return a 1-indexed array result of length n where result[k] represents the total number of pairs of houses such that the minimum streets required to reach one house from the other is k.
Note that x and y can be equal.

Example 1:
Input: n = 3, x = 1, y = 3
Output: [6,0,0]
Explanation: Let's look at each pair of houses:
- For the pair (1, 2), we can go from house 1 to house 2 directly.
- For the pair (2, 1), we can go from house 2 to house 1 directly.
- For the pair (1, 3), we can go from house 1 to house 3 directly.
- For the pair (3, 1), we can go from house 3 to house 1 directly.
- For the pair (2, 3), we can go from house 2 to house 3 directly.
- For the pair (3, 2), we can go from house 3 to house 2 directly.

Example 2:
Input: n = 5, x = 2, y = 4
Output: [10,8,2,0,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (2, 4), (4, 2), (3, 4), (4, 3), (4, 5), and (5, 4).
- For k == 2, the pairs are (1, 3), (3, 1), (1, 4), (4, 1), (2, 5), (5, 2), (3, 5), and (5, 3).
- For k == 3, the pairs are (1, 5), and (5, 1).
- For k == 4 and k == 5, there are no pairs.

Example 3:
Input: n = 4, x = 1, y = 1
Output: [6,4,2,0]
Explanation: For each distance k the pairs are:
- For k == 1, the pairs are (1, 2), (2, 1), (2, 3), (3, 2), (3, 4), and (4, 3).
- For k == 2, the pairs are (1, 3), (3, 1), (2, 4), and (4, 2).
- For k == 3, the pairs are (1, 4), and (4, 1).
- For k == 4, there are no pairs.

Constraints:
2 <= n <= 105
1 <= x, y <= n
"""
import heapq
class Solution:
    def countOfPairs(self, n: int, x: int, y: int):
        res = [(i-1) * 2 for i in range(n, 0, -1)]
        total_pairs = n * (n - 1)
        assert sum(res) == total_pairs
        x, y = min(x, y), max(x, y)
        visited = set()
        pq = []
        heapq.heappush(pq, (1, x, y))
        while pq:
            cur_num, a, b = heapq.heappop(pq)
            if (a, b) in visited:
                continue
            print(cur_num, a, b, res)
            # if b - a <= cur_num or b > n or a < 1 or (a, b) in visited:
            #     continue
            res[b-a-1] -= 2
            res[cur_num - 1] += 2
            visited.add((a, b))
            for delta_a, delta_b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                new_a, new_b = a + delta_a, b + delta_b
                if new_a < 1 or new_b > n or new_b - new_a <= cur_num or new_a > new_b or (new_a, new_b) in visited:
                    continue
                heapq.heappush(pq, (cur_num + 1, new_a, new_b))
        return res


    def countOfPairsSlow(self, n: int, x: int, y: int):
        result = [0] * n
        # Loop through the list
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                # Find the minimum number of streets that need to be traveled to reach house2 from house1
                min_street = min(abs(i - j), abs(i - x) + 1 + abs(j - y), abs(i - y) + 1 + abs(j - x))
                # Increment the value of the result list at index min_street - 1
                result[min_street - 1] += 1
        return [i * 2 for i in result]


s = Solution()
# print(s.countOfPairs(100, 43, 67))
print(s.countOfPairs(6,1,5))
# print(s.countOfPairs(3,1,3))
# print(s.countOfPairs(4, 1, 1))
# # Output: [6,4,2,0]
# print(s.countOfPairs(5,2, 4))
# Output: [10,8,2,0,0]
