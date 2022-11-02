#include <cstring>

class Solution {
public:
    bool isPalindrome(int x) {
        string pal = to_string(x);
        
        for (int i = 0; i < pal.length() / 2; i++)
        {
            int j = pal.length() - i - 1;
            if (pal[i] == pal[j])
                continue;
            else
                return false;
        }
        
        return true;
    }
};
