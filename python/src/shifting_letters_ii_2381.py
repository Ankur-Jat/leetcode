"""
Leetcode: https://leetcode.com/problems/shifting-letters-ii/
Date: 12-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        line-sweep algorithm
        """
        result = [0] * (len(s)+1)
        for start, end, diff in shifts:
            diff = 1 if diff == 1 else -1
            result[start] += diff
            result[end+1] -= diff
        result_str = ''
        prefix = 0
        for index, char in enumerate(s):
            prefix += result[index]
            result_str += chr((ord(char) - 97 + prefix) % 26 + 97)
        return result_str


def test():
    testcases = [
        ["abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]], 'ace'],
        ["dztz", [[0, 0, 0], [1, 1, 1]], 'catz']
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.shiftingLetters(testcase[0], testcase[1])
        assert result == testcase[2], "Testcase #{} failed! Expected: {}. Got: {}".format(
            index, testcase[2], result)


if __name__ == "__main__":
    test()
