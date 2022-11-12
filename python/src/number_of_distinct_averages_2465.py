"""
Leetcode: https://leetcode.com/problems/number-of-distinct-averages/
Date: 12-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def distinctAverages(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        distinct_set = set()
        start, end = 0, len(nums) - 1
        while start < end:
            distinct_set.add((nums[start] + nums[end]) / 2.0)
            start += 1
            end -= 1
        return len(distinct_set)

def test():
    testcases = [
        [[4, 1, 4, 0, 3, 5], 2],
        [[1,100], 1]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.distinctAverages(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}. Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
