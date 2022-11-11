"""
Leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Date: 11-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, 0
        endPtr = 1
        while end < len(nums):
            if nums[end] != nums[start]:
                start += 1
                nums[start] = nums[end]
            end += 1
        return start + 1


def test():
    testcases = [
        [[1, 1, 2], 2, [1, 2]],
        [[0, 0, 1, 1, 1, 2, 2, 3], 4, [0, 1, 2, 3]],
        [[0, 1, 1, 1, 2, 2, 3, 3, 4, 4], 5, [0, 1, 2, 3, 4]],
        [[0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]],
        [[0, 1, 2, 3, 4], 5, [0, 1, 2, 3, 4]]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.removeDuplicates(testcase[0])
        assert result == testcase[1], "Testcase {} failed! Expected: {}. Got: {}".format(
            index, testcase[1], result)
        assert testcase[0][:result] == testcase[2], "Testcase {} failed in array change! Expected: {}. Got: {}".format(
            index, testcase[2], testcase[0][:result])

if __name__ == "__main__":
    test()