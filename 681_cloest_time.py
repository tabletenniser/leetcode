'''
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
'''
def is_valid(digits):
    return digits[0]*10+digits[1] < 24 and digits[2]*10+digits[3] <= 59

def nextClosestTime(time):
    """
    :type time: str
    :rtype: str
    """
    h, m = int(time[:2]), int(time[3:])
    digits = [h/10, h%10, m/10, m%10]
    print digits
    i = len(digits) - 1
    new_digits = digits[::]
    while i >= 0:
        smallest_greater = 10
        for j in xrange(len(digits)):
            if digits[j] > digits[i]:
                smallest_greater = min(smallest_greater, digits[j])
        if smallest_greater < 10:
            new_digits[i] = smallest_greater
            for k in xrange(i+1, len(digits)):
                new_digits[k] = min(digits)
            if is_valid(new_digits):
                break
            new_digits = digits[::]
        i -= 1
    if i == -1:
        for i in xrange(len(digits)):
            new_digits[i] = min(digits)
    h = str(new_digits[0]*10+new_digits[1])
    if new_digits[0] == 0:
        h = '0' + h
    m = str(new_digits[2]*10+new_digits[3])
    if new_digits[2] == 0:
        m = '0' + m
    return ":".join([h, m])

print nextClosestTime("19:34")
print nextClosestTime("23:59")
print nextClosestTime("12:34")
print nextClosestTime("16:57")
print nextClosestTime("01:32")
