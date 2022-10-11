"""
Leetcode: https://leetcode.com/problems/increasing-triplet-subsequence/
Date: 11-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for third in nums:
            if second < third:
                return True
            if third <= first:
                first = third
            elif third <= second:
                second = third
        return False


def test():
    testcases = [
        [[1, 2, 3, 4, 5], True],
        [[5, 4, 3, 2, 1], False],
        [[1, 20, 4, 5, 30], True],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.increasingTriplet(
            testcase[0]) == testcase[1], "Testcase {} is failing".format(index)


if __name__ == "__main__":
    test()
