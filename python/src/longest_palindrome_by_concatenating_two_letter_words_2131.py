"""
Leetcode: https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
Date: 3-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


from collections import Counter
class Solution:
    def longestPalindrome(self, words):
        # a count variable contains the number of occurrences of each word
        count = Counter(words)
        answer = 0
        central = False
        for word, count_of_the_word in count.items():
            # if the word is a palindrome
            if word[0] == word[1]:
                if count_of_the_word % 2 == 0:
                    answer += count_of_the_word
                else:
                    answer += count_of_the_word - 1
                    central = True
            # consider a pair of non-palindrome words,
            # such that one is the reverse of another
            # word[1] + word[0] is the reversed word
            elif word[0] < word[1]:
                answer += 2 * min(count_of_the_word, count[word[1] + word[0]])
        if central:
            answer += 1
        return 2 * answer


def test():
    testcases = [
        [["lc", "cl", "gg"], 6],
        [["ab", "ty", "yt", "lc", "cl", "ab"], 8],
        [["cc", "ll", "xx"], 2],
        [["cc", "cc", "cc", "cc", "cc", "aa", "aa", "aa", "ab", "ba"], 18],
        [["cc", "cc", "cc", "cc", "cc", "aa", "aa",
            "aa", "ab", "ba", "dd", "ee", "ee"], 22],
        [["wy", "wy", "nn", "ww", "yy", "nw", "nn", "yw", "ww", "yw", "yy", "nn", "yw", "ny", "nn", "yy", "yy", "nw", "yy", "ww", "wy", "wy", "wn", "wn", "ny", "ny", "yn", "ww", "wn", "yn", "yn", "wy", "nw", "wn", "yn", "wn", "nn", "yw", "wy", "ww", "wy", "wy", "yw", "nn", "nw",
            "nn", "yy", "ww", "yn", "yw", "yw", "yn", "yw", "nw", "yn", "yn", "yy", "wn", "wn", "nw", "yn", "nw", "yw", "nw", "nw", "nn", "ww", "nw", "nw", "wn", "wn", "nw", "nn", "nw", "wy", "nn", "yy", "ww", "yn", "nw", "wn", "yn", "yn", "nw", "yy", "nn", "wy", "nn", "wn"], 150],
        [["rj", "xx", "ee", "jj", "rj", "uu", "ee", "ww", "oo", "ll", "oo", "ii", "xx", "hh", "ll", "hh", "pp", "hh", "ii", "ll", "ii", "gg", "nn", "nn", "cc", "dd", "ww",
            "aa", "tt", "rr", "ff", "gg", "gg", "oo", "kk", "rj", "xx", "rr", "qq", "tt", "ww", "vv", "vv", "oo", "nn", "yy", "hh", "ll", "vv", "ss", "jr", "mm", "aa", "rj"], 70]

    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.longestPalindrome(testcase[0])
        assert result == testcase[1], "Testcase #{} failed.\nExpected: {}\nReceived: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
