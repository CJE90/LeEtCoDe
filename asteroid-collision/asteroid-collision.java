class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> stack = new ArrayDeque<>();
        for(int asteroid:asteroids){
            if(asteroid > 0){
                stack.push(asteroid);
            }
            else{
                while(!stack.isEmpty() && stack.peek()>0 && stack.peek() < -asteroid){
                    stack.pop();
                }
                if(stack.isEmpty() || stack.peek()<0){
                    stack.push(asteroid);
                }
                else{
                    if(stack.peek() == -asteroid){
                        stack.pop();
                    }
                }
            }
        }
        
        int n = stack.size();
        int[] res = new int[n];
        for(int i = n-1; i>=0; i--){
            res[i] = stack.pop();
        }
        return res;
    }
}