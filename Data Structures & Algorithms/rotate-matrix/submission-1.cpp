class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        for (int r= 0; r<n;r++) {
            for (int c= 0; c<r; c++) {
                swap(matrix[r][c], matrix[c][r]);
            }
        }
        for (int row = 0; row<n; row++) {
            int l = 0, r= n-1;
            while(l<r) {
                swap(matrix[row][l], matrix[row][r]);
                r--;
                l++;
            }
        }
        
        
    }
};
