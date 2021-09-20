class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        
        int minLength = Integer.MAX_VALUE;
        int left = 0;
        int sum = 0;
        
        for(int right = 0; right<nums.length;right++){
            sum+= nums[right];
            while(sum>=target){
                minLength = Math.min(minLength, right-left+1);
                sum-=nums[left++];
            }
        }
        if(minLength == Integer.MAX_VALUE){
            return 0;
        }
        return minLength;
    }
}