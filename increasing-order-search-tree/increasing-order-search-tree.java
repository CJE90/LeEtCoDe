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
    public TreeNode increasingBST(TreeNode root) {
        List<Integer> vals = new ArrayList<>();
        inOrder(root,vals);
        TreeNode ans = new TreeNode(0);
        TreeNode current = ans;
        for(Integer i:vals){
            current.right = new TreeNode(i);
            current = current.right;
            
        }
        return ans.right;
    }
    
    public void inOrder(TreeNode root, List<Integer> vals){
        if(root == null){
            return;
        }
        inOrder(root.left, vals);
        vals.add(root.val);
        inOrder(root.right,vals);
    }
}