class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, Integer> emailToIndex = new HashMap<>();
        UnionFind uf = new UnionFind(accounts.size());
        
        //crate hashamp of unioned indexes of emails
        
        //Iterate of every element in accounts
        for(int i = 0; i<accounts.size(); i++){
            //listOfEmails will be the reference to the list in each account element
            List<String> listOfEmails = accounts.get(i);
            //walk through each email
            for(int j = 1; j<listOfEmails.size();j++){
                //Store the current email in a String varialbe
                String currEmail = listOfEmails.get(j);
                //If the hashmap already contains the current email, the current email index can be unioned to the previously seen 
                //email. This tells us that the current account we are at is owned by the same person as found in the map
                if(emailToIndex.containsKey(currEmail)){
                    uf.union(emailToIndex.get(currEmail),i);
                }
                //Put the email and account index in the map.
                else{
                    emailToIndex.put(currEmail, i);
                }
            }
        }
        // Union find object now holds roots/parent of each account.
        // Need to create a master list of index of account and unioned emails
        
        Map<Integer, Set<String>> disjointSet = new HashMap<>();
        // Walk through each account element
        for(int i = 0; i<accounts.size();i++){
            //Store the root/parent index of each account in accounts
            int parentIndex = uf.root(i);
            // In our new object if the parent index is not there add it with empty set to store emails
            disjointSet.putIfAbsent(parentIndex, new HashSet<>());
            // CurSet represents the set for the parent index we are at(empty or not)
            Set<String> curSet = disjointSet.get(parentIndex);
            //For each email in the account we are in we add it to our set
            // remember that parent index will always lead back to the correct bucket to put emails in
            // regardless of where we are in Accounts
            for(int j = 1; j< accounts.get(i).size(); j++){
                curSet.add(accounts.get(i).get(j));
            }
            disjointSet.put(parentIndex, curSet);
        }
        
        List<List<String>> result = new ArrayList<>();
        for(Integer index:disjointSet.keySet()){
            List<String> curSet = new ArrayList<>();
            
            // for(String email:disjointSet.get(index)){
            //     curSet.add(email);
            // }
            
            if(disjointSet.containsKey(index)){
                curSet.addAll(disjointSet.get(index));
            }
            Collections.sort(curSet);
            curSet.add(0, accounts.get(index).get(0));
            result.add(curSet);
        }
//         System.out.println(result.toString());
        
//         System.out.println(disjointSet.toString());
//         uf.print();
//         System.out.println(emailToIndex.toString());
        
        
        return result;
    }
}

class UnionFind{
    private int[] id;
    private int[] sz;
    private int count;

    public UnionFind(int N) {
        id = new int[N];
        sz = new int[N];
        count = N;
        for(int i = 0; i < N; i++){
            id[i] = i;
            sz[i] = 1;
        }
    }

    public boolean isConnected(int p, int q){
        return root(p) == root(q);
    }

    public int root(int p){
        while(p != id[p]){
            id[p] = id[id[p]];
            p = id[p];
        }
        return p;
    }

    public void union(int p, int q){
        id[root(p)] = id[root(q)];
        // count--;
        // if(sz[p] >= sz[q]){
        //     id[q] = p;
        //     sz[p] += sz[q];
        // }
        // else{
        //     id[p] = q;
        //     sz[q] += sz[p];
        // }
    }
    public void print(){
        for(Integer i:id){
            System.out.print(i+", ");
        }
        System.out.println();
    }
}