实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返回栈中最小元素的操作
[leetcode](https://leetcode-cn.com/problems/min-stack/)


solution：
C++: [参考](https://www.cnblogs.com/zhangwanying/p/9886577.html)
```c++
class MinStack {
	
public:
    MinStack() {
    }
	
    // 入栈
    void push(int x) {
        stk.push(x);
        if (!help.empty()) {
            // 比help栈的栈顶小才入栈
            // 这样help栈的栈顶一定是最小的 因为比栈顶大的不会进这个栈
            help.push( min(help.top(), x) ); 
        }   
        else
            help.push(x);
    }
    
    // 出栈
    void pop() {
        stk.pop();
        help.pop();
    }
    
    // 获取栈顶
    int top() {
        return stk.top();
    }
    
    // 返回栈最小元素
    int getMin() {
        return help.top();
    }
	
	// 借助两个栈
    stack<int> stk, help;
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
 ```