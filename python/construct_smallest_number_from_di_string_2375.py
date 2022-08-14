"""
Leetcode: https://leetcode.com/problems/construct-smallest-number-from-di-string/
Date: 14-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        num = [1, 2] if pattern[0] == 'I' else [2, 1]
        next_num = 3
        for index in range(1, len(pattern)):
            char = pattern[index]
            if char == 'I':
                num.append(next_num)
            elif char == 'D':
                backup = num[-1]
                temp_index = index
                while temp_index >= 0 and pattern[temp_index] == 'D':
                    num[temp_index] += 1
                    temp_index -= 1
                num.append(backup)
            next_num += 1
        return ''.join([str(i) for i in num])


def test():
    testcases = [
        ["IIIDIDDD", "123549876"],
        ["DDD", "4321"]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.smallestNumber(testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
