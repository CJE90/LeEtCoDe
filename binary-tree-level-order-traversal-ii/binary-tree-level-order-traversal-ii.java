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
        List<List<Integer>> result = new ArrayList<>();
        if(root == null){
            return result;
        }
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            List<Integer> currentLevel = new ArrayList<>();
            
            for(int i = 0 ; i < size; i++){
                TreeNode currentNode = queue.remove();
                currentLevel.add(currentNode.val);
                if(currentNode.left != null){
                    queue.add(currentNode.left);
                }
                if(currentNode.right != null){
                    queue.add(currentNode.right);
                }
            }
            result.add(currentLevel);
        }
        int size = result.size();
        List<List<Integer>> finalResult = new ArrayList<>();
        for(int i = size-1; i >=0; i--){
            finalResult.add(result.get(i));
        }
        return finalResult;
    }
}