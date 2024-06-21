class Solution {
public:
    bool isValid(string s) {
        stack<char> parentheses;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ')' && !(parentheses.empty())) {
                if (parentheses.top() != '(') {
                    return 0;
                } else {
                    parentheses.pop();
                }
            }
            else if (s[i] == '}' && !(parentheses.empty())) {
                if (parentheses.top() != '{') {
                    return 0;
                } else {
                    parentheses.pop();
                }
            }
            else if (s[i] == ']' && !(parentheses.empty())) {
                if (parentheses.top() != '[') {
                    return 0;
                } else {
                    parentheses.pop();
                }
            }
            else {
                parentheses.push(s[i]);
            }
        }
        return parentheses.empty();
    }
};