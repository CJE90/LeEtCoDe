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
        List<Double> result = new ArrayList<>();
        
        que.offer(root);
        
        while(!que.isEmpty()){
            int n = que.size();
            Double sum = 0.0;
            for(int i = 0; i< n; i++){
                TreeNode cur = que.poll();
                if(cur.left != null){
                    que.offer(cur.left);
                }
                if(cur.right != null){
                    que.offer(cur.right);
                }
                sum+=cur.val;
            }
            result.add(sum/n);
        }
        return result;
        
    }
}