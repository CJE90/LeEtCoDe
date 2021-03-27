class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        
        Map<Character, Integer> hm = new HashMap<>();
        Map<Character, Integer> compare = new HashMap<>();
        List<Integer> ans = new LinkedList<>();
        for(Character c:p.toCharArray()){
            hm.put(c, hm.getOrDefault(c,0)+1);
        }
        
        int len = p.length();
        
        int start = 0;
        for(int end = 0; end<s.length();end++){
            compare.put(s.charAt(end), compare.getOrDefault(s.charAt(end),0)+1);
            
            while(end-start+1 == len){
                if(compare.equals(hm)){
                    ans.add(start);
                }
                if(compare.get(s.charAt(start)) == 1){
                    compare.remove(s.charAt(start));
                }
                else{
                    compare.put(s.charAt(start), compare.get(s.charAt(start))-1);
                }
                start++;
                
            }
        }
        return ans;
        
    }
}