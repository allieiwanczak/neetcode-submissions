class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
       sort(strs.begin(), strs.end());
       string prefix = "";

       for (int i = 0; i < strs[0].length(); i++) {
        char candidate = strs[0][i];
        prefix+= candidate;
        for (int j = 0; j < strs.size(); j++) {
            if (strs[j][i] != candidate) {
                prefix.pop_back();
                return prefix;
            }
        
        }
       } 
       return prefix;
    }
};