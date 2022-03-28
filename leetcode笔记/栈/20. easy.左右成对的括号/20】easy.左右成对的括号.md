## 检测输入的括号是否全部成对 
##### 此题目给的字符串一般是全都为括号的

python:
##### 注意python没有栈结构，用列表来模拟栈结构
```python
class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {
            ")": "(", 
            "}": "{", 
            "]": "["
        }
        # 遍历 字符串 s
        for char in s:
            if char in mapping:     # 如果是右边的括号，把上一个送进去的推出来
                if stack:                       # 栈是否为空
                    top_element = stack.pop()   # 元素出栈
                else:
                    top_element = '#'
                
                if mapping[char] != top_element:    # 如果括号交叉不配对的话'{{[}]}' 直接返回 false
                    return False
            else:                   # 如果是左边的括号 送入栈
                stack.append(char)

        # stack 为空 返回 True
        return not stack
```
c++:
```c++
class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        //只有左符号才入栈
        for (int i = 0; i < s.size(); i++)
        {
            
            if (s[i] == '(' || s[i] == '{'|| s[i] == '[')
            {   
                st.push(s[i]);          //左符号,入栈
            }
            else
            {   
                // 不是左边的符号
                if (st.size() == 0){
                    return false;       // 栈为空
                }

                char top = st.top();    // 获取栈顶元素
                st.pop();

                char match;             
                if (s[i] == ')')        // 如果是右边的元素
                    match = '(';
                else if(s[i] == '}')
                    match = '{';
                else{
                    assert(s[i] == ']');
                    match = '[';
                }

                if (top != match){
                    return false;
                }
            }  
        }

        if (st.size() != 0){
            return false;
        }
        return true;
    }
};
```