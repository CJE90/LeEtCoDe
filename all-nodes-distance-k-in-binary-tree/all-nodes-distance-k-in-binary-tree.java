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
        
        List<Integer> ans = new ArrayList<>();
        Map<TreeNode, TreeNode> nodeToParent = new HashMap<>();
        Set<TreeNode> seen = new HashSet<>();
        Queue<TreeNode> que = new LinkedList<>();
        if(k ==0){
            ans.add(target.val);
            return ans;
        }
        mapNodeToParent(nodeToParent, root, null);
        
        que.offer(target);
        int level = 0;
        while(!que.isEmpty()){
            int n = que.size();
            
            for(int i = 0; i<n;i++){
                
                TreeNode cur = que.poll();
                seen.add(cur);
                if(level == k && cur!=target){
                    ans.add(cur.val);
                }
                if(cur.left != null && !seen.contains(cur.left)){
                    que.offer(cur.left);
                }
                if(cur.right != null && !seen.contains(cur.right)){
                    que.offer(cur.right);
                }
                if(nodeToParent.get(cur) != null && !seen.contains(nodeToParent.get(cur))){  
                    que.offer(nodeToParent.get(cur));
                }
            }
            level++;
        }
        return ans;
        
        
    }
    public void mapNodeToParent(Map<TreeNode,TreeNode> hm, TreeNode current, TreeNode parent){
        if(current == null){
            return;
        }
        hm.put(current,parent);
        mapNodeToParent(hm,current.left,current);
        mapNodeToParent(hm,current.right,current);
    }
}