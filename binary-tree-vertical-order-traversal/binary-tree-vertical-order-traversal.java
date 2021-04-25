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
    public List<List<Integer>> verticalOrder(TreeNode root) {
        Map<Integer,List<Integer>> colToVal = new TreeMap<>();
        Map<Integer,Integer> valToCol = new TreeMap<>();
        List<List<Integer>> answer = new ArrayList<>();
        if(root == null){
            return answer;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        valToCol.put(root.val,0);
        //colToVal.put(0,root.val);
        if(colToVal.get(0) == null){
            colToVal.put(0, new ArrayList<Integer>());
            colToVal.get(0).add(root.val);
        }
        else{
            colToVal.get(0).add(root.val);
        }
        
        while(!queue.isEmpty()){
            int size = queue.size();
            
            for(int i = 0; i < size; i++){
                TreeNode currentNode = queue.remove();
                int currentColumn = valToCol.get(currentNode.val);
                 if(currentNode.left != null){
                     queue.add(currentNode.left);
                     valToCol.put(currentNode.left.val, currentColumn-1);
                     if(colToVal.get(currentColumn-1) == null){
                         colToVal.put(currentColumn-1, new ArrayList<Integer>());
                         colToVal.get(currentColumn-1).add(currentNode.left.val);
                     }
                     else{
                         colToVal.get(currentColumn-1).add(currentNode.left.val);
                     }
                 }
                if(currentNode.right != null){
                    queue.add(currentNode.right);
                     valToCol.put(currentNode.right.val, currentColumn+1);
                    if(colToVal.get(currentColumn+1) == null){
                         colToVal.put(currentColumn+1, new ArrayList<Integer>());
                         colToVal.get(currentColumn+1).add(currentNode.right.val);
                     }
                     else{
                         colToVal.get(currentColumn+1).add(currentNode.right.val);
                     }
                }
                 
            }
        }
        for(Integer key:colToVal.keySet()){
            answer.add(colToVal.get(key));
        }
        return answer;
    }
}