class Solution {
    public int maxSatisfied(int[] customers, int[] grumpy, int minutes) {
        int nonGrumpy = 0;
        int custWhileGrumpy = 0;
        int max = 0;
        
        
        for(int right = 0; right<customers.length;right++){
            if(grumpy[right] == 0){
                nonGrumpy += customers[right];
            }
            if(grumpy[right] == 1){
                custWhileGrumpy += customers[right];
            }
            if(right>=minutes && grumpy[right-minutes] == 1){
                custWhileGrumpy -= customers[right-minutes];
            }
            max = Math.max(custWhileGrumpy, max);
        }
        return nonGrumpy+max;
        
    }
}