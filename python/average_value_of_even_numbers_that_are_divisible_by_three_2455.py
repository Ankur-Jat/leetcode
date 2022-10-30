"""
Leetcode: https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/
Date: 28-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_sum = 0
        even_count = 0
        for num in nums:
            if num % 2 == 0 and num % 3 == 0:
                even_sum += num
                even_count += 1
        return (even_sum / even_count) if even_count > 0 else 0


def test():
    testcases = [
        [[1, 3, 6, 10, 12, 15], 9],
        [[1, 2, 4, 7, 10], 0]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.averageValue(
            testcase[0]) == testcase[1], "Testcase #{} should pass".format(index)


if __name__ == "__main__":
    test()
