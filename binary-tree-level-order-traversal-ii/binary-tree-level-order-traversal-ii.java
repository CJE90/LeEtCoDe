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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        Queue<TreeNode> que = new LinkedList<>();
        List<List<Integer>> result = new ArrayList<>();
        if(root == null){
            return result;
        }
        que.offer(root);
        while(!que.isEmpty()){
            int n = que.size();
            List<Integer> levelList = new ArrayList<>();
            for(int i = 0; i< n; i++){
                TreeNode cur = que.poll();
                if(cur.left != null){
                    que.add(cur.left);
                }
                if(cur.right != null){
                    que.add(cur.right);
                }
                levelList.add(cur.val);
            }
            //Collections.reverse(levelList);
            result.add(levelList);
        }
        Collections.reverse(result);
        return result;
        
        
    }
}