
/**
 * Leetcode: https://leetcode.com/problems/3sum-closest/
 * Date: 8-Oct-2022
 * Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
 */
import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public boolean findTarget(TreeNode root, int k) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        Map<Integer, Boolean> sumMap = new HashMap<>();
        while (queue.size() > 0) {
            TreeNode node = queue.remove();
            if (sumMap.get(node.val) != null)
                return true;
            sumMap.put(k - node.val, true);
            if (node.left != null)
                queue.add(node.left);
            if (node.right != null)
                queue.add(node.right);
        }
        return false;
    }
}

public class TwoSumIvInputIsABST653 {
    public static void main(String[] args) throws Exception {
        TreeNode root = new TreeNode(8);
        root.left = new TreeNode(4);
        root.right = new TreeNode(12);
        root.left.left = new TreeNode(2);
        root.right.left = new TreeNode(10);
        root.right.right = new TreeNode(16);
        root.right.right.left = new TreeNode(14);

        Solution solution = new Solution();
        if (solution.findTarget(root, 26) != true)
            throw new Exception("first test case failed");
        if (solution.findTarget(root, 30) != true)
            throw new Exception("second test case failed");
        if (solution.findTarget(root, 100) != false)
            throw new Exception("third test case failed");
    }
}
