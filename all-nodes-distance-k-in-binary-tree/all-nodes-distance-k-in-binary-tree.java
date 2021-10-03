/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        List<Integer> result  =  new ArrayList<>();
        Queue<TreeNode> que = new LinkedList<>();
        Map<TreeNode,TreeNode> nodeToParent = new HashMap<>();
        Set<TreeNode> seen = new HashSet<>();
        int level = 0;
        
        connectNodeToParent(nodeToParent, root, null);
        
        que.add(target);
        while(!que.isEmpty()){
            int n = que.size();
            if(level == k){
                for(TreeNode t:que){
                    result.add(t.val);
                }
                return result;
            }
            for(int i = 0; i< n; i++){
                TreeNode current = que.poll();
                if(current.left != null && !seen.contains(current.left)){
                    que.add(current.left);
                }
                if(current.right != null && !seen.contains(current.right)){
                    que.add(current.right);
                }
                if(nodeToParent.get(current) != null && !seen.contains(nodeToParent.get(current))){
                    que.add(nodeToParent.get(current));
                }
                seen.add(current);
            }
            level++;
        }
        return result;
        
    }
    
    public void connectNodeToParent(Map<TreeNode,TreeNode> nodeToParent, TreeNode current, TreeNode parent){
        if(current == null){
            return;
        }
        nodeToParent.put(current,parent);
        
        connectNodeToParent(nodeToParent,current.left, current);
        connectNodeToParent(nodeToParent,current.right, current);
    }
}