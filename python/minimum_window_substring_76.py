"""
Leetcode: https://leetcode.com/problems/minimum-window-substring/
Date: 22-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tlen = len(t)
        slen = len(s)
        if slen < tlen:
            return ''

        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        window_dict = {}
        l, r, find, required = 0, 0, 0, len(t_dict)
        ans = float('inf'), None, None
        while r < slen:
            char = s[r]
            window_dict[char] = window_dict.get(char, 0) + 1
            if char in t_dict and window_dict[char] == t_dict[char]:
                find += 1
            if find == required:
                # Reduce window
                while l <= r and find == required:
                    if ans[0] > (r - l + 1):
                        ans = r - l + 1, l, r
                    char = s[l]
                    window_dict[char] -= 1
                    if char in t_dict and window_dict[char] < t_dict[char]:
                        find -= 1
                    l += 1
            r += 1
        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+1]


"a"
"a"
"a"
"aa"
"aaaaaaaaaaab"
"aaaaab"


def test():
    solution = Solution()
    test_cases = [
        ["ADOBECODEBANC", "ABC", "BANC"],
        ["aa", "a", "a"],
        ["a", "aa", ''],
        ["aaaaaaaaaaa", "aaaaab", ''],
        ["acaaaaaabaab", "aaaaab", "aaaaab"]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.minWindow(
            test_case[0], test_case[1]) == test_case[2], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
