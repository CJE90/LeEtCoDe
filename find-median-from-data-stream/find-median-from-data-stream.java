class MedianFinder {
List<Integer> myArr = new ArrayList<>();
    /** initialize your data structure here. */
    public MedianFinder() {
         
    }
    
    public void addNum(int num) {
        myArr.add(num);
        Collections.sort(myArr);
        
        
    }
    
    public double findMedian() {
        int middle = myArr.size()/2;
        if(myArr.size() % 2 == 0){
            return (myArr.get(middle)+myArr.get(middle-1))/2.0;
        }
        else{
            return myArr.get(middle);
        }
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */


