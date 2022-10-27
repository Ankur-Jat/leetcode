"""
Leetcode: https://leetcode.com/problems/minimum-window-subsequence/
Date: 27-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def minWindow(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: str
        """
        index_s1, index_s2 = 0, 0
        min_subsequence_len = float('inf')
        result = ''
        while index_s1 < len(s1):
            if s1[index_s1] == s2[index_s2]:
                index_s2 += 1
                if index_s2 == len(s2):
                    index_s2 -= 1
                    start, end = index_s1, index_s1+1
                    while index_s2 >= 0:
                        if s1[start] == s2[index_s2]:
                            index_s2 -= 1
                        start -= 1
                    start += 1
                    if (end - start) < min_subsequence_len:
                        min_subsequence_len = end - start
                        result = s1[start:end]
                    index_s1, index_s2 = start, 0
            index_s1 += 1
        return result


def test():
    testcases = [
        ["abcdebdde", "bde", "bcde"],
        ["jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u", ''],
        ["jmeqksfrsdcmsiwvaovztaqenprpvnbstl",
            "fsdbst", "frsdcmsiwvaovztaqenprpvnbst"],
        ["jmseqksaaaaaaaaaaafrsdcmsiwvaovztaqenpsrpfrvnbstl", "sfr", "srpfr"]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.minWindow(
            testcase[0], testcase[1]) == testcase[2], "Testcase #{} failed.".format(index)


if __name__ == "__main__":
    test()
