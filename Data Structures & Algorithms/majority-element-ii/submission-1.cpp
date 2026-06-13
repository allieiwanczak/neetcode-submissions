class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        unordered_map<int, int> freq;

        for (int x: nums) {
            freq[x]++;
        }
        
        for (const auto& pair: freq) {
            if (pair.second > n/3) ans.push_back(pair.first);
        }
        return ans;

    }
};