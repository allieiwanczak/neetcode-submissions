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
private:
public:
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        if (!head) return nullptr;
        ListNode* curr = head;

        while (curr->next != nullptr) {
            ListNode* newNode = new ListNode(gcd(curr->val, curr->next->val), curr->next);
            curr->next = newNode;
            curr=curr->next->next;
        }
        return head;
    }
};