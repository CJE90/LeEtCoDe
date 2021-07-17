class Solution {
    public int maxDepth(String s) {
        int maxDepth = 0;
        int currentDepth = 0;
        Deque<Character> stack = new ArrayDeque<>();
        
        for(char c:s.toCharArray()){
            if(c == '('){
                stack.push('(');
                currentDepth++;
                maxDepth = Math.max(maxDepth, currentDepth);
            }
            if(c == ')'){
                stack.pop();
                    currentDepth--;
                
            }
        }
        return maxDepth;
    }
}