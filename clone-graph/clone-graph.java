/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    public Node cloneGraph(Node node) {
        if(node == null){
            return node;
        }
        Queue<Node> que = new LinkedList<>();
        Map<Node,Node> visited = new HashMap<>();
        
        que.add(node);
        visited.put(node, new Node(node.val, new ArrayList()));
        while(!que.isEmpty()){
           Node n = que.poll();
            for(Node neighbor:n.neighbors){
                if(!visited.containsKey(neighbor)){
                    que.add(neighbor);
                    visited.put(neighbor, new Node(neighbor.val, new ArrayList())); 
                }
                visited.get(n).neighbors.add(visited.get(neighbor));
            }
            
        }
        
        
        return visited.get(node);
    }
}