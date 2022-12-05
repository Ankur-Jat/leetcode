"""
Leetcode: https://leetcode.com/problems/minimum-average-difference/
Date: 5-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def minimumAverageDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        nums_sum = sum(nums)
        N = len(nums)
        running_sum = 0
        min_average = float('inf')
        min_average_index = None
        for index, num in enumerate(nums):
            running_sum += num
            current_avg_diff = abs(
                running_sum / (index+1) - (nums_sum - running_sum) / max(N - index - 1, 1))
            if min_average > current_avg_diff:
                min_average = current_avg_diff
                min_average_index = index
        return min_average_index


def test():
    testcases = [
        [[2, 5, 3, 9, 5, 3], 3],
        [[0], 0],
        [[1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], 4],
        [[1], 0],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.minimumAverageDifference(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
