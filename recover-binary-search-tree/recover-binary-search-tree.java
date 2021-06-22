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
    public void recoverTree(TreeNode root) {
        List<Integer> arr = new ArrayList<>();
        inorder(root,arr);
        
        int[] pair = findPair(arr);
        dfsSwap(root, 2, pair[0],pair[1]);
        
        
    }
    public void dfsSwap(TreeNode root, int count, int x, int y){
        if(root == null){
            return;
        }
        if(root.val == x){
            root.val = y;
            count--;
        }else if(root.val == y){
            root.val = x;
            count--;
        }
        if(count == 0){
            return;
        }
        
        dfsSwap(root.left,count, x,y);
        dfsSwap(root.right,count, x,y);
       
    }
    public void inorder(TreeNode root, List<Integer> arr){
        if(root == null){
            return;
        }
        inorder(root.left, arr);
        arr.add(root.val);
        inorder(root.right, arr);
    }
    public int[] findPair(List<Integer> list){
        
        int x = -1, y=-1;
        for(int i = 0; i<list.size()-1; i++){
            if(list.get(i)> list.get(i+1)){
                y = list.get(i+1);
                if(x ==-1){
                    x = list.get(i);
                }
                else{
                    break;
                }  
            } 
        }
        return new int[]{x,y};
    }
}