class KthLargest {
public:
    priority_queue<int, vector<int>, std::greater<int>> minHeap;
    int sz = 0;
    int kth;

    KthLargest(int k, vector<int>& nums) {
        kth = k;
        
        for (auto cur: nums) {
            if (sz < k) {
                minHeap.push(cur);
                ++sz;
            }
            else {
                if ( !minHeap.empty() && (cur >= minHeap.top()) ) {
                    minHeap.pop();
                    minHeap.push(cur);
                }
            }
        }
    }
    
    int add(int val) {
        if (sz < kth) {
                minHeap.push(val);
                ++sz;
            }
        else {
            if ( !minHeap.empty() && (val >= minHeap.top()) ) {
                minHeap.pop();
                minHeap.push(val);
            } 
        }
        if (!minHeap.empty()) { return minHeap.top(); }
        else { return -99; }
    }
};
