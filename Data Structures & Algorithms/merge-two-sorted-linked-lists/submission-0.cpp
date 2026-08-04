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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (!list1 && list2) { return list2; } 
        else if (list1 && !list2) { return list1; }
        else if (!list1 && !list2) {return nullptr; } 

        ListNode* a{list1};
        ListNode* b(list2);
        ListNode* c = (a->val <= b->val) ? a : b;
        if (a->val <= b->val) { a = a->next; }
        else { b = b->next; }

        ListNode* start{c};
        while (a && b) {
            if (a->val <= b->val) {
                c->next = a;
                c = c->next;
                a = a->next;
            }
            else {
                c->next = b;
                c = c->next;
                b = b->next;
            }
        }

        while (a) {
            c->next = a;
            c = c->next;
            a = a->next;
        }

        while (b) {
            c->next = b;
            c = c->next;
            b = b->next;
        }

        return start;
    }
};
