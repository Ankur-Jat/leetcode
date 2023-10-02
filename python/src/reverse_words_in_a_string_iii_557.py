"""
Leetcode: https://leetcode.com/problems/reverse-words-in-a-string-iii/
Date: 2-Oct-2023
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
Problem: Reverse Words in a String III
    Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([word[::-1] for word in s.split(" ")])


def test():
    testcases = [
        ["Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"],
        ["God Ding", "doG gniD"]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.maxJump(testcase[0])
        assert result == testcase[1], 'Testcase #{} failed! Expected: {}. Got: {}'.format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
