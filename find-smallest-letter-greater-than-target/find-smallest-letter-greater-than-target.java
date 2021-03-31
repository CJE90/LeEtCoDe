class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        
        int low = 0;
        int high = letters.length-1;
        
        while(low <= high){
            int mid = (low+high)/2;
            System.out.println("Low: "+low+" High: "+high+" Mid:"+mid);
            System.out.println(letters[mid]);
            
            if(letters[mid] == target){
                if(mid>= letters.length){
                    return letters[0];
                }
                if(mid == letters.length-1){
                    return letters[0];
                }
                if(letters[mid+1] == target){
                    low++;
                }
                else{
                    return letters[mid+1];
                }
                
                
            }
            else if(letters[mid]<target){
                if(mid+1 < letters.length && letters[mid+1]>target){
                    return letters[mid+1];
                }
                if(mid == 0){
                    return letters[1];
                }
                low = mid+1;
            }
            else if(letters[mid]>target){
                if(mid-1 >= 0 && letters[mid-1]<=target){
                    return letters[mid];
                }
                high = mid-1;
            }
        }
        
        return letters[0];
        
    }
}



