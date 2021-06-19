class Solution {
    public int maxVowels(String s, int k) {
        Set<Character> hs = new HashSet<>();
        hs.add('a');
        hs.add('e');
        hs.add('i');
        hs.add('o');
        hs.add('u');
        int left = 0;
        int count = 0;
        int maxCount = 0;
        for(int right = 0; right<s.length();right++){
            if(hs.contains(s.charAt(right))){
                count++;
            }
            while(right-left+1 > k){
                if(hs.contains(s.charAt(left))){
                    count--;
                }
                left++;
            }
            maxCount = Math.max(count, maxCount);   
               
        } 
        return maxCount;
    }
               
}