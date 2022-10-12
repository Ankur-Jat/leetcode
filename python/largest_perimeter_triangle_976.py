"""
Leetcode: https://leetcode.com/problems/largest-perimeter-triangle/
Date: 12-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0


def test():
    testcases = [
        [[2, 1, 2], 5],
        [[1, 2, 1], 0]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.largestPerimeter(
            testcase[0]) == testcase[1], "Testcase {} is failing".format(index)


if __name__ == "__main__":
    test()
