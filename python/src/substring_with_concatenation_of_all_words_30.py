"""
Leetcode: https://leetcode.com/problems/substring-with-concatenation-of-all-words/
Date: 13-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_dict = {}
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1

        word_len = len(words[0])
        words_len = len(words) * word_len
        s_len = len(s)
        
        if s_len < words_len:
            return []
        result = []
        for i in range(s_len - words_len + 1):
            sub_str = s[i: i+words_len]
            j = 0
            curr_dict = {}
            while j < words_len:
                curr_word = sub_str[j:j+word_len]
                if curr_word not in words_dict:
                    break
                curr_dict[curr_word] = curr_dict.get(curr_word, 0) + 1
                j += word_len
            if words_dict == curr_dict:
                result.append(i)
        return result


def test():
    solution = Solution()
    test_cases = [
        [ "barfoothefoobarman", ["foo", "bar"], [0, 9] ],
        [ "aaa", ["a", "a"], [0, 1]]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.findSubstring(test_case[0], test_case[1]) == test_case[2], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
