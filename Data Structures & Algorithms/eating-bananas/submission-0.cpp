class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
       auto max_value = *max_element(piles.begin(), piles.end());

       int l = 1, r = max_value, ans=r;

       while (l<=r) {
        int mid = l + (r-l)/2;
        long long sum = 0;
        for (int i = 0; i< piles.size(); i++) {
            sum += (piles[i] + mid-1) / mid;
        }
        if (sum<= h) {
             ans = mid;
            r = mid-1;
        } else {
            l = mid+1;
        }
        
       }
       return ans;
    }
};
