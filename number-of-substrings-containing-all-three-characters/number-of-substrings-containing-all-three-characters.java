class Solution {
    public int numberOfSubstrings(String s) {
        Map<Character,Integer> hm = new HashMap<>();
        int count = 0;
        int k = 3;
        int left = 0;
        int result = 0;
        
        for(int right = 0; right<s.length(); right++){
            hm.put(s.charAt(right), hm.getOrDefault(s.charAt(right),0)+1);
            
            while(hm.size() == 3){
                hm.put(s.charAt(left), hm.get(s.charAt(left))-1);
                if(hm.get(s.charAt(left)) == 0){
                    hm.remove(s.charAt(left));
                }
                left++;
            }
            result+=left;
        }
        return result;
    }
}


