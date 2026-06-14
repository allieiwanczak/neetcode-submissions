class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int l = 0, r = nums.size()-1;
        k = k%nums.size();
        while (l<r) {
            swap(nums[l++], nums[r--]);
        }
        l = 0, r=k-1;
        
        while (l<r) {
            swap(nums[l++], nums[r--]);
        }
        l = k, r = nums.size()-1;

        while (l<r) {
            swap(nums[l++], nums[r--]);
        }
    }
};