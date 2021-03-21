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
    public boolean isUnivalTree(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        helper(res, root);
        int key = res.get(0);
        for(Integer c:res){
            if(c!= key){
                return false;
            }
        }
        return true;
    }
    
    public void helper(List<Integer> res, TreeNode root){
        if(root == null){
            return;
        }
        res.add(root.val);
        helper(res, root.left);
        helper(res, root.right);
    }
}