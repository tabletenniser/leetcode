'''
Given 2n balls of k distinct colors. You will be given an integer array balls of size k where balls[i] is the number of balls of color i.

All the balls will be shuffled uniformly at random, then we will distribute the first n balls to the first box and the remaining n balls to the other box (Please read the explanation of the second example carefully).

Please note that the two boxes are considered different. For example, if we have two balls of colors a and b, and two boxes [] and (), then the distribution [a] (b) is considered different than the distribution [b] (a) (Please read the explanation of the first example carefully).

We want to calculate the probability that the two boxes have the same number of distinct balls.

Example 1:
Input: balls = [1,1]
Output: 1.00000
Explanation: Only 2 ways to divide the balls equally:
- A ball of color 1 to box 1 and a ball of color 2 to box 2
- A ball of color 2 to box 1 and a ball of color 1 to box 2
In both ways, the number of distinct colors in each box is equal. The probability is 2/2 = 1

Example 2:
Input: balls = [2,1,1]
Output: 0.66667
Explanation: We have the set of balls [1, 1, 2, 3]
This set of balls will be shuffled randomly and we may have one of the 12 distinct shuffles with equale probability (i.e. 1/12):
[1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
After that we add the first two balls to the first box and the second two balls to the second box.
We can see that 8 of these 12 possible random distributions have the same number of distinct colors of balls in each box.
Probability is 8/12 = 0.66667

Example 3:
Input: balls = [1,2,1,2]
Output: 0.60000
Explanation: The set of balls is [1, 2, 2, 3, 4, 4]. It is hard to display all the 180 possible random shuffles of this set but it is easy to check that 108 of them will have the same number of distinct colors in each box.
Probability = 108 / 180 = 0.6

Example 4:
Input: balls = [3,2,1]
Output: 0.30000
Explanation: The set of balls is [1, 1, 1, 2, 2, 3]. It is hard to display all the 60 possible random shuffles of this set but it is easy to check that 18 of them will have the same number of distinct colors in each box.
Probability = 18 / 60 = 0.3

Example 5:
Input: balls = [6,6,6,6,6,6]
Output: 0.90327

Constraints:
1 <= balls.length <= 8
1 <= balls[i] <= 6
sum(balls) is even.
Answers within 10^-5 of the actual value will be accepted as correct.
'''
import math
class Solution:
    def getNumerator(self, balls, bag1, bag2):
        print(balls, bag1, bag2)
        s = sum(balls)
        assert s%2 == 0
        if s == 0:
            return 1
        res = 0
        for i in range(len(balls)):
            remaining_balls = balls[:]
            # print(remaining_balls)
            if remaining_balls[i] <= 0:
                continue
            remaining_balls[i] -= 1
            if i in bag1:
                existing_color = True
            else:
                existing_color = False
            for j in range(len(remaining_balls)):
                if remaining_balls[j] <= 0:
                    continue
                remaining_balls[j] -= 1
                if (j in bag2 and existing_color) or ((j not in bag2) and (not existing_color)):
                    new_b1, new_b2 = bag1.copy(), bag2.copy()
                    new_b1.add(i)
                    new_b2.add(j)
                    res += self.getNumerator(remaining_balls, new_b1, new_b2)
                remaining_balls[j] += 1
        return res

    def getProbability(self, balls) -> float:
        n = sum(balls)
        denom = math.factorial(n)
        for b in balls:
            denom //= math.factorial(b)
        bag1, bag2 = set(), set()
        numerator = self.getNumerator(balls, bag1, bag2)
        print(numerator, denom)
        return numerator / denom



s = Solution()
# balls = [6,6,6,6,6,6]
# balls = [2,1,1]
# balls = [1,2,1,2]
balls = [3,3]
res = s.getProbability(balls)
print(res)
