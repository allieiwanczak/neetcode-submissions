class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, vector<int>> rows;
        unordered_map<int, vector<int>> cols;
        unordered_map<int, vector<int>> squares;
        
        
        for (int i = 0; i< 9; i++) {
            for (int j=0; j<9; j++) {
                int sqI = i/3 *3 +j/3;
                if (board[i][j] != '.') {
                    if (find(rows[i].begin(), rows[i].end(), board[i][j]) != rows[i].end() ||
                find(cols[j].begin(), cols[j].end(), board[i][j]) != cols[j].end() ||
               find(squares[sqI].begin(), squares[sqI].end(), board[i][j]) != squares[sqI].end()) 
                return false;
                rows[i].push_back(board[i][j]);
                cols[j].push_back(board[i][j]);
                squares[sqI].push_back(board[i][j]);
                }
                
            }
        }
        return true;
    }
};
