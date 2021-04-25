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
    public boolean isCousins(TreeNode root, int x, int y) {
        if(root == null){
            return false;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            boolean doesXExist = false;
            boolean doesYExist = false;
            for(int i = 0; i< size; i++){
                TreeNode currentNode = queue.remove();
                if(currentNode.val == x){
                    doesXExist = true;
                }
                if(currentNode.val == y){
                    doesYExist = true;
                }
                
                if(currentNode.left != null && currentNode.right != null){
                    if(currentNode.left.val == x && currentNode.right.val == y){
                        return false;
                    }
                    if(currentNode.left.val == y && currentNode.right.val == x){
                        return false;
                    }
                }
                
                if(currentNode.left != null){
                    queue.add(currentNode.left);
                }
                if(currentNode.right != null){
                    queue.add(currentNode.right);
                }
                
            }
            if(doesXExist && doesYExist){
                return true;
            }
        }
        return false;
        
    }
}


