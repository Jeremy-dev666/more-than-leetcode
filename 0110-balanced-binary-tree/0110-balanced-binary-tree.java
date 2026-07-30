/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    boolean result = true;
    public boolean isBalanced(TreeNode root) {
        maxDepth(root);
        return result;
    }
    int maxDepth(TreeNode node) {
        // base case
        if(node == null) return 0;

        int leftMaxDepth = maxDepth(node.left);
        int rightMaxDepth = maxDepth(node.right);

        // 后序遍历操作位置，继续传递参数
        if(Math.abs(leftMaxDepth - rightMaxDepth) > 1) {
            result = false;
        }
        return 1 + Math.max(leftMaxDepth, rightMaxDepth);
    }
}