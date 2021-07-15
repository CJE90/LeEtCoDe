class Solution {
    public String removeDuplicates(String s, int k) {
        Deque<Adjacent> stack = new ArrayDeque<>();
        for(char c:s.toCharArray()){
            if(!stack.isEmpty() && stack.peek().chr == c){
                stack.peek().frequency++;
            }
            else{
                stack.push(new Adjacent(c));
            }
            if(stack.peek().frequency == k){
                stack.pop();
            }
        }
        StringBuilder str = new StringBuilder();
        for(Adjacent a:stack){
            str.append(String.valueOf(a.chr).repeat(a.frequency));
        }
        
        return str.reverse().toString();
    }
    
    class Adjacent{
        char chr;
        int frequency;
        
        public Adjacent(char chr){
            this.chr = chr;
            this.frequency = 1;
        }
    }
}