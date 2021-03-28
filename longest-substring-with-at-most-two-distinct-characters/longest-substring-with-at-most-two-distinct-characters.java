class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        int maxWindow = -1;
        Map<Character,Integer> hm = new HashMap<>();
        
        int left = 0;
        for(int right = 0; right < s.length(); right++){
            char c = s.charAt(right);
            hm.put(c,hm.getOrDefault(c,0)+1);
            
            while(hm.size() > 2 && left<right){
                if(hm.get(s.charAt(left)) == 1){
                    hm.remove(s.charAt(left++));
                }
                else{
                    hm.put(s.charAt(left), hm.get(s.charAt(left++))-1);
                }
            }
            maxWindow = Math.max(maxWindow, right-left+1);
        }
        return maxWindow;
    }
}