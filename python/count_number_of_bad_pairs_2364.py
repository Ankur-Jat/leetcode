"""
Leetcode: https://leetcode.com/problems/count-number-of-bad-pairs/
Date: 7-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        total_pairs = (n * (n-1)) / 2
        two_sum_dict = {}
        good_pairs_count = 0
        for i in range(n):
            if (i - nums[i]) in two_sum_dict:
                good_pairs_count += two_sum_dict[i - nums[i]]
            two_sum_dict[i - nums[i]] = two_sum_dict.get( i - nums[i], 0) + 1
        return total_pairs - good_pairs_count


def test():
    solution = Solution()
    test_cases = [
        [ [4,1,3,3], 5 ],
        [ [1,2,3,4,5], 0 ]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.countBadPairs(test_case[0]) == test_case[1], 'test case number {} is failing'.format(index)

if __name__ == '__main__':
    test()