class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList<>();
        backtrack(list, "", n, 0, 0);
        return list;
    }
    
    public void backtrack(List<String> list, String s, int max, int open, int close){
        if(s.length() == max*2){
            list.add(s);
            return;
        }
        if(open<max){
            
            backtrack(list, s+'(', max, open+1, close);
        }
        if(close<open){
            
            backtrack(list, s+')', max, open, close+1);
        }
        
    }
}

