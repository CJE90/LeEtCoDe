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
    TreeNode visited;

    public BSTIterator(TreeNode root) {
        stack = new ArrayDeque<>();
        visited = root;
        
    }
    
    public int next() {
        while(visited != null){
            stack.push(visited);
            visited  = visited.left;
        }
        TreeNode curr = stack.pop();
        visited = curr.right;
        return curr.val;
        
    }
    
    public boolean hasNext() {
        if(visited != null || !stack.isEmpty()){
            return true;
        }
        return false;
        
        
    }
    
    }


/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */