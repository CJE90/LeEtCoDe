class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> answer = new ArrayList<>();
        backtrack(answer, 0, s.toCharArray());
        return answer;
    }
    
    public void backtrack(List<String> answer, int index, char[] s){
        if(index == s.length){
            answer.add(new String(s));
        }
        else{
            if(Character.isLetter(s[index])){
                s[index] = Character.toUpperCase(s[index]);
                backtrack(answer,index+1, s);
                s[index] = Character.toLowerCase(s[index]);
                backtrack(answer,index+1, s);
            }
            else{
                backtrack(answer,index+1,s);
            }
        }
    }
}




