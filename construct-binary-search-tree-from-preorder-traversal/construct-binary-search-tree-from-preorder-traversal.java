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
    public TreeNode bstFromPreorder(int[] preorder) {
        
        return constructTree(preorder,Integer.MAX_VALUE, new int[]{0});
        
    }
    
    public TreeNode constructTree(int[] preorder, int limit, int[] indexArr){
        if(indexArr[0] == preorder.length || preorder[indexArr[0]] > limit){
            return null;
        }
        
        TreeNode newNode = new TreeNode(preorder[indexArr[0]]);
        indexArr[0] += 1;
        newNode.left = constructTree(preorder, newNode.val, indexArr);
        newNode.right = constructTree(preorder,limit, indexArr);
        return newNode;
        
    }
    
}