"""
Leetcode: https://leetcode.com/problems/sort-characters-by-frequency/
Date: 3-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        char_dict = {}
        for char in s:
            char_dict[char] = char_dict.get(char, 0) + 1
        char_freq_list = list(char_dict.items())
        char_freq_list.sort(key=lambda x: x[1], reverse=True)
        return ''.join([char*freq for char, freq in char_freq_list])


def test():
    testcases = [
        ["abc", "abc"],
        ["cabbba", "bbbaac"]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.frequencySort(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
