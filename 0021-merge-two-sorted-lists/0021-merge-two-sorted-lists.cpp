/***
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
    void insert(ListNode* list1, ListNode* list2) {
        list1->next = new ListNode(list2->val, list1->next);
        return;  
    }
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        if (list1 == nullptr && list2 == nullptr)
            return nullptr;
        
        int valOne = 101;
        int valTwo = 101;
        
        ListNode* mp1 = list1;
        ListNode* mp2 = list2;
        
        if (list1 != nullptr) {
        valOne = list1->val;
        }
        
        if (list2 != nullptr) {
        valTwo = list2->val;
        }
        
        ListNode* result = new ListNode(valOne < valTwo? valOne: valTwo);
        ListNode* mpFinal = result;
        
        if (valOne < valTwo) {
            if (mp1 != nullptr)
            mp1 = mp1->next;
        }
        else { 
            if (mp2 != nullptr)
            mp2 = mp2->next;
        }
        
        while (mp1 != nullptr && mp2 !=nullptr) {
            if (mp1->val > mp2->val) {
                mpFinal->next = mp2;
                mpFinal = mpFinal->next;
                mp2 = mp2->next;
            }
            else {
                mpFinal->next = mp1;
                mpFinal = mpFinal->next;
                mp1 = mp1->next;
            }
        }
        
        while (mp1 != nullptr) {
            mpFinal->next = mp1;
            mpFinal = mpFinal->next;
            mp1 = mp1->next;
        }
        
        while (mp2 != nullptr) {
            mpFinal->next = mp2;
            mpFinal = mpFinal->next;
            mp2 = mp2->next;
        }
        
        return result;
    }
};