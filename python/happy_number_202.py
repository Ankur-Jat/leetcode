"""
Leetcode: https://leetcode.com/problems/happy-number/
Date: 4-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def isHappyOld(self, n):
        """
        :type n: int
        :rtype: bool
        Exxtra memory
        """
        numbersInCycle = {}
        numbersInCycle[n] = True
        while True:
            newNumber = sum([int(number)*int(number) for number in str(n)])
            if newNumber == 1:
                return True
            if numbersInCycle.get(newNumber):
                return False
            else:
                numbersInCycle[newNumber] = True
            n = newNumber

    def numSquareSum(self, n):
        return sum([int(number)*int(number) for number in str(n)])

    def isHappy(self, n):

        # initialize slow
        # and fast by n
        slow = n
        fast = n
        while(True):

            # move slow number
            # by one iteration
            slow = self.numSquareSum(slow)

            # move fast number
            # by two iteration
            fast = self.numSquareSum(self.numSquareSum(fast))
            if(slow != fast):
                continue
            else:
                break

        # if both number meet at 1,
        # then return true
        return (slow == 1)


def test():
    testcases = [
        [19, True, ],
        [2, False, ],
        [1091, False, ],
    ]

    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.isHappy(
            testcase[0]) == testcase[1], " Testcase #{} failed in isHappy".format(index)
        assert solution.isHappyOld(
            testcase[0]) == testcase[1], " Testcase #{} failed in isHappyOld".format(index)


if __name__ == "__main__":
    test()
