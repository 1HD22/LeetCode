class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int total = 0;
        int j = mat.size() - 1;
        
        for (int i = 0; i < mat.size(); i++)
        {
            total += mat[i][i];
            
            if (i != j)
            {
                total += mat[j][i];
            }
            j--;
        }
        
        return total;
    }
};


            