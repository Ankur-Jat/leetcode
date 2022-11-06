"""
Leetcode: https://leetcode.com/problems/orderly-queue/
Date: 6-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k >= 2:
            return ''.join(sorted(s))
        smallest = s
        original = s
        while True:
            s = s[1:] + s[0]
            if smallest > s:
                smallest = s
            if s == original:
                return smallest


def test():
    testcases = [
        ["cba", 1, "acb"],
        ["cba", 2, "abc"]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.orderlyQueue(testcase[0], testcase[1])
        assert result == testcase[2], "Testcase #{} failed. Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
