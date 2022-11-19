"""
Leetcode: https://leetcode.com/problems/erect-the-fence/
Date: 19-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def outerTrees(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(trees) <= 1:
            return trees

        def is_orientation_anti_clockwise(p1, p2, p3):
            return ((p2[1] - p1[1]) * (p3[0] - p2[0]) - (p3[1] - p2[1]) * (p2[0] - p1[0])) >= 0

        trees.sort(key=lambda x: (x[0], x[1]))
        lower_convex_hull = []
        for tree in trees:
            while len(lower_convex_hull) >= 2 and not is_orientation_anti_clockwise(lower_convex_hull[-2], lower_convex_hull[-1], tree):
                lower_convex_hull.pop()
            lower_convex_hull.append(tuple(tree))

        upper_convex_hull = []
        for tree in trees[::-1]:
            while len(upper_convex_hull) >= 2 and not is_orientation_anti_clockwise(upper_convex_hull[-2], upper_convex_hull[-1], tree):
                upper_convex_hull.pop()
            upper_convex_hull.append(tuple(tree))

        return list(set(upper_convex_hull[:-1] + lower_convex_hull[:-1]))


def test():
    testcases = [
        [[[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
            [(2, 4), (1, 1), (2, 0), (4, 2), (3, 3)]],
        [[[1, 2], [2, 2], [4, 2]], [(1, 2), (4, 2), (2, 2)]]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.outerTrees(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
