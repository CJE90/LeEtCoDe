class Solution {
    public List<String> letterCasePermutation(String s) {
        List<String> result = new ArrayList<>();
        backtrack(result,s.toCharArray(),0);
        return result;
    }
    
    public void backtrack(List<String> result, char[] s, int i){
        //System.out.println(index+" "+s.length);
        if(i == s.length){
            result.add(new String(s));
            return;
        }
        else{
            
                if(Character.isDigit(s[i])) backtrack(result, s, i+1);
                else{
                    s[i] = Character.toUpperCase(s[i]);
                    backtrack(result, s, i+1);
                    s[i] = Character.toLowerCase(s[i]);
                    backtrack(result, s, i+1);  
                }
            
        }
    }
}