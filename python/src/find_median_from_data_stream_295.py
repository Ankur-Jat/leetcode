"""
Leetcode: https://leetcode.com/problems/find-median-from-data-stream/
Date: 12-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
import heapq


class MedianFinder(object):

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.max_heap) == len(self.min_heap):
            num = -1 * (heapq.heappushpop(self.min_heap, num)
                        if self.min_heap else num)
            heapq.heappush(self.max_heap, num)
        else:
            heapq.heappush(self.min_heap, -1 *
                           heapq.heappushpop(self.max_heap, -1 * num))

    def findMedian(self):
        """
        :rtype: float
        """
        return ((-1 * self.max_heap[0] + self.min_heap[0]) / 2.0) if len(self.max_heap) == len(self.min_heap) else -1 * self.max_heap[0]


def test():
    testcases = [
        [["MedianFinder", "addNum", "addNum", "findMedian", "addNum",
            "findMedian"], [[], [1], [2], [], [3], []], [None, None, None, 1.5, None, 2]],
        [["MedianFinder", "addNum", "addNum", "findMedian", "addNum",
            "findMedian"], [[], [3], [1], [], [2], []], [None, None, None, 2, None, 2]]
    ]
    for index, testcase in enumerate(testcases):
        solution = None
        for inner_index, operation in enumerate(testcase[0]):
            if operation == 'MedianFinder':
                solution = MedianFinder()
            elif operation == 'addNum':
                solution.addNum(testcase[1][inner_index][0])
            elif operation == 'findMedian':
                result = solution.findMedian()
                assert result == testcase[2][inner_index], "Testcase: #{} with findMedian: #{} failed! Excepted: {}. Got: {}".format(
                    index, inner_index, testcase[2][inner_index], result)


if __name__ == "__main__":
    test()
