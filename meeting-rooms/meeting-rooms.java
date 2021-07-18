class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals,(startTime1,startTime2)->Integer.compare(startTime1[0], startTime2[0]));
        for(int i = 0; i<intervals.length-1;i++){
            if(intervals[i][1] > intervals[i+1][0]){
                return false;
            }
        }
        return true;
        
    }
}