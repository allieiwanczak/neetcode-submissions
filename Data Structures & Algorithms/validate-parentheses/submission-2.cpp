class Solution {
public:
    bool isValid(string s) {
        int n = s.length();
        stack<char> brackets;
        unordered_map<char, char> pairs = {{'{', '}'}, {'[', ']'}, {'(', ')'}};

        int i = 0;
        while (i<n) {
            if (pairs.find(s[i]) != pairs.end()){
                brackets.push(s[i]);
                i++;
            } else{
            if (brackets.empty()) return false;
            char last = brackets.top();
            brackets.pop();
            if (pairs[last] != s[i]) return false;
            i++; 
            }
        } 
        return brackets.empty();
    }
};
