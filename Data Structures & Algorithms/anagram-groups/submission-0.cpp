class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> seen;
        vector<vector<string>> ans;
        for (const string& s : strs) {
            string sortedS = s;
            sort(sortedS.begin(), sortedS.end());
            seen[sortedS].push_back(s);
        }
        for (auto& x: seen) {
            ans.push_back(x.second);
        }
        return ans;
    }
};
