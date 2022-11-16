"""
Leetcode: https://leetcode.com/problems/guess-number-higher-or-lower/
Date: 16-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""

# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    # Note: no need to write this in leetcode. This is just to pass the testcases
    def __init__(self, num):
        self.num = num

    # Note: no need to write this in leetcode. This is just to pass the testcases
    def guess(self, n):
        if n == self.num:
            return 0
        elif self.num > n:
            return 1
        return -1
        
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start <= end:
            mid = (start+end) // 2
            # Note: in leetcode remove self.
            result = self.guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                end = mid - 1
            else:
                start = mid+1
        return start
        
def test():
    testcases = [
        [10, 100],
        [10001, 1000000]
    ]
    for index, testcase in enumerate(testcases):
        solution = Solution(testcase[0])
        result = solution.guessNumber(testcase[1])
        assert result == testcase[0], "Testcase: {} failed. Expected: {}, Got: {}".format(index, testcase[0], result)

if __name__ == "__main__":
    test()
