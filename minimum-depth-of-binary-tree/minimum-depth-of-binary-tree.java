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
    public int minDepth(TreeNode root) {
        if(root == null){
            return 0;
        }
        Queue<TreeNode> que = new LinkedList<>();
        int level = 1;
        
        que.add(root);
        while(que.size() != 0){
            int n = que.size();
            for(int i = 0; i<n; i++){
                TreeNode cur = que.poll();
                if(cur.left == null && cur.right == null){
                return level;
             }
                if(cur.left != null){
                que.add(cur.left);
                }
                if(cur.right != null){
                 que.add(cur.right);
                }
            }
            level++;
            
        }
        return 0;
    }
}