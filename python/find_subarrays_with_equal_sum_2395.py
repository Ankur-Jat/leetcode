"""
Leetcode: https://leetcode.com/problems/find-subarrays-with-equal-sum/
Date: 3-Sep-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_dict = {}
        for i in range(1, len(nums)):
            index_sum = nums[i] + nums[i-1]
            if index_sum in sum_dict:
                return True
            sum_dict[index_sum] = i
        return False


def test():
    testcases = [
        [[4,2,4], True],
        [[1,2,3,4,5], False],
        [[0,0,0], True]
    ]
    solution = Solution()
    for i, testcase in enumerate(testcases):
        assert solution.findSubarrays(testcase[0]) == testcase[1], "Testcase #{} failed".format(i)


if __name__ == "__main__":
    test()
