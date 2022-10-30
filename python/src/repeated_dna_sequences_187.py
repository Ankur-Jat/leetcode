"""
Leetcode: https://leetcode.com/problems/repeated-dna-sequences/
Date: 28-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        window_size = 10
        seq_dict = {}
        result = set()
        for i in range(len(s) - window_size + 1):
            word = s[i:i+window_size]
            if word in seq_dict:
                result.add(word)
            seq_dict[word] = True
        return list(result)


def test():
    testcases = [
        ["AAAAAAAAAAA", ["AAAAAAAAAA"]],
        ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"]],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.findRepeatedDnaSequences(
            testcase[0]) == testcase[1], "Testcase #{} failed.".format(index)


if __name__ == "__main__":
    test()
