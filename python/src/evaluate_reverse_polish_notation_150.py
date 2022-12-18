"""
Leetcode: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Date: 14-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operations = {
            '/': lambda a, b: int(float(a) / b),
            '*': lambda a, b: a * b,
            '-': lambda a, b: a - b,
            '+': lambda a, b: a + b
        }
        for item in tokens:
            if item not in ['+', '-', '*', '/']:
                stack.append(int(item))
            else:
                b = stack.pop()
                a = stack.pop()
                result = operations[item](a, b)
                # print(a, b, item, result)
                stack.append(result)
        return stack[-1]


def test():
    testcases = [
        # [["2", "1", "+", "3", "*"], 9],
        # [["4", "13", "5", "/", "+"], 6],
        [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.evalRPN(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}. Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
