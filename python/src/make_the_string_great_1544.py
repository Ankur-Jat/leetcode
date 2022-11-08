"""
Leetcode: https://leetcode.com/problems/make-the-string-great/
Date: 8-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
import string


class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        while i < len(s) - 1:
            if (s[i] in string.ascii_lowercase and s[i+1] in string.ascii_uppercase and s[i] == s[i+1].lower()) or (s[i] in string.ascii_uppercase and s[i+1] in string.ascii_lowercase and s[i] == s[i+1].upper()):
                s = s[0:i] + s[i+2:]
                i = max(0, i-1)
            else:
                i += 1
        return s


def test():
    testcases = [
        ["leEeetcode", "leetcode"],
        ["abBAcC", ""],
        ["sASa", "sASa"],
        ["sss", "sss"]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.makeGood(testcase[0])
        assert result == testcase[1], "Testcase #{} failed. Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
