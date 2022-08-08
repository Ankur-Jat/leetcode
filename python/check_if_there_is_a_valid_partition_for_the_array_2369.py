"""
Leetcode: https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
Date: 8-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def validPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums) + 3
        dp = [0] * N
        dp[1] = dp[2] = 1
        i = 4
        while i < N:
            if nums[i-3] == nums[i-4] and dp[i-2]:
                dp[i] = 1
            elif dp[i-3]:
                if nums[i-3] == nums[i-4] and nums[i-4] == nums[i-5]:
                    dp[i] = 1
                elif nums[i-3] - nums[i-4] == 1 and nums[i-4] - nums[i-5] == 1:
                    dp[i] = 1
            i += 1
        return dp[-1]


def test():
    solution = Solution()
    test_cases = [
        [ [4,4,4,5,6], True ],
        [ [1,1,1,2], False ],
        [ [4,4,5,6,7,8,9,9,10,11,12], False ],
        [ [4,4,5,6,7,8,8,9,10,11], True ],
        [ [803201,803201,803201,803201,803202,803203], True ]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.validPartition(test_case[0]) == test_case[1], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
