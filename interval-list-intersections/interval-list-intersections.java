class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> result = new ArrayList<>();
        int i = 0; int j=0;
        
        while(i < firstList.length && j < secondList.length){
            if(firstList[i][0]<=secondList[j][1] && firstList[i][1]>=secondList[j][0]){
                int[] temp = new int[2];
                temp[0] = Math.max(firstList[i][0],secondList[j][0]);
                temp[1] = Math.min(firstList[i][1],secondList[j][1]);
                result.add(temp);
            }
            if(firstList[i][1]<= secondList[j][1]){
                i++;
            }
            else if(secondList[j][1]<=firstList[i][1]){
                j++;
            }
        }
       return result.toArray(new int[result.size()][]);
    }
}