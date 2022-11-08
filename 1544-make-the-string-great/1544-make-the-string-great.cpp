class Solution {
public:
    bool isbad(char x, char y) {
        if ((x - y == 32 ) || (x - y == -32))
            return true;
        return false;
    }
    string makeGood(string s) {
        int i = 0;
        int t = s.length() - 1;
        
        while (i < t)
        {
            if (isbad(s[i],s[i+1]))
            {
                s.erase(i,2);
                i = -1;
                t -= 2;
            }
            i++;
        }
                 
        return s;
        
    }
};
