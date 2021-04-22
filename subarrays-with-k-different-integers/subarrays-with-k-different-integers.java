class Solution {
    public int subarraysWithKDistinct(int[] A, int K) {
        return atMost(A,K) - atMost(A,K-1);
    }
    
    public int atMost(int[] A, int K){
        Map<Integer,Integer> hm = new HashMap<>();
        int left = 0;
        int count = 0;
        
        for(int right = 0; right < A.length; right++){
            hm.put(A[right], hm.getOrDefault(A[right],0)+1);
            if(hm.get(A[right]) == 1){
                K--;
            }
            while(K<0){
                hm.put(A[left], hm.get(A[left])-1);
                if(hm.get(A[left]) < 1){
                    hm.remove(A[left]);
                    K++;
                }
                left++;
            }
            count += right-left+1;  
        }   
        return count;
    }
    
}
