class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> q = new ArrayDeque<>();
        List<Integer> answer = new ArrayList<>();
        
        for(int right = 0; right<nums.length; right++){
            while(!q.isEmpty() && nums[q.getLast()]<= nums[right]){
                q.removeLast();
            }
            
            q.addLast(right);
            
            if(q.getFirst() == right-k){
                q.removeFirst();
            }
            
            if(right>= k-1){
                answer.add(nums[q.peek()]);
            }
        }
        
        int[] result = new int[answer.size()];
        for(int i = 0; i<result.length;i++){
            result[i] = answer.get(i);
        }
        return result;
    }
}