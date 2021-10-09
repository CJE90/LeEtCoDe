class Solution {
    public int maximumSwap(int num) {
        char[] digits = String.valueOf(num).toCharArray();
        int[] maxIndexes = new int[digits.length];
        int maxPosition = digits.length-1;
        maxIndexes[maxPosition] = maxPosition;
        
        for(int i = digits.length-2; i>= 0; i--){
            if(digits[i]>digits[maxPosition]){
                maxPosition = i;
            }
            maxIndexes[i] = maxPosition; 
        }
        for(int i = 0; i<digits.length; i++){
            if(digits[i] != digits[maxIndexes[i]]){
                char temp = digits[i];
                digits[i] = digits[maxIndexes[i]];
                digits[maxIndexes[i]] = temp;
                return Integer.parseInt(String.valueOf(digits));
            }
        }
        return num;
    }
    
//     public int maximumSwap(int num) {
//         char[] digits = String.valueOf(num).toCharArray();
//         int[] maxIdx = new int[digits.length];
//         int maxPos = digits.length - 1;
//         maxIdx[maxPos] = maxPos;
        
//         for (int i = digits.length - 2; i >= 0; i--) {
//             if (digits[i] > digits[maxPos]) {
//                 maxPos = i;
//             }
//             maxIdx[i] = maxPos;
//         }
        
//         for (int i = 0; i < digits.length; i++) {
//             if (digits[i] != digits[maxIdx[i]]) {
//                 char tmp = digits[i];
//                 digits[i] = digits[maxIdx[i]];
//                 digits[maxIdx[i]] = tmp;
//                 return Integer.parseInt(String.valueOf(digits));
//             }
//         }
        
//         return num;
//     }
}