"""
Leetcode: https://leetcode.com/problems/break-a-palindrome/
Date: 10-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        if len(palindrome) <= 1:
            return ""
        length = len(palindrome) // 2
        for index in range(length):
            if palindrome[index] != "a":
                return palindrome[0:index] + "a" + palindrome[index+1:]
        return palindrome[:-1] + "b"


def test():
    solution = Solution()
    test_cases = [
        ["aba", "abb"],
        ["aaaa", "aaab"],
        ["aabbaa", "aaabaa"],
        ["aabaa", "aabab"]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.breakPalindrome(
            test_case[0]) == test_case[1], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
