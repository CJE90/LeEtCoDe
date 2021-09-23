class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> hashSet = new HashSet<>();
        for(Integer n:nums){
            if(hashSet.contains(n)){
                return true;
            }
            hashSet.add(n);
        }
        return false;
    }
}