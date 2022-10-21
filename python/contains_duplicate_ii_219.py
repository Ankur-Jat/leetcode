"""
Leetcode: https://leetcode.com/problems/contains-duplicate-ii/
Date: 21-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k_dict = {}
        counter = 0
        index = 0
        while index < len(nums):
            if (index - counter) > k:
                del k_dict[nums[counter]]
                counter += 1
            if nums[index] in k_dict:
                return True
            k_dict[nums[index]] = True
            index += 1
        return False


def test():
    solution = Solution()
    testcases = [
        [[1, 2, 3, 1, 2, 3], 3, True],
        [[1, 2, 3, 1, 2, 3], 2, False],
        [[1, 0, 1, 1], 1, True],
        [[1, 2, 3, 1], 2, False]
    ]
    for index, testcase in enumerate(testcases):
        assert solution.containsNearbyDuplicate(
            testcase[0], testcase[1]) == testcase[2], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
