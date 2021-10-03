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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        List<List<Integer>> result = new ArrayList<>();
        if(root == null){
            return result;
        }
        
        int level = 0;
        
        que.offer(root);
        
        while(!que.isEmpty()){
            int n = que.size();
            List<Integer> levelList = new ArrayList<>();
            for(int i = 0; i<n;i++){
                TreeNode current = que.poll();
                if(current.left != null){
                    que.add(current.left);
                }
                if(current.right != null){
                    que.add(current.right);
                }
                levelList.add(current.val);
            }
            if(level%2 != 0){
                Collections.reverse(levelList);
            }
            result.add(levelList);
            level++;
        }
        return result;
        
    }
}