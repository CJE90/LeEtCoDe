class Solution {
    public boolean isValid(String s) {
        if(s.length() < 2){
            return false;
        }
        Stack<Character> stack = new Stack<>();
        
        for(Character c:s.toCharArray()){
            if(c == '('){
                stack.push(')');
            }
            else if(c == '['){
                stack.push(']');
            }
            else if(c == '{'){
                stack.push('}');
            }
            else{
                if(!stack.isEmpty()){
                    char temp = stack.pop();
                    if(temp != c){
                        return false;
                    }
                }
                else{return false;}
            }
        }
        
        return stack.isEmpty();
    }
}