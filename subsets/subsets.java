class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        dfs(nums, new ArrayList<>(),answer, 0);
        return answer;
        
    }
    
    public void dfs(int[] nums, List<Integer> subset, List<List<Integer>> answer, int index){
        
        answer.add(new ArrayList<>(subset));
        for(int i = index; i< nums.length; i++){
            subset.add(nums[i]);
            dfs(nums, subset, answer, i+1);
            subset.remove(subset.size()-1);
        } 
    }
    
}

