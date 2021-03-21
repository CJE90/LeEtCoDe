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
    public List<Integer> getLonelyNodes(TreeNode root) {
        List<Integer> myList = new ArrayList<>();
        getLonelyNodesHelper(myList, root);
        return myList;
        
    }
    
    public void getLonelyNodesHelper(List<Integer> l, TreeNode root){
        if(root == null){
            return;
        }
        
        if(root.left == null && root.right != null){
            l.add(root.right.val);
        }
       if(root.right == null && root.left != null){
        l.add(root.left.val);
        }
    
    getLonelyNodesHelper(l,root.left);
    getLonelyNodesHelper(l,root.right);
    }
}