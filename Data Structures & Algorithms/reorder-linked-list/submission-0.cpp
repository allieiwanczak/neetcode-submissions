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
    void reorderList(ListNode* head) {
        ListNode* fast = head->next;
        ListNode* slow = head;

        while (fast != nullptr && fast->next != nullptr) {
            fast = fast->next->next;
            slow = slow->next;
        }

        ListNode* curr = slow->next;
        ListNode* prev = slow->next = nullptr;
        while (curr!= nullptr) {
            ListNode* temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        ListNode* first = head;
        curr = prev;
        while (curr!= nullptr) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = curr->next;

            first->next = curr;
            curr->next = temp1;
            first = temp1;
            curr = temp2;
        }
    }
};
