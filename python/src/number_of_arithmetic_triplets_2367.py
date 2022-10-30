"""
Leetcode: https://leetcode.com/problems/number-of-arithmetic-triplets/
Date: 7-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count = 0
        for j in range(1, len(nums) - 1):
            i = j - 1
            k = j + 1
            while i >= 0 and k < len(nums):
                idiff = nums[j] - nums[i]
                kdiff = nums[k] - nums[j]
                if idiff == kdiff and kdiff == diff:
                    count += 1
                    break
                if idiff != diff:
                    i -= 1
                if kdiff != diff:
                    k += 1
        return count


def test():
    solution = Solution()
    test_cases = [
        [ [0,1,4,6,7,10], 3, 2 ],
        [ [4,5,6,7,8,9], 2, 2 ]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.arithmeticTriplets(test_case[0], test_case[1]) == test_case[2], 'test case number {} is failing'.format(index)

if __name__ == '__main__':
    test()