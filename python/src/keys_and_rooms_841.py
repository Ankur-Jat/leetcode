"""
Leetcode: https://leetcode.com/problems/keys-and-rooms/
Date: 21-Dec-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution:
    def canVisitAllRooms(self, rooms):
        added = set()
        n = len(rooms)
        stack = [rooms[0]]
        added.add(0)
        while stack:
            keys = stack.pop()
            for key in keys:
                if key not in added:
                    added.add(key)
                    stack.append(rooms[key])
            if len(added) == n:
                return True
        return len(added) == n


def test():
    testcases = [
        [[[1], [2], [3], []], True],
        [[[1, 3], [3, 0, 1], [2], [0]], False],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.canVisitAllRooms(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}. Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
