class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> list = new ArrayList<>();
        backtrack(list, new ArrayList<>(), n, k, 1);
        return list;
    }
    public void backtrack(List<List<Integer>> list, List<Integer> tempList, int n, int k, int index){
        if(k == 0){
            list.add(new ArrayList(tempList));
            return;
        }
            for(int i = index; i<=n; i++){
                tempList.add(i);
                backtrack(list, tempList, n, k-1, i+1);
                tempList.remove(tempList.size()-1);
            }  
    }
    
	// public static List<List<Integer>> combine(int n, int k) {
	// 	List<List<Integer>> combs = new ArrayList<List<Integer>>();
	// 	combine(combs, new ArrayList<Integer>(), 1, n, k);
	// 	return combs;
	// }
	// public static void combine(List<List<Integer>> combs, List<Integer> comb, int start, int n, int k) {
	// 	if(k==0) {
	// 		combs.add(new ArrayList<Integer>(comb));
	// 		return;
	// 	}
	// 	for(int i=start;i<=n;i++) {
	// 		comb.add(i);
	// 		combine(combs, comb, i+1, n, k-1);
	// 		comb.remove(comb.size()-1);
	// 	}
	// }
}

