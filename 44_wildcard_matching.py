'''

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") : false
isMatch("aa","aa") : true
isMatch("aaa","aa") : false
isMatch("aa", "*") : true
isMatch("aa", "a*") : true
isMatch("ab", "?*") : true
isMatch("aab", "c*a*b") : false
'''
def isMatch(s, p):
    dp = [[False for _ in xrange(len(s)+1)] for _ in xrange(len(p)+1)]
    dp[0][0] = True     # Both pattern and string are None
    # dp[0][j] = False for j >= 1 as None pattern should not match any string
    for j in xrange(1, len(p)+1):
        if p[j-1] == '*':
            dp[j][0] = dp[j-1][0]
    for i in xrange(1, len(p)+1):
        for j in xrange(1, len(s)+1):
            if p[i-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            elif p[i-1] == s[j-1] or p[i-1] == '?':
                dp[i][j] = dp[i-1][j-1]
    return dp[len(p)][len(s)]

assert(not isMatch("aa","a"))
assert(isMatch("aa","aa"))
assert(not isMatch("aaa","aa"))
assert(isMatch("aa", "*"))
assert(isMatch("aa", "a*"))
assert(isMatch("ab", "?*"))
assert(not isMatch("aab", "c*a*b"))
print "DONE"
