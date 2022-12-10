"""
Leetcode: https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/
Date: 10-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        maxLen = 0
        for word in strs:
            length = len(word)
            if word.isdigit():
                length = int(word)
            maxLen = max(maxLen, length)
        return maxLen


def test():
    testcases = [
        [["alic3", "bob", "3", "4", "00000"], 5],
        [["1", "01", "001", "0001"], 1]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.maximumValue(testcase[0])
        assert result == testcase[1], 'Testcase #{} failed! Expected: {}. Got: {}'.format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
