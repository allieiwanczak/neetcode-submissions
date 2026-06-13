class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int l1 = 0, l2 = 0, r1=word1.length(), r2=word2.length();
        string ans = "";

        while (l1<r1 && l2<r2) {
            ans+=word1[l1];
            ans+=word2[l2];
            l1++; l2++;
        }
        while (l1<r1) {
            ans+=word1[l1];
            l1++;
        }
        while (l2<r2) {
            ans+=word2[l2];
            l2++;
        }
        return ans;
    }
};