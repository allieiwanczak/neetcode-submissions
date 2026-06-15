/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    int dfs(TreeNode* root, int maxV) {
        if (!root) return 0;

        int res = (root->val >= maxV) ? 1 : 0;
        maxV = max(maxV, root->val);
        res+=dfs(root->right, maxV);
        res+=dfs(root->left, maxV);

        return res;
    }
public:
    int goodNodes(TreeNode* root) {
        return dfs(root, root->val);
    }
};
