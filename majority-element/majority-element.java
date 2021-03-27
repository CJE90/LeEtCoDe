class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer,Integer> hm = new HashMap<>();
        for(Integer n:nums){
            hm.put(n,hm.getOrDefault(n,0)+1);
        }
        
        int max = 0;
        int ans = 0;
        for(Integer k:hm.keySet()){
            if(hm.get(k) > max){
                max = hm.get(k);
                    ans = k;
            }
        }
        return ans;
        
    }
}