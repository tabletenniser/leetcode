'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
'''
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def evaluate(num1, num2, op):
            if op == '+':
                return num1+num2
            if op == '-':
                return num1-num2
        i = 0
        operands = []
        operators = []
        while i < len(s):
            ch = s[i]
            if ord('0') <= ord(ch) <= ord('9'):
                num = 0
                while ord('0') <= ord(ch) <= ord('9'):
                    num = 10 * num + int(ch)
                    i += 1
                    if i >= len(s):
                        break
                    ch = s[i]
                operands.append(num)
                continue
            elif ch == '(':
                operators.append(ch)
            elif ch == ')':
                while operators[-1] != '(':
                    result = evaluate(operands[-2], operands[-1], operators[-1])
                    del operators[-1]
                    del operands[-1]
                    del operands[-1]
                    operands.append(result)
                del operators[-1]
            elif ch == '+' or ch == '-':
                while len(operators) > 0 and operators[-1] != '(':
                    result = evaluate(operands[-2], operands[-1], operators[-1])
                    del operators[-1]
                    del operands[-1]
                    del operands[-1]
                    operands.append(result)
                operators.append(ch)
            i += 1

        # print operators, operands
        while len(operators) > 0:
            result = evaluate(operands[-2], operands[-1], operators[-1])
            del operators[-1]
            del operands[-1]
            del operands[-1]
            operands.append(result)
        return operands[0]

s = Solution()
assert s.calculate("1 + 1") == 2
assert s.calculate(" 2-1 + 2 ") == 3
assert s.calculate("(1+(4+5+2)-3)+(6+8)") == 23
