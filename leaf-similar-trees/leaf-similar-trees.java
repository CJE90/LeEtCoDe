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
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        ArrayList<Integer> daList = new ArrayList<Integer>();
        ArrayList<Integer> daList2 = new ArrayList<Integer>();
        dfs(root1, daList);
        dfs(root2, daList2);
        if(!daList.equals(daList2)){
            return false;
        }
        
        
        return true;
        
        
    }
    
    public void dfs(TreeNode node, ArrayList<Integer> daList){
        if(node == null){
            return;
        }
        if(node.left == null && node.right == null){
                daList.add(node.val);
            }
            dfs(node.left, daList);
            dfs(node.right, daList);
    }
}