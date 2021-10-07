class Solution {
    public int search(int[] nums, int target) {
        int lo = 0; 
        int hi = nums.length-1;
        
        Arrays.sort(nums);
        
        while(lo<=hi){
            int mid = lo+(hi-lo)/2;
            if(target == nums[mid]){
                return mid;
            }
            if(target<nums[mid]){
                hi = mid-1;
                
            }
            if(target>nums[mid]){
                lo = mid+1;
                
            }
            
        }
        return -1;
        
    }
}