"""
Leetcode: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
Date: 3-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        min_cost = 0
        prev_color = s[0]
        prev_cost = cost[0]
        for i in range(1, len(s)):
            if s[i] == prev_color:
                min_cost += min(prev_cost, cost[i])
                prev_cost = max(prev_cost, cost[i])
            else:
                prev_cost = cost[i]
                prev_color = s[i]
        return min_cost


def test():
    solution = Solution()
    test_cases = [
        [ "abaac", [1,2,3,4,5], 3, ],
        [ "abc", [1,2,3], 0, ],
        [ "aabaa", [1,2,3,4,1], 2, ],
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.minCost(test_case[0], test_case[1]) == test_case[2], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
