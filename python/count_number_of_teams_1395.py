"""
Leetcode: https://leetcode.com/problems/count-number-of-teams/
Date: 11-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(rating)):
            llc = lgc = rlc = rgc = 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    llc += 1
                elif rating[j] > rating[i]:
                    lgc += 1
            for j in range(i+1, len(rating)):
                if rating[j] < rating[i]:
                    rlc += 1
                elif rating[j] > rating[i]:
                    rgc += 1                    
            count += llc * rgc + lgc * rlc
        return count


def test():
    solution = Solution()
    test_cases = [
        [ [2,5,3,4,1], 3 ],
        [ [2,1,3], 0 ],
        [ [1,2,3,4], 4 ]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.numTeams(test_case[0]) == test_case[1], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
