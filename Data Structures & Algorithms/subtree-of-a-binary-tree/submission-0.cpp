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
public:
    //TreeNode* test = new TreeNode(2, new TreeNode(4, new TreeNode(6), nullptr), new TreeNode(5));
    
    bool nodeEquality(TreeNode* root, TreeNode* subRoot) {
        if (subRoot == nullptr && root == nullptr) { return true; }
        if (!subRoot || !root) { return false; }
        if (root->val != subRoot->val) { return false; }
        return nodeEquality(root->left, subRoot->left) && nodeEquality(root->right, subRoot->right);
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if (!root) { return false; }
        if (nodeEquality(root, subRoot)) { return true; }
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};
