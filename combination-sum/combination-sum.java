class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> list = new ArrayList<>();
        
        backtrack(list, new ArrayList<>(), candidates, target, 0);
        return list; 
    }
    
    public void backtrack(List<List<Integer>> list, List<Integer> tempList, int[] nums, int target, int start){
        
        if(target == 0){
            list.add(new ArrayList(tempList));
        }
        
        for(int i = start; i<nums.length; i++){
            if(nums[i]<=target){
                tempList.add(nums[i]);
                target-=nums[i];
                backtrack(list, tempList, nums, target,i);
                target+=nums[i];
                tempList.remove(tempList.size()-1);
            }
        }
    }
}