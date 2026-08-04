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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        if (root == nullptr) { return result; }

        queue<TreeNode*> q;
        int cnt = 0;

        q.push(root);

        while (!q.empty()) {
            TreeNode* rightSide = nullptr;
            cnt = q.size();

            for (int i = 0; i < cnt; ++i) {
                TreeNode* cur = q.front();
                q.pop();
                if (cur) {
                    rightSide = cur;
                    q.push(cur->left);
                    q.push(cur->right);
                }
            }
            if (rightSide) {
                result.push_back(rightSide->val);
            }
        }
        return result;
    }
};
