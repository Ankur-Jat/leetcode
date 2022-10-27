"""
Leetcode: https://leetcode.com/problems/sliding-window-maximum/
Date: 27-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or not k:
            return []
        if k > len(nums):
            k = len(nums)
        window = deque()
        result = []
        counter = 0
        while counter < k:
            while window and nums[counter] > nums[window[-1]]:
                window.pop()
            window.append(counter)
            counter += 1
        result.append(nums[window[0]])
        for i in range(k, len(nums)):
            while window and nums[i] > nums[window[-1]]:
                window.pop()
            window.append(i)
            while window and window[0] == (i - k):
                window.popleft()
            result.append(nums[window[0]])
        return result


def test():
    testcases = [
        [[1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]],
        [[1], 1, [1]],
        [[1, 2, 3, 4, 5, 6, 4, 3, 2, 5, 1], 11, [6]],
        [[1, 2, 3, 4, 5, 6, 4, 3, 2, 5, 1], 4, [4, 5, 6, 6, 6, 6, 5, 5]]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.maxSlidingWindow(
            testcase[0], testcase[1]) == testcase[2], "Testcase #{} failed.".format(index)


if __name__ == "__main__":
    test()
