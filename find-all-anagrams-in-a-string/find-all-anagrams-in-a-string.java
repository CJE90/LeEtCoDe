class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        
        Map<Character, Integer> hm = new HashMap<>();
        
        List<Integer> ans = new LinkedList<>();
        for(Character c:p.toCharArray()){
            hm.put(c, hm.getOrDefault(c,0)+1);
        }
        
        int len = p.length();
        int count = 0;
        
        int left = 0;
        int right = 0;
        while(right<s.length()){
            if(hm.containsKey(s.charAt(right))){
                if(hm.get(s.charAt(right)) > 0){
                    count++;
                }
                hm.put(s.charAt(right), hm.get(s.charAt(right))-1);
            }
            while(right-left+1 > len){
                if(hm.containsKey(s.charAt(left))){
                    hm.put(s.charAt(left), hm.get(s.charAt(left))+1);
                    if(hm.get(s.charAt(left)) > 0){
                        count--;
                    }
                }
                left++;
            }
            if(count == len){
                ans.add(left);
            }
            right++;
        }
        
        
        return ans;
        
        
    }
}