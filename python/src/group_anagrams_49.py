"""
Leetcode: https://leetcode.com/problems/group-anagrams/
Date: 28-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        str_dict = {}
        result = []
        for word in strs:
            sort_word = ''.join(sorted(word))
            if sort_word not in str_dict:
                str_dict[sort_word] = len(result)
                result.append([])
            result[str_dict[sort_word]].append(word)
        return result


def test():
    testcases = [
        [["eat", "tea", "tan", "ate", "nat", "bat"], [
            ["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]],
        [[""], [[""]]],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.groupAnagrams(
            testcase[0]) == testcase[1], "Testcase #{} failed.".format(index)


if __name__ == "__main__":
    test()
