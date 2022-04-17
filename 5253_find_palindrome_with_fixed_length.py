'''
5253. Find Palindrome With Fixed Length
Given an integer array queries and a positive integer intLength, return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength or -1 if no such palindrome exists.
A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

Example 1:
Input: queries = [1,2,3,4,5,90], intLength = 3
Output: [101,111,121,131,141,999]
Explanation:
The first few palindromes of length 3 are:
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201, ...
The 90th palindrome of length 3 is 999.

Example 2:
Input: queries = [2,4,6], intLength = 4
Output: [1111,1331,1551]
Explanation:
The first six palindromes of length 4 are:
1001, 1111, 1221, 1331, 1441, and 1551.

Constraints:
1 <= queries.length <= 5 * 104
1 <= queries[i] <= 109
1 <= intLength <= 15
'''
class Solution:
    def kthPalindrome(self, queries, intLength: int):
        l = (intLength-1) // 2
        res = []
        for q in queries:
            # s = str(q+9) if intLength > 2 else str(q)
            s = str(q + (10**l-1))
            # if intLength == 1:
            #     num = q if q <= 9  else -1
            #     res.append(num)
            if intLength % 2 == 0:
                num = s+s[::-1]
                elem = int(num) if len(num) == intLength else -1
                res.append(elem)
            else:
                num = s+s[::-1][1:]
                print(num)
                elem = int(num) if len(num) == intLength else -1
                res.append(elem)
        return res

s = Solution()
queries = [1,2,3,4,5,90,91]
intLength = 3
queries=[2,201429812,8,520498110,492711727,339882032,462074369,9,7,6]
intLength=1
# queries=[392015495,5,4,1,425320571,565971690,3,7,6,3,506222280,468075092,5]
# intLength=2
# queries=[449229674,501930675,40059525,908875541,9,672504016]
# intLength=5
res = s.kthPalindrome(queries, intLength)
print(res)
