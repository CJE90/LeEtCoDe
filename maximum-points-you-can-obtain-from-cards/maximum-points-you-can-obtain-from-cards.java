class Solution {
    public int maxScore(int[] cardPoints, int k) {
        
        int score = Integer.MIN_VALUE;
        int l = 0;
        int currWindowSum = 0;
        
        int totalPoints = 0;
        for(Integer num:cardPoints){
            totalPoints+=num;
        }
        if(k == cardPoints.length){
            return totalPoints;
        }
        
        for(int r = 0; r<cardPoints.length;r++){
            currWindowSum += cardPoints[r];
            
            if(r>=cardPoints.length-k-1){
                score = Math.max(score,totalPoints-currWindowSum);
                currWindowSum -= cardPoints[r-(cardPoints.length-k-1)];
                l++;
            }
        }
        return score;
       
        
    }
}