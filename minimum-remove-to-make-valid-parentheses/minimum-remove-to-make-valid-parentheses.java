class Solution {
    public String minRemoveToMakeValid(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        
        for(int i = 0; i < s.length(); i++){
            if(s.charAt(i) == '('){
                stack.push(i);
            }
            else if(s.charAt(i) == ')'){
                if(stack.isEmpty()){
                    stack.push(i);
                }
                else{
                    
                    if(s.charAt(stack.peek()) == ')'){
                        stack.push(i);
                    }
                    else{
                        stack.pop();
                    }
                    
                }
            }
        }
        
        
        int[] nums = new int[stack.size()];
        int numsSize = stack.size();
        for(int i = 0; i< numsSize; i++){
            nums[i] = stack.pop();
        }
            
        int count = nums.length-1;
        
        StringBuilder str = new StringBuilder();
        
        for(int i = 0; i<s.length();i++){
            if(count >= 0){
                if(i == nums[count]){
                    count--;
                    continue;
                }
                else{
                    str.append(s.charAt(i));
                }  
            }
            else{
            str.append(s.charAt(i));}
        }
        return str.toString();
        
    }
}