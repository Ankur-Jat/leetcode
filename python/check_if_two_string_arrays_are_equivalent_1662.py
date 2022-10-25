"""
Leetcode: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
Date: 25-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        # return ''.join(word1) == ''.join(word2)
        ptr1 = 0
        char1 = 0
        ptr2 = 0
        char2 = 0
        while ptr1 < len(word1) and ptr2 < len(word2):
            if word1[ptr1][char1] != word2[ptr2][char2]:
                return False
            char1 += 1
            if char1 == len(word1[ptr1]):
                ptr1 += 1
                char1 = 0
            char2 += 1
            if char2 == len(word2[ptr2]):
                char2 = 0
                ptr2 += 1
        return ptr1 == len(word1) and char1 == 0 and ptr2 == len(word2) and char2 == 0


def test():
    testcases = [
        [["abcddefg"], ["abc", "d", "defgh"], False],
        [["a", "cb"], ["ab", "c"], False],
        [["abc", "d", "defg"], ["abcddefg"], True],
        [["ab", "c"], ["a", "bc"], True]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.arrayStringsAreEqual(
            testcase[0], testcase[1]) == testcase[2], "Testcase #{} failed.".format(index)


if __name__ == "__main__":
    test()
