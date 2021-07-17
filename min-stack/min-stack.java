class MinStack {
    private Deque<Integer> stack;
    PriorityQueue<Integer> minHeap;
    /** initialize your data structure here. */
    public MinStack() {
        stack = new ArrayDeque<>();
        minHeap = new PriorityQueue<Integer>(); 
    }
    
    public void push(int val) {
        stack.push(val);
        minHeap.add(val);
    }
    
    public void pop() {
        int num = stack.pop();
        minHeap.remove(num);
    }
    
    public int top() {
        return stack.peek();
        
    }
    
    public int getMin() {
        return minHeap.peek();
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */