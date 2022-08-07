"""
Leetcode: https://leetcode.com/problems/merge-similar-items
Date: 7-Aug-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        items1.sort(key=lambda x: x[0])
        items2.sort(key=lambda x: x[0])
        result = []
        items1_index = 0
        items2_index = 0
        
        while items1_index < len(items1) or items2_index < len(items2):
            item1 = items1[items1_index] if items1_index < len(items1) else [float('inf'), float('inf')]
            item2 = items2[items2_index] if items2_index < len(items2) else [float('inf'), float('inf')]
            if item1[0] < item2[0]:
                result.append(item1)
                items1_index += 1
            elif item1[0] > item2[0]:
                result.append(item2)
                items2_index += 1
            else:
                result.append([item1[0], item1[1] + item2[1]])
                items1_index += 1
                items2_index += 1
        return result


def test():
    solution = Solution()
    test_cases = [
        [ [[1,1],[4,5],[3,8]], [[3,1],[1,5]], [[1,6],[3,9],[4,5]] ],
        [ [[1,1],[3,2],[2,3]], [[2,1],[3,2],[1,3]], [[1,4],[2,4],[3,4]] ],
        [ [[1,3],[2,2]], [[7,1],[2,2],[1,4]], [[1,7],[2,4],[7,1]]]
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.mergeSimilarItems(test_case[0], test_case[1]) == test_case[2], 'test case number {} is failing'.format(index)

if __name__ == '__main__':
    test()
