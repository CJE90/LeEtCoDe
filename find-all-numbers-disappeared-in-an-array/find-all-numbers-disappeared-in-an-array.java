class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> answer = new ArrayList<>();
        int[] test = new int[nums.length+1];
        for(int i = 0; i<nums.length; i++){
            test[nums[i]] = -1;
        }
        for(int i = 1; i<test.length; i++){
            if(test[i] == 0) answer.add(i);
        }
        return answer;
        
    }
}