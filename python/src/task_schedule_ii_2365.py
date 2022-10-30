"""
Leetcode: https://leetcode.com/problems/task-scheduler-ii/
Date: 7-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def taskSchedulerII(self, tasks, space):
        """
        :type tasks: List[int]
        :type space: int
        :rtype: int
        """
        break_dict = {}
        days_count = 0
        for task_id in tasks:
            if task_id not in break_dict or break_dict[task_id] < days_count:
                days_count += 1
            else:
                days_count = break_dict[task_id] + 1
            break_dict[task_id] = days_count + space
        return days_count


def test():
    solution = Solution()
    test_cases = [
        [ [1,2,1,2,3,1], 3, 9 ],
        [ [5,8,8,5], 2, 6 ]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.taskSchedulerII(test_case[0], test_case[1]) == test_case[2], 'test case number {} is failing'.format(index)

if __name__ == '__main__':
    test()