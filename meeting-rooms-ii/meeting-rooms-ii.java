class Solution {
    public int minMeetingRooms(int[][] intervals) {
        int[] startTimes = new int[intervals.length];
        int[] endTimes = new int[intervals.length];
        for(int i = 0; i<intervals.length;i++){
            startTimes[i] = intervals[i][0];
            endTimes[i] = intervals[i][1];
        }
        Arrays.sort(startTimes);
        Arrays.sort(endTimes);
        int maxFound = 0;
        int count = 0;
        int i = 0; int j = 0;
        while(i<intervals.length){
            if(startTimes[i]<endTimes[j]){
                count++;
                i++;
            }
            else{
                count--;
                j++;
            }
            maxFound = Math.max(count,maxFound);
        }
        return maxFound;
    }
}