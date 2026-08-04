class KthLargest {
public:
    priority_queue<int, vector<int>, std::greater<int>> minHeap;
    int k;

    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (auto num: nums) {
            if (minHeap.size() < k) { minHeap.push(num); }
            else {
                if (minHeap.top() <= num) { 
                    minHeap.pop();
                    minHeap.push(num);
                }
            }
        }
    }
    
    int add(int val) {
        if (minHeap.size() < k) { minHeap.push(val); }
        else {
            if (minHeap.top() <= val) { 
                minHeap.pop();
                minHeap.push(val);
            } 
        }
        if (!minHeap.empty()) return minHeap.top();
    }
};
