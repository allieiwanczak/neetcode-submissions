class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> dp(n+1);
        dp[0] = 0;
        if (n == 0) return dp;
        dp[1]=1;
        if (n==1)return dp;
        int offset =1;
        
        for (int i = 2; i<=n; i++) {
            if (offset*2 == i) offset=i;
            dp[i] = dp[i-offset] +1; 
        }

        return dp;

    }
};
