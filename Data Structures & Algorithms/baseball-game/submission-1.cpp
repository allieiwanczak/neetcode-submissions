class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> nums;
        int score = 0;

        for (int i = 0; i<operations.size(); i++) {
            if (operations[i] == "+") {
                int b = nums.top();
                nums.pop();
                int a = nums.top();
                nums.push(b);
                nums.push(a+b);
                score+= a+b;
            }
            else if (operations[i] == "C") {
                score-=nums.top();
                nums.pop();
            }
            else if (operations[i] == "D"){
                nums.push(nums.top()*2);
                score+=nums.top();
            }
            else {
                nums.push(stoi(operations[i]));
                score+=nums.top();
            }
        }
        return score;
    }
};