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
    public boolean findTarget(TreeNode root, int k) {
        Set<Integer> hs = new HashSet<>();
        return dfs(root, hs, k);
        
    }
    public boolean dfs(TreeNode root, Set<Integer> hs, int k){
        if(root == null){
            return false;
        }
        if(hs.contains(k-root.val)){
            return true;
        }
        hs.add(root.val);
        return dfs(root.left, hs, k) || dfs(root.right, hs, k);
    }
}