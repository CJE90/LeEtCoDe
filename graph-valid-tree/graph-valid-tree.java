class Solution {
    public boolean validTree(int n, int[][] edges) {
        if(n == 1){
            return true;
        }
        int[] id = new int[n];
        for(int i = 0; i < n; i++){
            id[i] = i;
        }
        for(int[] edge:edges){
            if(isConnected(edge[0],edge[1],id)){
                return false;
            }
            union(edge[0],edge[1], id);
            n--;
        }
        return n == 1;
        
    }
    public boolean isConnected(int p, int q, int[] id){
        return root(p, id) == root(q, id);
    }
    public void union(int p, int q, int[] id){
        id[root(q,id)] = root(p,id);
    }
    public int root(int i, int[] id){
        while(i != id[i]){
            id[i] = id[id[i]];
            i = id[i];
        }
        return i;
    }
}