from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root:
                return 0, None

            left = dfs(root.left)
            right = dfs(root.right)

            if left[0] > right[0]:
                return left[0] + 1, left[1]
            if left[0] < right[0]:
                return right[0] + 1, right[1]
            return left[0] + 1, root

        return dfs(root)[1]
    

def test():
    testcases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, None, 4, None, 5],
        [1],
        [1, None, 2],
        [1, 2]
    ]
    expected = [
        [2],
        [2],
        [1],
        [1],
        [1]
    ]
    for i, (tc, expec) in enumerate(zip(testcases, expected)):
        root = TreeNode(tc[0])
        nodes = [root]
        for val in tc[1:]:
            if val is not None:
                node = TreeNode(val)
                if not nodes[0].left:
                    nodes[0].left = node
                else:
                    nodes[0].right = node
                    nodes.pop(0)
                nodes.append(node)
            else:
                if nodes[0].left and not nodes[0].right:
                    nodes.pop(0)
        assert Solution().lcaDeepestLeaves(root).val == expec[0], f"Test case {i + 1} failed"
    print("All test cases passed!")


if __name__ == "__main__":  
    test()
