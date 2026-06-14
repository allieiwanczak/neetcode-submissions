class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        int count = 0;
        unordered_map<int,int> freq;

        for (int i =0; i< nums.size(); i++) {
            if (freq.find(nums[i]) != freq.end() && abs(i - freq[nums[i]]) <= k) {
                return true;
            }
            else {
                freq[nums[i]] = i;
            }
        }
        return false;
    }
};