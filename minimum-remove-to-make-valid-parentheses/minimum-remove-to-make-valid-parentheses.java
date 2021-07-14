class Solution {
    public String minRemoveToMakeValid(String s) {
        StringBuilder str = new StringBuilder(s);
        Deque<Integer> stack = new ArrayDeque<>();
        
        for(int i = 0; i<s.length();i++){
            if(s.charAt(i) == '('){
                stack.push(i);
            }
            if(s.charAt(i) == ')'){
                if(stack.isEmpty()){
                    str.setCharAt(i, '*');
                }
                else{
                    stack.pop();
                }
            }
        }
        
        while(!stack.isEmpty()){
            str.setCharAt(stack.pop(), '*');
        }
        
        return str.toString().replaceAll("\\*","");

    }
}