"""
Leetcode: https://leetcode.com/problems/di-string-match/
Date: 14-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        result = []
        l, h = 0, len(s)
        addl = False
        for index in range(0, len(s)):
            if s[index] == 'I':
                result.append(l)
                l += 1
            else:
                result.append(h)
                h -= 1
        result.append(l)
        return result


def test():
    testcases = [
        ["IDID", [0,4,1,3,2]],
        ["III", [0,1,2,3]],
        ["DDI", [3,2,0,1]]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.diStringMatch(testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
