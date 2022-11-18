"""
Leetcode: https://leetcode.com/problems/rectangle-overlap/
Date: 17-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return True if (
            max(0, min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]))
            *
            max(0, min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]))
        ) else False


def test():
    testcases = [
        [[-3, 0, 3, 4], [0, -1, 9, 2], True],
        [[-2, -2, 2, 2], [-2, -2, 2, 2], True],
        [[-2, -2, 2, 2], [2, 2, 4, 4], False]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.isRectangleOverlap(testcase[0], testcase[1])
        assert result == testcase[2], "Testcase: {} failed. Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
