"""
Leetcode: https://leetcode.com/problems/determine-if-two-strings-are-close/
Date: 2-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False
        word1_dict = {}
        for char in word1:
            word1_dict[char] = word1_dict.get(char, 0) + 1
        word1_count_set = list(word1_dict.values())
        word1_count_set.sort()
        word1_char_set = list(word1_dict.keys())
        word1_char_set.sort()
        word2_dict = {}
        for char in word2:
            word2_dict[char] = word2_dict.get(char, 0) + 1
        word2_count_set = list(word2_dict.values())
        word2_count_set.sort()
        word2_char_set = list(word2_dict.keys())
        word2_char_set.sort()
        # print(word1_count_set, word2_count_set, word1_char_set, word2_char_set)
        return word1_count_set == word2_count_set and word1_char_set == word2_char_set


def test():
    testcases = [
        ["abc", "bca", True],
        ["cabbba", "abbccc", True],
        ["a", "aa", False],
        ["abbccc", "cdbbbc", False],
        ["uau", "ssx", False],
        ["kyq", "kqy", True]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.closeStrings(testcase[0], testcase[1])
        assert result == testcase[2], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[2], result)


if __name__ == "__main__":
    test()
