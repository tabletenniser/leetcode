'''
Imagine you have a special keyboard with the following keys:

Key 1: (A): Prints one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation: 
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Example 2:
Input: N = 7
Output: 9
Explanation: 
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Note:
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.
'''
class Solution(object):
    def maxARec(self, steps_left, cur_count, cur_copy, cur_buffer, hash_table):
        #print steps_left, cur_count, cur_copy, cur_buffer
        if steps_left < 0:
            return -1
        if steps_left == 0:
            return cur_count
        if (steps_left, cur_count, cur_copy) in hash_table:
            return hash_table[(steps_left, cur_count, cur_copy)]
        resA, resB, resC, resD = 0, 0, 0, 0
        if cur_copy > 1:        # press ctrl+V
            resD = self.maxARec(steps_left - 1, cur_count + cur_copy, cur_copy, cur_buffer, hash_table)
        else:                   # press single A
            resA = self.maxARec(steps_left - 1, cur_count + 1, cur_copy, cur_buffer, hash_table)
        if cur_count > cur_copy:    # press ctrl+A,ctrl+C,ctrl+V
            resB = self.maxARec(steps_left - 3, cur_count + cur_count, cur_count, cur_count, hash_table)
        res = max(resA, resB, resD)
        hash_table[(steps_left, cur_count, cur_copy)] = res
        return res

    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        hash_table = dict()
        return self.maxARec(N, 0, 0, 0, hash_table)
