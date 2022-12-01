"""
Leetcode: https://leetcode.com/problems/determine-if-string-halves-are-alike/
Date: 1-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rt`ype: bool
        """
        vowelCounter = 0
        half = len(s) // 2
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for index, char in enumerate(s):
            if char in vowels:
                if index >= half:
                    vowelCounter -= 1
                else:
                    vowelCounter += 1
        return vowelCounter == 0


def test():
    testcases = [
        ['boOk', True],
        ['tExtbOok', False]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.halvesAreAlike(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
