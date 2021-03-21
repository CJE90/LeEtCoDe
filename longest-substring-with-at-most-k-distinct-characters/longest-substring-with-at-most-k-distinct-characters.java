class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        Map<Character, Integer> hm = new HashMap<>();
        int max = 0;
        int l = 0; int r = 0;
        
        while(r<s.length()){
            hm.put(s.charAt(r),r++);
            while(hm.size() > k){
                int minVal = Collections.min(hm.values());
                hm.remove(s.charAt(minVal));
                l = minVal+1;
            }
            max = Math.max(max, r-l);
        }
        return max;
    }
}