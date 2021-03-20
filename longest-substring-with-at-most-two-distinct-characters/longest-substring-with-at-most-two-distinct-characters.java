class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        Map<Character,Integer> hm = new HashMap<>();
        int windowStart = 0;
        int max = Integer.MIN_VALUE;
        
        for(int windowEnd = 0; windowEnd < s.length(); windowEnd++){
            if(hm.containsKey(s.charAt(windowEnd))){
                int count = hm.get(s.charAt(windowEnd));
                hm.replace(s.charAt(windowEnd),count+1);
            }
            else{
                hm.put(s.charAt(windowEnd), 1);
            }
           while(hm.size() > 2){
               int count = hm.get(s.charAt(windowStart));
               if(count-1 == 0){
                   hm.remove(s.charAt(windowStart++));
               }
               else{
                   hm.replace(s.charAt(windowStart), count-1);
                   windowStart++;
               }
           }
            max = Math.max(max, windowEnd-windowStart+1);
        }
        return max;
    }
}