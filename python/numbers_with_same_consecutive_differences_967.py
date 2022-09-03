"""
Leetcode: https://leetcode.com/problems/numbers-with-same-consecutive-differences/
Date: 3-Sep-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import defaultdict

class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        def generate_number(num_array=None):
            result = []
            pre_result = defaultdict(list)
            if not num_array:
                num_array = list(range(1, 10))
            new_num_array = set()
            for num in num_array:
                new_num_array.add(num % 10)
                pre_result[num % 10].append(num)
            iter_array = list(new_num_array)

            for num in iter_array:
                abs_next = num + k
                if abs_next >= 0 and abs_next <= 9:
                    for temp_num in pre_result[num]:
                        result.append(int(str(temp_num) + str(abs_next)))
                abs_prev = num - k
                if abs_prev >= 0 and abs_prev <= 9:
                    for temp_num in pre_result[num]:
                        result.append(int(str(temp_num) + str(abs_prev)))
            return list(set(result))
        
        answer = generate_number()
        n -= 1
        while n > 1:
            answer = generate_number(answer)
            n -= 1
        return answer


def test():
    testcases = [
        [2, 1, [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]],
        [3, 7, [181,292,707,818,929]],
        [2, 0, [11,22,33,44,55,66,77,88,99]],
        [9, 9, [909090909]]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        answer = solution.numsSameConsecDiff(testcase[0], testcase[1])
        answer.sort()
        assert answer == testcase[2], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()