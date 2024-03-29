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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if(root == null){
            return false;
        }
        if(root.val == targetSum && root.right == null && root.left == null){
            return true;
        }
        int newTarget = targetSum-root.val;
        boolean leftHasPathSum = hasPathSum(root.left, newTarget);
        boolean rightHasPathSum = hasPathSum(root.right, newTarget);
        return leftHasPathSum || rightHasPathSum;
    }
}