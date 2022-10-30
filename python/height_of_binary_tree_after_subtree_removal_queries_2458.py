"""
Leetcode: https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
Date: 30-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import defaultdict


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        node_dict = defaultdict(dict)
        level_dict = defaultdict(list)

        def dfs(node, depth):
            if not node:
                return 0
            node_dict[node.val]["depth"] = depth
            node_dict[node.val]["height"] = max(
                dfs(node.left, depth+1),
                dfs(node.right, depth+1)
            )
            return 1 + node_dict[node.val]["height"]
        dfs(root, 0)
        cousin_dict = defaultdict(list)
        for node in node_dict.keys():
            depth = node_dict[node]["depth"]
            score = depth + node_dict[node]["height"]
            cousin_dict[depth].append((node, score))
            cousin_dict[depth].sort(key=lambda x: x[1], reverse=True)
            cousin_dict[depth] = cousin_dict[depth][:2]

        result = []
        # print("node_dict", node_dict)
        # print("cousin_list", cousin_dict)
        for query in queries:
            depth = node_dict[query]["depth"]
            cousin_list = cousin_dict[depth]
            if query == cousin_list[0][0]:
                if len(cousin_list) > 1:
                    result.append(cousin_list[1][1])
                else:
                    result.append(depth-1)
            else:
                result.append(cousin_list[0][1])
            # print('query', query, 'depth', depth, 'cousin_list', cousin_list, 'value', result[-1])
        return result


def test():
    testcases = []
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(2)
    root1.right.left = TreeNode(6)
    root1.right.right = TreeNode(5)
    root1.right.right.right = TreeNode(7)
    testcases.append((root1, [4], [2]))

    root2 = TreeNode(5)
    root2.left = TreeNode(8)
    root2.right = TreeNode(9)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(1)
    root2.left.left.left = TreeNode(4)
    root2.left.left.right = TreeNode(6)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(7)
    testcases.append((root2, [3, 2, 4, 8], [3, 2, 3, 2]))

    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.treeQueries(
            testcase[0], testcase[1]) == testcase[2], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
