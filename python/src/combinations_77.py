"""
Leetcode: https://leetcode.com/problems/combinations/description/
Date: 1-Aug-2023
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        initial = [[item + 1] for item in range(n)]
        result = [[[item + 1], item] for item in range(n)]
        for _ in range(k - 1):
            nr = []
            for item, i in result:
                for j in range(i + 1, n):
                    nr.append([item + initial[j], j])
            result = nr
        return [item[0] for item in result]
