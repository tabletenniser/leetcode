'''
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account, in sorted order.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the format they were given: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
'''
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        result = []
        email_to_index_map = dict()
        for i in xrange(len(accounts)):
            account = accounts[i]
            name = account[0]
            emails = account[1:]
            common_index = None
            for email in emails:
                if email in email_to_index_map:
                    if email_to_index_map[email] != i:
                        common_index = email_to_index_map[email]
                    continue
                email_to_index_map[email] = i
            if common_index != None:
                print common_index, accounts, email_to_index_map
                known_emails = set(accounts[common_index][1:])
                for email in emails:
                    if email not in known_emails:
                        result[common_index].append(email)
                result.append(None)
            else:
                result.append(account[::])
        # print result
        result = filter(lambda a: a != None, result)
        result = map(lambda a: sorted(a[1:]), result)
        # print email_to_index_map
        return result


s = Solution()
# print s.accountsMerge([["Alex","Alex5@m.co","Alex4@m.co","Alex0@m.co"],["Ethan","Ethan3@m.co","Ethan3@m.co","Ethan0@m.co"],["Kevin","Kevin4@m.co","Kevin2@m.co","Kevin2@m.co"],["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe2@m.co"],["Gabe","Gabe3@m.co","Gabe4@m.co","Gabe2@m.co"]])
print s.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]])
# print s.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", 'john_newyork@mail.com', "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com", 'john00@mail.com'], ["Mary", "mary@mail.com"]])
