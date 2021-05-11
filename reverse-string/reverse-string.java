class Solution {
    public void reverseString(char[] s) {
     helper(s,0,s.length-1);
    for(Character c:s){
            System.out.print(c);
        }
        
    }
    public void helper(char[] s, int l, int r){
        if(l>r){
            return;
        }
        helper(s,l+1,r-1);
        char temp  = s[l];
        s[l] = s[r];
        s[r] = temp;
        
    }
}

