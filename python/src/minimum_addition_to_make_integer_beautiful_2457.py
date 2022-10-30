"""
Leetcode: https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/
Date: 30-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        def digit_sum(num):
            sum_value = 0
            while num:
                sum_value += num % 10
                num /= 10
            return sum_value
        original_n = n
        counter = 0
        while digit_sum(n) > target:
            n = n // 10 + 1
            counter += 1
        return n * (10 ** counter) - original_n


def test():
    testcases = [
        [467, 33],
        [16, 6],
        [734504727, 10]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcase):
        assert solution.makeIntegerBeautiful(
            testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
