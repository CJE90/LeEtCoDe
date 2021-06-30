class Solution {
    public boolean validTree(int n, int[][] edges) {
        int[] roots = new int[n];
        int countOfComponents = n;
        
        for(int i = 0; i<n;i++){
            roots[i] = i;
        }
        
        for(int[] edge:edges){
            if(connected(edge[0],edge[1],roots)){
                return false;
            }
            roots[root(edge[1],roots)] = edge[0];
            countOfComponents--;
        }
        return countOfComponents == 1;
        
        
    }
    public int root(int i, int[] roots){
        while(i != roots[i]){
            roots[i] = roots[roots[i]];
            i = roots[i];
        }
        return i;
    }
    public boolean connected(int p, int q, int[] roots){
        return root(p, roots) == root(q,roots);
    }
    
}