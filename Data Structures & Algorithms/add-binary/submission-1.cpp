class Solution {
public:
    string addBinary(string a, string b) {
        string ans = "";
        int l = a.length()-1, r = b.length()-1, carry = 0;

        while (l>=0 || r>=0 || carry >0) {
            int valA = l>= 0 ? a[l] - '0': 0;
            int valB = r>= 0? b[r] - '0':0;

            int sum = valA + valB + carry;
            carry = sum / 2;
            sum = sum %2 ;

            ans+= (sum) + '0';
            l--;
            r--;
        }   
        reverse(ans.begin(), ans.end());
        return ans;
    }
};