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
    public List<Double> averageOfLevels(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        List<Double> ans = new ArrayList<>();
        
        que.add(root);
        
        while(que.size() != 0){
            Double runSum = 0.0;
            int n = que.size();
            for(int i = 0; i<n; i++){
                TreeNode temp = que.poll();
                if(temp.left != null){
                    que.add(temp.left);
                }
                if(temp.right != null){
                    que.add(temp.right);
                }
                runSum+=temp.val;
            }
            ans.add(runSum/n);
            runSum = 0.0;
        }
        return ans;
        
    }
}