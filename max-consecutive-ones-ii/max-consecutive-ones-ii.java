class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxWindowLength = Integer.MIN_VALUE;
        int windowStart = 0;
        boolean flippedZero = false;
        int lastSeenZero = 0;
        
        for(int windowEnd = 0; windowEnd < nums.length; windowEnd++){
            if(nums[windowEnd] == 1){
                maxWindowLength = Math.max(maxWindowLength, windowEnd-windowStart+1);
            }
            else if(nums[windowEnd] == 0 && !flippedZero){
                maxWindowLength = Math.max(maxWindowLength, windowEnd-windowStart+1);
                flippedZero = true;
                lastSeenZero = windowEnd;
            }
            else{
                windowStart = lastSeenZero+1;
                lastSeenZero = windowEnd;
            }
        }
        return maxWindowLength;
    }
}