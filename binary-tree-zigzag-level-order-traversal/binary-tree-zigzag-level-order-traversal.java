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
        List<List<Integer>> answer = new ArrayList<>();
        boolean useLeft = false;
        if(root == null){
            return answer;
        }
        
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while(!queue.isEmpty()){
            List<Integer> currentLevel = new ArrayList<>();
            int size = queue.size();
            
            for(int i = 0; i<size;i++){
                TreeNode currentNode = queue.remove();
                if(useLeft){
                    currentLevel.add(0,currentNode.val);
                }
                else{
                    currentLevel.add(currentNode.val);
                }
                if(currentNode.left != null){
                    queue.add(currentNode.left);
                }
                if(currentNode.right != null){
                    queue.add(currentNode.right);
                }
            }
            useLeft = !useLeft;
            
            answer.add(currentLevel);
            
        }
        return answer;
    }
}