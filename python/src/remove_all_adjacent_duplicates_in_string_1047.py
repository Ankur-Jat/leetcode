"""
Leetcode: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Date: 10-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


from collections import deque


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = deque()
        for char in s:
            if stack and stack[-1] == char:
                while stack and stack[-1] == char:
                    stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


def test():
    testcases = [
        ["abbaca", "ca"],
        ["azxxzy", "ay"]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.removeDuplicates(testcase[0])
        assert result == testcase[1], "Testcase #{} failed. Expected: {}. Actual: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
