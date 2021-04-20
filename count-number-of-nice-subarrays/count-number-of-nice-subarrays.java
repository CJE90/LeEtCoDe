class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int finalCount = 0;
        int countOfNiceSubArrays = 0;
        int countOfOddNumbers = 0;
        int left = 0;
        
        for(int right = 0; right < nums.length; right++){
            if(nums[right] %2 != 0){
                countOfOddNumbers++;
                countOfNiceSubArrays = 0;
            }
            
            
            
            while(countOfOddNumbers >= k){
                countOfNiceSubArrays++;
                if(nums[left] %2 != 0){
                    countOfOddNumbers--;
                }
                
                left++;
            }
            
            finalCount+=countOfNiceSubArrays;
        }
        return finalCount;
    }
}