/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* next;
        for (ListNode* trav=head; trav != nullptr;) {
            cout << trav->val;
            next = trav->next;
            trav->next = prev;
            prev = trav; 
            trav = next;
            //if (prev) { cout << prev->val << endl ; }
            //if (trav && prev) { cout << ' ' << prev->val << ' ' << trav->val << endl; }
        }
        return prev;
    }
};
