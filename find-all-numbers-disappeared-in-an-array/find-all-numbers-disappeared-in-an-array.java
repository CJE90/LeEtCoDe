class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> hs = new HashSet<>();
        for(int i = 1; i<=nums.length; i++){
            hs.add(i);
        }
        for(Integer n:nums){
            hs.remove(n);
        }
        List<Integer> res = new ArrayList<>(hs);
        return res;
    }
}