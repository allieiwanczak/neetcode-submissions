class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> chars;
        int maxLength = 0;
        int l = 0;

        for (int r = 0; r<s.size(); r++) {
            while (chars.find(s[r]) != chars.end()) {
                chars.erase(s[l]);
                l++;
            }
            chars.insert(s[r]);
            maxLength = max(r-l+1, maxLength);
            
        }
        return maxLength;

    }
};
