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
    int diameter = 0;
    public int diameterOfBinaryTree(TreeNode root) {
        
        
        
        dfs(root);
        return diameter;
        
    }
    public int dfs(TreeNode root){
            if(root == null){
                return -1;
            }
            int left = dfs(root.left);
            int right = dfs(root.right);
            diameter = Math.max(diameter, right+left +2);
            return 1+Math.max(left, right);
        }
}