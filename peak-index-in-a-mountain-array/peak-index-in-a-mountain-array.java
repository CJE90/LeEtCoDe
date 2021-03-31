class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int low = 0;
        int high = arr.length-1;
        int peak = high-1;
        
        while(low<high){
            
            int mid = low+(high-low)/2;
            System.out.println(mid);
            if(arr[mid]> arr[mid+1]){
                if(arr[mid]>arr[mid-1]){
                    return mid;
                }
                high = mid;
            }
            else{
                low = mid;
            }
            
        }
        return low;
        
        
    }
}