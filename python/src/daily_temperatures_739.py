"""
Leetcode: https://leetcode.com/problems/daily-temperatures/
Date: 14-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(temperatures)
        result = [0] * n
        for index in range(n):
            while stack and temperatures[index] > temperatures[stack[-1]]:
                result[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return result


def test():
    testcases = [
        [[73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]],
        [[30, 40, 50, 60], [1, 1, 1, 0]],
        [[30, 60, 90], [1, 1, 0]],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.dailyTemperatures(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}. Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
