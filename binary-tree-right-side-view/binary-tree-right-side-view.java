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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        Queue<TreeNode> que = new LinkedList<>();
        if(root == null){
            return ans;
        }
        que.add(root);
        
        while(!que.isEmpty()){
            int n = que.size();
            
            for(int i = 0; i<n;i++){
                TreeNode cur = que.poll();
                if(n-i == 1){
                    ans.add(cur.val);
                }
                
                if(cur.left != null){
                    que.add(cur.left);
                }
                if(cur.right != null){
                    que.add(cur.right);
                }
            }
        }
        return ans;
        
    }
}