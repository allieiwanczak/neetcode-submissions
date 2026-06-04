class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set numSet(nums.begin(),nums.end());
        int longest = 0;

        for (int x: numSet) {
           if (numSet.find(x-1) == numSet.end()) {
            int curr = 1;
            while (numSet.find(x+curr) != numSet.end()) curr++;
            longest = max(longest, curr);
           } 
        }
        return longest;

    }
};
