"""
Leetcode: https://leetcode.com/problems/online-stock-span/
Date: 9-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        counter = 1
        while self.stack and self.stack[-1][0] <= price:
            counter += self.stack.pop()[1]
        self.stack.append((price, counter))
        return counter


def test():
    testcases = [
        [
            ["StockSpanner", "next", "next", "next",
                "next", "next", "next", "next"],
            [[], [100], [80], [60], [70], [60], [75], [85]],
            [None, 1, 1, 1, 2, 1, 4, 6]
        ]
    ]
    
    for index, testcase in enumerate(testcases):
        solution = StockSpanner()
        for day, price in enumerate(testcase[1][1:]):
            price = price[0]
            result = solution.next(price)
            day = day + 1
            assert result == testcase[2][day], "Testcase #{} failed on day #{}. Expected: {}, Actual: {}".format(
                index, day+1, testcase[2][day], result)


if __name__ == "__main__":
    test()
