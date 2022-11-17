"""
Leetcode: https://leetcode.com/problems/rectangle-area/
Date: 17-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""

class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        return abs((ay2 - ay1) * (ax2 - ax1)) + abs((by2 - by1) * (bx2 - bx1)) - abs(max(0, min(ax2, bx2) - max(ax1, bx1)) * max(0, min(ay2, by2) - max(ay1, by1)))

def test():
    testcases = [
        [[-3, 0, 3, 4, 0, -1, 9, 2], 45],
        [[-2, -2, 2, 2, -2, -2, 2, 2], 16]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.computeArea(*testcase[0])
        assert result == testcase[1], "Testcase: {} failed. Expected: {}, Got: {}".format(index, testcase[1], result)

if __name__ == "__main__":
    test()
