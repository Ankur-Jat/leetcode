"""
Leetcode: https://leetcode.com/problems/check-distances-between-same-letters/
Date: 3-Sep-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def checkDistances(self, s, distance):
        """
        :type s: str
        :type distance: List[int]
        :rtype: bool
        """
        char_distance = {}
        for i, char in enumerate(s):
            val = ord(char) - 97
            if val in char_distance:
                char_distance[val] = i - char_distance[val] - 1
            else:
                char_distance[val] = i
        for i in range(len(distance)):
            if i in char_distance and char_distance[i] != distance[i]:
                return False
        return True


def test():
    solution = Solution()
    test_cases = [
        ["abaccb", [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], True],
        ["aa", [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], False]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.checkDistances(
            test_case[0], test_case[1]) == test_case[2], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
