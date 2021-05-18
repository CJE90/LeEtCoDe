class Solution {
    public int fib(int n) {
        if(n == 0){
            return 0;
        }
        int[] arr = new int[n];
        return helper(n, arr);
    }
    public int helper(int n, int[] arr){
        if(arr[n-1] != 0){
            return arr[n-1];
        }
        if(n<3){
            return 1;
        }
        arr[n-1] = helper(n-1,arr)+helper(n-2,arr);
        return arr[n-1];
    }
}