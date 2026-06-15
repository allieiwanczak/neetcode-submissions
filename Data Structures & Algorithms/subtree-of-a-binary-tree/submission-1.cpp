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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q)return true;
        else if (!p || !q) return false;
        else if (p->val != q->val) return false;
        else {
            return isSameTree(p->right, q->right)
             && isSameTree(p->left, q->left);
        }

        return true;
    }
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root && !subRoot) return true;
        else if (!root || !subRoot) return false;
        else if(isSameTree(root, subRoot)) return true;
        else return isSubtree(root->left, subRoot) || isSubtree(root->right,subRoot);
    }
};
