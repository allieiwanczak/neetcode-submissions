class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> ans;
        sort(nums.begin(), nums.end());
        long long t = target; 

        for (int i = 0; i<nums.size(); i++) {
            for (int j = 0; j<nums.size(); j++) {
                if (i==j) continue;
                int l = j+1, r = nums.size()-1;
                while (l<r) {
                    long long sum = (long long)nums[l] + nums[r]+nums[i]+nums[j];
                    if (sum > t) r--;
                    else if (sum< t) l++;
                    else {
                        vector<int> candidate = {nums[i], nums[j], nums[l], nums[r]};
                        sort(candidate.begin(), candidate.end());
                        if (find(ans.begin(), ans.end(), candidate) == ans.end() &&
                        r!=j && r!=i && l!=i && l!=j) {
                            ans.push_back(candidate);
                        }
                        l++;
                        r--;
                        while (l<r && nums[l] == nums[l-1])l++;
                        while (l<r && nums[r] == nums[r-1])r--;
                    }

                }
            }
        }
        return ans;
    }
};