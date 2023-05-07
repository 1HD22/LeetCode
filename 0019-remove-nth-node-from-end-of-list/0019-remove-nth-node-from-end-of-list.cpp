/**
 * * Definition for singly-linked list.
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* mp = head;
        int Total=0;
        while (mp!=nullptr) {
            Total++;
            mp=mp->next;
        }
        
        mp = head;
        for (int i=0; i<Total-n-1; ++i)
            mp = mp->next;
        
        if (n == Total) {
            ListNode* temp = head->next;
            delete head;
            return temp;
        }
        
        if (mp->next == nullptr)
            ;
        
        else if (mp->next->next == nullptr) {
            delete mp->next;
            mp->next = nullptr;
        }
        else {
            ListNode* temp = mp->next->next;
            delete mp->next;
            mp->next = temp;
        }
        
        return head;
    }
};