"""
Leetcode: https://leetcode.com/problems/reverse-vowels-of-a-string/
Date: 3-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, len(s) - 1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        while start < end:
            while start < end and s[start] not in vowels:
                start += 1
            while end > start and s[end] not in vowels:
                end -= 1
            if start != end and s[start] in vowels and s[end] in vowels:
                s = s[0:start] + s[end] + s[start+1:end] + s[start] + s[end+1:]
                start += 1
                end -= 1
        return s


def test():
    testcases = [
        ["hello", "holle"],
        ["leetcode", "leotcede"],
        ["nkr", "nkr"],
        ["bab", "bab"],
        ["aeiou", "uoiea"],
        ["aa", "aa"],
        ["aA", "Aa"],
        ["EO", "OE"],
        ["oE", "Eo"],
        ["au", "ua"],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.reverseVowels(testcase[0])
        assert result == testcase[1], "Testcase #{} failed. Expected: {}, Actual: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
