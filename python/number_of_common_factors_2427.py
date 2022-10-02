"""
Leetcode: https://leetcode.com/problems/number-of-common-factors/
Date: 2-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        commonFactorCount = 0
        factor = 1
        while factor <= min(a, b):
            if a % factor == 0 and b % factor == 0:
                commonFactorCount += 1
            factor += 1
        return commonFactorCount


def test():
    solution = Solution()
    test_cases = [
        [ 12, 6, 4 ],
        [ 30, 25, 2]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.commonFactors(test_case[0], test_case[1]) == test_case[2], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
