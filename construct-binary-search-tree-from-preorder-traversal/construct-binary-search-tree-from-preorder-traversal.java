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
        if(preorder == null || preorder.length == 0){
            return null;
        }
        int preorder_root = preorder[0];
        List<Integer> lower = new ArrayList<>();
        List<Integer> upper = new ArrayList<>();
        for(int i = 1; i<preorder.length;i++){
            if(preorder[i]<preorder_root){
                lower.add(preorder[i]);
            }
            else{
                upper.add(preorder[i]);
            }
        }
        
        int[] lowerFixed = lower.stream().mapToInt(i->i).toArray();
        int[] upperFixed = upper.stream().mapToInt(i->i).toArray();
        
        TreeNode root = new TreeNode(preorder_root);
        root.left = bstFromPreorder(lowerFixed);
        root.right = bstFromPreorder(upperFixed);
        return root;
    }
}