class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int lRow = 0, lCol = 0, rRow = matrix.size()-1, rCol = matrix[0].size()-1, midR = 0;

        while (lRow<= rRow ) {
            midR = lRow + (rRow-lRow) /2;
            if (matrix[midR][0] > target) {
                rRow = midR-1;
            }
            else if (matrix[midR][rCol] < target) {
                lRow = midR+1;
            }
            else {
                break;
            }   
        }

        
        while (lCol <= rCol) {
            int midC = lCol + (rCol - lCol) /2;
            if (matrix[midR][midC] == target) return true;
            else if (matrix[midR][midC] < target) {
                lCol = midC +1;
            }
            else {
                rCol = midC-1;
            }
        }
        return false;
    
    }
};
