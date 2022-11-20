"""
Leetcode: https://leetcode.com/problems/basic-calculator/
Date: 19-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def process_stack(num=0):
            while stack:
                if stack[-1] in ["+", "-"]:
                    sign = 1 if stack.pop() == "+" else -1
                    num2 = stack.pop() if stack else 0
                    if isinstance(num2, int):
                        num = num2 + sign * num
                    else:  # this could be '('
                        stack.append(num2)
                        num *= sign
                elif stack[-1] == "(":
                    break
                else:
                    num = stack[-1]
                    break
            stack.append(num)

        stack = []
        index = 0
        while index < len(s):
            char = s[index]
            if char == ")":
                num = stack.pop()  # pop last number
                stack.pop()  # pop '(' bracket
                process_stack(num)  # process the stack now
            elif char in ["+", "(", "-"]:
                stack.append(char)
            elif s[index].isdigit():
                result = ''
                while index < len(s) and s[index].isdigit():
                    result += s[index]
                    index += 1
                num = int(result)
                process_stack(num)
                index -= 1
            index += 1
        process_stack()
        return stack[-1]


def test():
    testcases = [
        [" -2-1 + 2 ", -1],
        ["(1+(4+5+2)-3)+(6+8)", 23],
        ["1 + 1", 2],
        ["- (3 + (4 + 5))", -12],
        ["1-(     -2)", 3]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.calculate(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
