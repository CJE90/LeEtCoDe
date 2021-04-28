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

/*
Find Max in array
Create node
recurse left side of array setting next max as left child
recurse right side of array setting nex max as right child

return first created node.

*/
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if(nums.length == 0 ){
            return null;
        }
        
       return createFromMax(nums,0,nums.length);
    }
    
    public TreeNode createFromMax(int[] nums, int left, int right){
        
        if(left == right){
            
            return null;
        }
        int indexOfMax = left;
        for(int i = left; i<right;i++){
            if(nums[i] > nums[indexOfMax]){
                indexOfMax = i;
            }
        }
        
        TreeNode node = new TreeNode(nums[indexOfMax]);
        node.left = createFromMax(nums, left, indexOfMax);
        node.right = createFromMax(nums, indexOfMax+1,right);
        
        return node;
        
    }
}