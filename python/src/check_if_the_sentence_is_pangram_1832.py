"""
Leetcode: https://leetcode.com/problems/check-if-the-sentence-is-pangram/
Date: 17-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution:
    def checkIfPangram(self, sentence):
        seen = 0
        for curr_char in sentence:
            mapped_index = ord(curr_char) - ord('a')
            curr_bit = 1 << mapped_index
            seen |= curr_bit

        return seen == (1 << 26) - 1


def test():
    solution = Solution()
    testcases = [
        ["thequickbrownfoxjumpsoverthelazydog", True],
        ["leetcode", False]
    ]
    for index, testcase in enumerate(testcases):
        assert solution.checkIfPangram(
            testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
