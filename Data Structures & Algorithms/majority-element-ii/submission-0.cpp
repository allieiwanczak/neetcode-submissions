class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        unordered_map<int, int> freq;

        for (int x: nums) {
            freq[x]++;
            if (freq[x] > n/3 && find(ans.begin(), ans.end(), x) == ans.end()) ans.push_back(x);
        }
        return ans;

    }
};