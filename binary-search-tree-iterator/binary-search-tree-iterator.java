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
class BSTIterator {
    Deque<TreeNode> stack;

    public BSTIterator(TreeNode root) {
        stack = new ArrayDeque<>();
        fillStack(root);
        
    }
    
    public int next() {
        TreeNode curNode = stack.pop();
        if(curNode.right != null){
            fillStack(curNode.right);
        }
        return curNode.val;
        
    }
    
    public boolean hasNext() {
        if(!stack.isEmpty()){
            return true;
        }
        return false;
        
        
    }
    public void fillStack(TreeNode root){
        while(root!= null){
            stack.push(root);
            root = root.left;
        }
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */