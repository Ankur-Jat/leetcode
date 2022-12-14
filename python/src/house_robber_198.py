"""
Leetcode: https://leetcode.com/problems/house-robber/
Date: 14-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]
        for i in range(2, len(nums)):
            dp[i+1] = nums[i] + max(dp[i-2], dp[i-1])
        return max(dp[-1], dp[-2])


def test():
    testcases = [
        [[183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168,
            128, 177, 235, 50, 81, 185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211], 3365],
        [[1, 2, 3, 1, 6, 8, 6, 8, 6, 8, 8, 8, 8, 8], 44],
        [[2,1,1,2], 4],
        [[1,2,3,4,5], 9]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.rob(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}. Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
