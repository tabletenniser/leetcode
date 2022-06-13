'''
Alice is texting Bob using her phone. The mapping of digits to letters is shown in the figure below.
In order to add a letter, Alice has to press the key of the corresponding digit i times, where i is the position of the letter in the key.
For example, to add the letter 's', Alice has to press '7' four times. Similarly, to add the letter 'k', Alice has to press '5' twice.
Note that the digits '0' and '1' do not map to any letters, so Alice does not use them.
However, due to an error in transmission, Bob did not receive Alice's text message but received a string of pressed keys instead.
For example, when Alice sent the message "bob", Bob received the string "2266622".
Given a string pressedKeys representing the string received by Bob, return the total number of possible text messages Alice could have sent.
Since the answer may be very large, return it modulo 109 + 7.

Example 1:
Input: pressedKeys = "22233"
Output: 8
Explanation:
The possible text messages Alice could have sent are:
"aaadd", "abdd", "badd", "cdd", "aaae", "abe", "bae", and "ce".
Since there are 8 possible messages, we return 8.
Example 2:

Input: pressedKeys = "222222222222222222222222222222222222"
Output: 82876089
Explanation:
There are 2082876103 possible text messages Alice could have sent.
Since we need to return the answer modulo 109 + 7, we return 2082876103 % (109 + 7) = 82876089.

Constraints:
1 <= pressedKeys.length <= 105
pressedKeys only consists of digits from '2' - '9'.
'''
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 1000000007
        three_ht = {}
        four_ht = {}
        def getCount(key, count):
            if count < 1:
                return 0
            if count == 1:
                return 1
            if key == '7' or key == '9':
                if count in four_ht:
                    return four_ht[count]
            else:
                if count in three_ht:
                    return three_ht[count]
            res = 0
            if key == '7' or key == '9':
                for i in range(1, 5):
                    res += getCount(key, count-i) % MOD
                if count <= 4:
                    res += 1
                four_ht[count] = res
            else:
                for i in range(1, 4):
                    res += getCount(key, count-i) % MOD
                if count <= 3:
                    res += 1
                three_ht[count] = res
            return res
        i = 0
        cur_count = 0
        final_res = 1
        while i < len(pressedKeys):
            cur_count += 1
            if i == len(pressedKeys)-1 or pressedKeys[i] != pressedKeys[i+1]:
                final_res = (final_res * getCount(pressedKeys[i], cur_count)) % MOD
                cur_count = 0
            i += 1
        # print(four_ht)
        # print(three_ht)
        return final_res

s = Solution()
pressedKeys = '22233'
pressedKeys = '222222222222222222222222222222222222'
res = s.countTexts(pressedKeys)
print(res)
