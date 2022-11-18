"""
Leetcode: https://leetcode.com/problems/ugly-number-ii/
Date: 18-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        factors = [2, 3, 5]
        factors_multiple_index = [0, 0, 0]
        k = len(factors)
        result = [1]
        counter = 1
        while counter < n:
            next_ugly = min([result[factors_multiple_index[i]]
                             * factors[i] for i in range(k)])
            result.append(next_ugly)
            counter += 1
            for i in range(k):
                if next_ugly == (factors[i] * result[factors_multiple_index[i]]):
                    factors_multiple_index[i] += 1
        return result[-1]


def test():
    testcases = [
        [3, 3],
        [10, 12],
        [20, 36],
        [40, 144],
        [201, 16384]
    ]

    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.nthUglyNumber(testcase[0])
        assert result == testcase[1], "Testcae #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
