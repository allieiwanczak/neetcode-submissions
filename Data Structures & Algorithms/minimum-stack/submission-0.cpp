class MinStack {
public:
stack<int> stk;
stack<int> smallest;
    MinStack() {
        
    }
    
    void push(int val) {
        stk.push(val);
        val = min(val, smallest.empty() ? val: smallest.top());
        smallest.push(val);
    }
    
    void pop() {
        stk.pop();
        smallest.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return smallest.top();
    }
};
