class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int rows = matrix.size(), cols = matrix[0].size();
        vector<vector<int>> ans;
        if (rows == cols) {
           for (int r = 0; r< matrix.size(); r++) {
            for (int c = 0; c<r; c++) {
                swap(matrix[r][c], matrix[c][r]);
            }
        } 
        return matrix;
        } 
        else {
            for (int c = 0; c<cols;c++) {
                vector<int> row;
                for (int r = 0; r<rows; r++) {
                    row.push_back(matrix[r][c]);
                }
                ans.push_back(row);
            }
        }
        
        return ans;
    }
};