class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> curr;
        for (const string& x: tokens) {
            if (x == "+") {
                int a = curr.top(); curr.pop();
                int b = curr.top(); curr.pop();
                curr.push(a+b);
            }
            else if (x == "-") {
                int a = curr.top(); curr.pop();
                int b = curr.top(); curr.pop();
                curr.push(b-a);
            }
            else if (x == "*") {
                int a = curr.top(); curr.pop();
                int b = curr.top(); curr.pop();
                curr.push(a*b);
            }
            else if (x == "/") {
                int a = curr.top(); curr.pop();
                int b = curr.top(); curr.pop();
                curr.push(b/a);
            }
            else {
                curr.push(stoi(x));
            }
        }
        return curr.top();
    }
};
