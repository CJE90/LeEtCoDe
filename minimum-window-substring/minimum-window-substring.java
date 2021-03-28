class Solution {
    public String minWindow(String s, String t) {
        if(t.length() > s.length()){
            return "";
        }
        List<Integer> pair = new ArrayList<>();
        StringBuilder str = new StringBuilder();
        int minWindowSize = Integer.MAX_VALUE;
        pair.add(0);
        pair.add(s.length());
        Map<Character,Integer> hm = new HashMap<>();
        
        for(Character c:t.toCharArray()){
            hm.put(c, hm.getOrDefault(c,0)+1);
        }
        
        int left = 0; int right = 0; int count = 0;
        int len = t.length();
        
        while(right<s.length()){
            while(count!=len && right < s.length()){
                if(hm.containsKey(s.charAt(right))){
                    if(hm.get(s.charAt(right))>0){
                        count++;
                    }
                    hm.put(s.charAt(right), hm.get(s.charAt(right))-1);
                }
                right++;
            }
            while(count == len){
                if(hm.containsKey(s.charAt(left))){
                    hm.put(s.charAt(left), hm.get(s.charAt(left))+1);
                    if(hm.get(s.charAt(left)) > 0){
                        count--;
                    }
                }
                left++;
            }
            if(pair.get(1) - pair.get(0) > (right-1)-(left-1)){
            pair.set(0,left-1);
            pair.set(1,right-1);
            }
        }
        if(pair.get(1) - pair.get(0) +1 > s.length()){
            return "";
        }
        for(int i = pair.get(0); i<=pair.get(1); i++){
            str.append(s.charAt(i));
        }
        return str.toString();
        
    }
}