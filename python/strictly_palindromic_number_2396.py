"""
Leetcode: https://leetcode.com/problems/strictly-palindromic-number/
Date: 3-Sep-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_base(b):
            result = ""
            temp_n = n
            while temp_n > 0:
                result += str(temp_n % b)
                temp_n /= b
            return result

        def is_palindrom(num):
            if len(num) == 1:
                return True
            i, j = 0, len(num) - 1
            while i < j:
                if num[i] != num[j]:
                    return False
                i += 1
                j -= 1
            return True

        for i in range(2, n - 1):
            if not is_palindrom(get_base(i)):
                return False
        return True


def test():
    testcases = [
        [9, False],
        [4, False],
        [10, False]
    ]
    solution = Solution()
    for i, testcase in enumerate(testcases):
        assert solution.isStrictlyPalindromic(testcase[0]) == testcase[1], "Testcase #{} failed".format(i)


if __name__ == "__main__":
    test()
