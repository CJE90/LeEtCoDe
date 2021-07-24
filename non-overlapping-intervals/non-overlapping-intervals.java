class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->Integer.compare(a[0],b[0]));
        int count = 0;
        int left = 0;
        int size = intervals.length;
        int right = 1;
        
        while(right<size){
            if(intervals[left][1]<=intervals[right][0]){
                left = right;
                right += 1;
            }
            else if(intervals[left][1]<=intervals[right][1]){
                count += 1;
                right += 1; //delete right
            }
            else if(intervals[left][1] > intervals[right][1]){
                count++;
                left = right;
                right += 1;
            }
        
        }
 return count;
    }
}



