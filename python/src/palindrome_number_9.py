"""
Leetcode: https://leetcode.com/problems/palindrome-number/
Date: 9-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        queue = []
        while x:
            r = x % 10
            x /= 10
            queue.append(r)
        i, j = 0, len(queue) - 1
        while i < j:
            if queue[i] != queue[j]:
                return False
            i += 1
            j -= 1
        return True


def test():
    testcases = [
        [9, True],
        [0, True],
        [-121, False],
        [121, True],
        [123, False]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.isPalindrome(
            testcase[0]) == testcase[1], "Testcase {} is failing".format(index)


if __name__ == "__main__":
    test()
