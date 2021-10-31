class Solution {
    public int findMin(int[] nums) {
        if(nums[0]<=nums[nums.length-1]){
            return nums[0];
        }
        int lo = 0; int hi = nums.length-1;
        
        while(lo<hi){
            int mid = lo+(hi-lo)/2;
            // if(nums[mid]<nums[lo] && nums[mid]<nums[hi]){
            //     return nums[mid];
            // }
            if(nums[mid]>nums[hi]){
                lo = mid+1;
            }
            else if(nums[mid]<nums[hi]){
                hi = mid;
            }
        }
        return nums[lo];
    }
}






// while (low < high) {
//             auto mid = low + (high - low) / 2;
//             if (num[mid] < num[high])
//                 // the mininum is in the left part
//                 high = mid;
//             else if (num[mid] > num[high])
//                 // the mininum is in the right part
//                 low = mid + 1;
//         }

//         return num[low];
     