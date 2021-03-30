class Solution {
    public double[] medianSlidingWindow(int[] nums, int k) {
        List<Double> sortedArray = new ArrayList<>();
        List<Double> result = new ArrayList<>();
        int left = 0; int right = 0;
        
        
        while(left <= right && right < nums.length){
            sortedArray.add((double) nums[right]);
            
            while(right-left+1 == k){
                Collections.sort(sortedArray);
                if(k%2 ==0){
                    double sum =(double) sortedArray.get(k/2)+sortedArray.get((k/2)-1);
                    result.add(sum/2);
                }
                else{
                    result.add(sortedArray.get(k/2));
                }
                
                double numToRemove = nums[left];
                
                sortedArray.remove(sortedArray.indexOf(numToRemove));
                
                
                left++;
            }
            right++;
        }
        return result.stream().mapToDouble(i->i).toArray();
    }
}