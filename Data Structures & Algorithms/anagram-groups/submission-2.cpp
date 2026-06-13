class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
       vector<vector<string>> ans;
       unordered_map<string, vector<string>> anagrams;

       for (string s: strs) {
            string sSorted = s;
            sort(sSorted.begin(), sSorted.end());
            anagrams[sSorted].push_back(s);
       }

       for (const auto &match: anagrams) {
        ans.push_back(match.second);
       }

       return ans;

    }
};
