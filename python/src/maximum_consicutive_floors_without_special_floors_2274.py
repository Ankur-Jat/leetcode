"""
Leetcode: https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
Date: 3-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        special.sort()
        res = max(top - special[-1], special[0] - bottom)
        for i in range(1, len(special)):
            res = max(res, special[i] - special[i-1] - 1)
        return res


def test():
    solution = Solution()
    test_cases = [
        [ 2, 9, [ 4,6, ], 3, ],
        [ 6, 8, [ 6, 7, 8, ], 0, ],
        [ 1, 23, [ 6, 23, ], 16, ],
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.maxConsecutive(test_case[0], test_case[1], test_case[2]) == test_case[3], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
