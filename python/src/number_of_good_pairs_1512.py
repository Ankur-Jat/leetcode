"""
Leetcode: https://leetcode.com/problems/number-of-good-pairs/
Date: 3-Oct-2023
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
Problem: Number of Good Pairs #1512
    Given an array of integers nums, return the number of good pairs.
    A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


Example 2:
Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.

Example 3:
Input: nums = [1,2,3]
Output: 0

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

from collections import Counter


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum([n * (n-1) // 2 for n in Counter(nums).values()])


def test():
    testcases = [
        [[1, 2, 3, 1, 1, 3], 4],
        [[1, 1, 1, 1], 6],
        [[1, 2, 3], 0]
    ]
    solution = Solution()
    for i, testcase in enumerate(testcases):
        assert solution.numIdenticalPairs(
            testcase[0]) == testcase[1], "Testcase #{} failed".format(i)


if __name__ == "__main__":
    test()
