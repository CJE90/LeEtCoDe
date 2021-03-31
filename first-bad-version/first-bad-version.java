/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int low = 0;
        int high = n;
        while(low<=high){
            int mid = low + ((high - low) / 2);
            if(!isBadVersion(mid)){
                if(isBadVersion(mid+1)){
                    return mid+1;
                }
                else{
                    low=mid;
                }
            }
            else{
                high = mid;
                
            }
        }
        return -1;
        
    }
}