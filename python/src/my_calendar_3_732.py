"""
Leetcode: https://leetcode.com/problems/my-calendar-iii/
Date: 7-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from sortedcontainers import SortedDict


class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        cur = res = 0
        for delta in self.diff.values():
            cur += delta
            res = max(cur, res)
        return res


def test():
    test_cases = [
        [
            ["MyCalendarThree", "book", "book", "book", "book", "book", "book"],
            [[], [24, 40], [43, 50], [27, 42], [5, 21], [30, 40], [14, 29]],
            [None, 1, 1, 2, 2, 3, 3]
        ]
    ]
    for index, test_case in enumerate(test_cases):
        myCalendar = MyCalendarThree()
        for inner_index, event in enumerate(test_case[1][1:]):
            assert myCalendar.book(event[0], event[1]) == test_case[2][inner_index +
                                                                       1], "Testcase #{} failed with inner index: #{}".format(index, inner_index)


if __name__ == '__main__':
    test()
