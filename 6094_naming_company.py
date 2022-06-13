'''
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:
Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.

Example 1:
Input: ideas = ["coffee","donuts","time","toffee"]
Output: 6
Explanation: The following selections are valid:
- ("coffee", "donuts"): The company name created is "doffee conuts".
- ("donuts", "coffee"): The company name created is "conuts doffee".
- ("donuts", "time"): The company name created is "tonuts dime".
- ("donuts", "toffee"): The company name created is "tonuts doffee".
- ("time", "donuts"): The company name created is "dime tonuts".
- ("toffee", "donuts"): The company name created is "doffee tonuts".
Therefore, there are a total of 6 distinct company names.
The following are some examples of invalid selections:
- ("coffee", "time"): The name "toffee" formed after swapping already exists in the original array.
- ("time", "toffee"): Both names are still the same after swapping and exist in the original array.
- ("coffee", "toffee"): Both names formed after swapping already exist in the original array.
Example 2:
Input: ideas = ["lack","back"]
Output: 0
Explanation: There are no valid selections. Therefore, 0 is returned.

Constraints:
2 <= ideas.length <= 5 * 104
1 <= ideas[i].length <= 10
ideas[i] consists of lowercase English letters.
All the strings in ideas are unique.
'''
from typing import List
from collections import defaultdict
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        first_letter_to_substring = defaultdict(set)
        substring_to_first_letter = defaultdict(set)
        for string in ideas:
            first_letter_to_substring[string[0]].add(string[1:])
            substring_to_first_letter[string[1:]].add(string[0])
        print(first_letter_to_substring)
        print(substring_to_first_letter)
        invalid_names = 0
        for string in ideas:
            for first_letter in substring_to_first_letter[string[1:]]:
                invalid_names += len(first_letter_to_substring[first_letter])
            print(invalid_names)
            for substring in first_letter_to_substring[string[0]]:
                invalid_names += len(substring_to_first_letter[substring])
            print(invalid_names)
            invalid_names -= len(first_letter_to_substring[string[0]]) + len(substring_to_first_letter[string[1:]]) - 1
            print(string, invalid_names)
        L = len(ideas)
        return L * (L - 1) - invalid_names

s = Solution()
ideas = ["coffee","donuts","time","toffee"]
res = s.distinctNames(ideas)
print(res)
