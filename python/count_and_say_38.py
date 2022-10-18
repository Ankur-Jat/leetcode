"""
Leetcode: https://leetcode.com/problems/count-and-say/
Date: 18-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        result = "1"
        counter = 1
        while counter < n:
            tempResult = ""
            count = 1
            for index in range(1, len(result)):
                if result[index] == result[index-1]:
                    count += 1
                else:
                    tempResult += str(count) + result[index-1]
                    count = 1
            tempResult += str(count) + result[-1]
            result = tempResult
            counter += 1
        return result


def test():
    solution = Solution()
    testcases = [
        [1, "1"],
        [2, '11'],
        [3, '21'],
        [4, '1211'],
        [5, '111221']
    ]
    for index, testcase in enumerate(testcases):
        assert solution.countAndSay(
            testcase[0]) == testcase[1], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
