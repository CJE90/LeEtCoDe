class Solution {
    public int countComponents(int n, int[][] edges) {
        if(n == 0 || n == 1){
            return n;
        }
        
        int[] roots = new int[n];
        for(int i = 0; i< n; i++){
            roots[i] = i;
        }
        Arrays.sort(edges, (a, b) -> Integer.compare(a[0], b[0]));
        
        for(int i = 0; i<edges.length; i++){
            int root1 = findRoot(edges[i][0],roots);
            int root2 = findRoot(edges[i][1],roots);
            //roots[edges[i][1]] = findRoot(edges[i][0],roots);
            if(root1 != root2){
                roots[root2] = root1;
            }
        }
        int count = 0;
    for(int i = 0; i < n; i++){
        if(roots[i] == i){
            count++;
        } 
    } 
    return count;
            
    }
    
    public int findRoot(int p, int[] roots){
        while(p != roots[p]){
            roots[p] = roots[roots[p]];
            p = roots[p];
        }
        return p ;
    }
}

   