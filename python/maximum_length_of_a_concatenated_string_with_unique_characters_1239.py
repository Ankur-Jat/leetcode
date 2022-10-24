"""
Leetcode: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
Date: 24-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution:
    def maxLength(self, A):
        dp = [set()]
        for a in A:
            if len(set(a)) < len(a):
                continue
            a = set(a)
            for c in dp[:]:
                if a & c:
                    continue
                dp.append(a | c)
        return max(len(a) for a in dp)


def test():
    testcases = [
        [["un", "iq", "ue"], 4],
        [["cha","r","act","ers"], 6],
        [["aa", "bb"], 0],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.maxLength(
            testcase[0]) == testcase[1], "Testcase {} is failing".format(index)


if __name__ == "__main__":
    test()
