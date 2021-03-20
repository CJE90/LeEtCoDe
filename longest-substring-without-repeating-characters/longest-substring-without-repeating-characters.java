class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> hs = new HashSet<>();
        int maxWindowSize = Integer.MIN_VALUE;
        int windowStart = 0;
        
        if(s.length() == 0){
            return 0;
        }
        
        for(int windowEnd = 0; windowEnd < s.length(); windowEnd++){
            if(!hs.contains(s.charAt(windowEnd))){
                hs.add(s.charAt(windowEnd));
                maxWindowSize = Math.max(maxWindowSize, windowEnd-windowStart+1);      
            }
            else{
                while(hs.contains(s.charAt(windowEnd))){
                    if(s.charAt(windowStart) != s.charAt(windowEnd)){
                        hs.remove(s.charAt(windowStart));
                        windowStart++;
                    }
                    else{
                        windowStart++;
                        break;
                    }
                }
            }
            
        }
        return maxWindowSize;
    }
}