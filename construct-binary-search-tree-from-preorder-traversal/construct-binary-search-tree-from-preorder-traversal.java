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
    int index = 0;
    public TreeNode bstFromPreorder(int[] preorder) {
        return helper(preorder,Integer.MAX_VALUE);
    }
    public TreeNode helper(int[] preorder, int limit){
        if(index>preorder.length-1 || preorder[index] > limit){
            return null;
        }
        TreeNode newNode = new TreeNode(preorder[index]);
        index++;
        newNode.left = helper(preorder,newNode.val);
        newNode.right = helper(preorder,limit);
        return newNode;
    }
}