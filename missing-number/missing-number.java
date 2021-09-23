class Solution {
    public int missingNumber(int[] nums) {
        int countFull = 0;
        int countHalf = 0;
        
        for(int i = 0; i<nums.length;i++){
            countFull+=i;
            countHalf+=nums[i];
        }
        countFull+=nums.length;
        return countFull-countHalf;
        
    }
}