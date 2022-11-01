"""
Leetcode: https://leetcode.com/problems/find-smallest-common-element-in-all-rows/
Date: 1-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution:
    def smallestCommonElement(self, mat):
        if len(mat[0]) == 1:
            return mat[0][0]
        prev_row = mat[0]
        R = len(mat)
        C = len(mat[0])
        for row in range(1, R):
            first, second = 0, 0
            inner_common = []
            while first < len(prev_row) and second < C:
                if prev_row[first] == mat[row][second]:
                    inner_common.append(mat[row][second])
                    first += 1
                    second += 1
                elif prev_row[first] < mat[row][second]:
                    first += 1
                else:
                    second += 1
            if not inner_common:
                return -1
            prev_row = inner_common
        return prev_row[0]


def test():
    testcases = [
        [[[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]], 5],
        [[[1, 2, 3], [2, 3, 4], [2, 3, 5]], 2],
        [[[1, 2, 3], [12, 13, 14], [2, 3, 5]], -1]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.smallestCommonElement(
            testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
