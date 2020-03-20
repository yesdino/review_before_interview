class MinStack {
	
public:
    MinStack() {
    }
	
    // 入栈
    void push(int x) {
        stk.push(x);
        if (!minstk.empty()) {
            // 比 minstk 栈的栈顶小才入栈
            // 这样 minstk 栈的栈顶一定是最小的 因为比栈顶大的不会进这个栈
            minstk.push( min(minstk.top(), x) ); 
        }   
        else
            minstk.push(x);
    }
    
    // 出栈
    void pop() {
        stk.pop();
        minstk.pop();
    }
    
    // 获取栈顶
    int top() {
        return stk.top();
    }
    
    // 返回栈最小元素
    int getMin() {
        return minstk.top();
    }
	
	// 借助两个栈
    stack<int> stk, minstk;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */