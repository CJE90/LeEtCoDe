class MedianFinder {
    private PriorityQueue<Integer> lo = new PriorityQueue<>(Collections.reverseOrder());//max heap
    private PriorityQueue<Integer> hi = new PriorityQueue<>(); //min heap
    

    /** initialize your data structure here. */
    public MedianFinder() {
        
    }
    
    public void addNum(int num) {
        // Default putting nums in the Max heap
        lo.offer(num);
        // Need to verify that numbers in lo are <= to numbers in hi, if not move number from lo to hi
        if(lo.size() != 0 && hi.size() != 0 && lo.peek() > hi.peek()){
            hi.offer(lo.poll());
        }
        
        // Verify sizes are balanced +/- 1
        if(lo.size()>(hi.size()+1)){
            hi.offer(lo.poll());
        }
        else if(hi.size()>lo.size()+1){
            lo.offer(hi.poll());
        }
    }
    
    public double findMedian() {
        if(hi.size() > lo.size()){
            return hi.peek();
        }
        else if(hi.size() < lo.size()){
            return lo.peek();
        }
        else{
        return (lo.peek()+hi.peek())*0.5;}
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */