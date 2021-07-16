class Solution {
    public String decodeString(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        
        for(int i = 0; i<s.length();i++){
            //If we are not at the end of a string to decode we need to push the character onto the stack
            if(s.charAt(i) != ']')
                stack.push(s.charAt(i));
            else{
                //if we have found an ending bracket we now need to decode the string
                List<Character> decodedString = new ArrayList<>();
                //this allows us to manage all characters on the stack after the opening bracket
                //and store them in a list of character
                while(stack.peek() != '['){
                    decodedString.add(stack.pop());
                }
                //pop off the [ character
                stack.pop();
                //Now we need to grab our K value. We need to handle if k is larger than 9
                int base = 1;
                int k = 0;
                while(!stack.isEmpty() && Character.isDigit(stack.peek())){
                    k = k + (stack.pop() - '0') * base;
                    base *=10;
                }
                //Now we have our k and our decoded string. We need to push the characters back on to the stack 
                while(k != 0){
                    for(int j = decodedString.size()-1; j >= 0; j--){
                        stack.push(decodedString.get(j));
                    }
                    k--;
                }
            }
        }
        
        StringBuilder str = new StringBuilder(stack.size());
        while(!stack.isEmpty()){
            str.append(stack.pop());
        }
        return str.reverse().toString();
        
    }
}