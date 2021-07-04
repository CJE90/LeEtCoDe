class Solution {
    public int longestConsecutive(int[] nums) {
        UnionFind uf = new UnionFind(nums.length);
        Map<Integer, Integer> hm = new HashMap<>();
        
        for(int i = 0; i< nums.length; i++){
            if(hm.containsKey(nums[i])){
                continue;
            }
            hm.put(nums[i],i);
            if(hm.containsKey(nums[i]+1)){
                uf.union(i, hm.get(nums[i]+1));
            }
            if(hm.containsKey(nums[i]-1)){
                uf.union(i, hm.get(nums[i]-1));
            }
        }
        return uf.max();
        
    }
}

class UnionFind{
    private int id[];
    private int sz[];
    
    public UnionFind(int N){
        id = new int[N];
        sz = new int[N];
        for(int i = 0; i< N; i++){
            id[i] = i;
            sz[i] = 1;
        }
    }
    
    public int root(int i){
        while(i != id[i]){
            id[i] = id[id[i]];
            i = id[i];
        }
        return i;
    }
    
    public int max(){
        int max = 0;
        int[] count = new int[id.length];
        for(int i = 0; i<count.length; i++){
            count[root(i)]++;
            max = Math.max(max, count[root(i)]);
        }
        return max;
    }
    
    public void union(int p, int q){
        int i = root(p);
        int j = root(q);
        
        if(sz[i] <= sz[j]){
            id[i] = j;
            sz[j] += i;
        }
        else{
            id[j] = i;
            sz[i] += j;
        }
    }
}