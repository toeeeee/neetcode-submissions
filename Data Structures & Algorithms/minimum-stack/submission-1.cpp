class MinStack {
public:
    MinStack(): st1(), st2() {} // Actual stack and min stack
    
    void push(int val) {
        if (st2.empty()) {
            st2.push_back(val);
        }
        else if (val <= st2.back()) {
            st2.push_back(val);
        }
        st1.push_back(val);
    }
    
    // No need for empty checking on pop, top, getMin
    void pop() {
        int valToPop = st1.back();
        int curMin = st2.back();
        if (valToPop==curMin) {
            st2.pop_back();    
        }
        st1.pop_back();
    }
    
    int top() {
        return st1.back();
    }
    
    int getMin() { 
        return st2.back();
    }

    vector<int> st1;
    vector<int> st2;
};
