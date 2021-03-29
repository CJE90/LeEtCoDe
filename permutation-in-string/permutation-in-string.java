class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s1.length()){
            return false;
        }
        
        Map<Character,Integer> hm = new HashMap<>();
        for(Character c:s1.toCharArray()){
            hm.put(c, hm.getOrDefault(c,0)+1);
        }
        
        
        int count = s1.length();
        int len = s1.length();
        int left = 0;
        
        for(int right = 0; right < s2.length(); right++){
            if(hm.containsKey(s2.charAt(right))){
                if(hm.get(s2.charAt(right)) > 0){
                    count--;
                }
                hm.put(s2.charAt(right), hm.get(s2.charAt(right))-1);
            }
            
            while(right-left+1 == len && left<=right){
                
                if(count == 0){
                    return true;
                }
                if(hm.containsKey(s2.charAt(left))){
                    hm.put(s2.charAt(left), hm.get(s2.charAt(left))+1);
                    if(hm.get(s2.charAt(left)) > 0){
                        count++;
                    }
                }
                left++;
            }
        }
        return false;
        
    }
}