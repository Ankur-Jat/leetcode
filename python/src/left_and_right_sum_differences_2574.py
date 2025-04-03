from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        numsSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            numsSum -= nums[i]
            result[i] = abs(numsSum - leftSum)
            leftSum += nums[i]
        return result


def test():
    testcases = [
        [[10,4,8,3], [15,1,11,22]],
        [[1], [0]],
        [[1, 2], [1, 1]],
        [[1, 2, 3], [2, 0, 2]],
        [[1, 2, 3, 4], [6, 4, 2, 0]],
        [[1, 2, 3, 4, 5], [10, 8, 6, 4, 0]],
        [[1, -1], [0, 0]],
        [[-1, -2], [0, 0]],
        [[-1, -2, -3], [0, 0, 0]],
        [[-1], [0]],
        [[-1, -2], [1, 1]],
        [[-1, -2, -3], [2, 0, 2]],
        [[-1, -2, -3, -4], [6, 4, 2, 0]],
        [[-1, -2, -3, -4, -5], [10, 8, 6, 4, 0]],
        [[-1, -2], [1, 1]],
        [[-1], [0]],
        [[-1, -2], [1, 1]],
        [[-1, -2], [1, 1]],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.leftRightDifference(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
