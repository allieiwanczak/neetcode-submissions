class Solution {
public:
    string addBinary(string a, string b) {
        int l = a.length()-1, r = b.length()-1;
        string ans="";
        int carry = 0;
        
        while (l>=0 || r>=0 || carry>0) {
            int digitA = l>=0 ? a[l]-'0' : 0;
            int digitB = r>=0 ? b[r]-'0' : 0;

            int digit = digitA+ digitB+carry;
            carry = digit / 2;
            digit = digit %2;

            ans+= digit+'0';
            r--;
            l--;
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};