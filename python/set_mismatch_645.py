"""
Leetcode: https://leetcode.com/problems/set-mismatch/
Date: 23-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicateNum = None
        for index, num in enumerate(nums):
            num = abs(num)
            if nums[num - 1] < 0:
                duplicateNum = num
            else:
                nums[num - 1] = -1 * nums[num - 1]
        for index, num in enumerate(nums):
            if num > 0:
                return [duplicateNum, index + 1]


def test():
    testcases = [
        [[1, 2, 2, 4], [2, 3]],
        [[1, 1], [1, 2]],
        [[2, 1, 4, 2], [2, 3]],
        [[3, 2, 1, 2], [2, 4]],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.findErrorNums(
            testcase[0]) == testcase[1], "Testcase {} is failing".format(index)


if __name__ == "__main__":
    test()
