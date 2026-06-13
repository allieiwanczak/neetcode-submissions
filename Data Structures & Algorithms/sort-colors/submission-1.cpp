class Solution {
public:
    void sortColors(vector<int>& nums) {
        int zero = 0, one= 0, two = 0;

        for (int x: nums) {
            if (x==0) {
                nums[two++] = 2;
                nums[one++] = 1;
                nums[zero++] = 0;
            }
            else if (x==1) {
                nums[two++] = 2;
                nums[one++] = 1;
            }
            else nums[two++] =2;
        }
    }
};