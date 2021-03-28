class Solution {
    public int lengthOfLongestSubstring(String s) {//only needs a for and a while
        if(s == null || s.length() == 0){
            return 0;
        }
        
        Set<Character> hs = new HashSet<>();
        int maxWindow = -1;
        
        int left = 0;
        
        for(int right = 0; right<s.length(); right++){
            char c = s.charAt(right);
            while(hs.contains(s.charAt(right))){
                hs.remove(s.charAt(left++));
            }
            
            hs.add(s.charAt(right));
            maxWindow = Math.max(maxWindow, right-left+1);
        }
        return maxWindow;
    }
}