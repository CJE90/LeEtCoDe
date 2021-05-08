class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        Map<Character,Integer> hm = new HashMap<>();
        for(Character c:s.toCharArray()){
            hm.put(c,hm.getOrDefault(c,0)+1);
        }
        
        for(Character c:t.toCharArray()){
            hm.put(c,hm.getOrDefault(c,0)-1);
            if(hm.get(c) == 0){
            hm.remove(c);
            }
        }
        
        if(hm.size() > 0){
            return false;
        }
        return true;
    }
}