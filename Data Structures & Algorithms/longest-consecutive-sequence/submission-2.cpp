class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> arr(nums.begin(), nums.end());

        int max_count = 0;
        for (int x: nums) {
            int count = 0;
            if(arr.find(x-1) == arr.end()) {
                while (arr.find(x+count) != arr.end()) count++;
                max_count = max(count, max_count);
            }
            
        }
        return max_count;
    }
};
