
class Solution {
public:
    double func(double x, int c) {
        double y = x * x;
        return (y - c)/(2 * x);
    }
    int mySqrt(int x) {
        int count = 0;
        double i = 1;
        double previ = 1;
        while (count < 3)
        {
            previ = i;
            i = i - func(i,x);
            
            /*the square root cannot be negative*/
            if (i < 0)
            continue;

            /*prevents equal value infinte loops*/
            if (i == previ & i * i != x)
            i++;

            /*main evaluation*/
            if (static_cast<int>(i) == static_cast<int>(previ))
            count++;

        }
        return static_cast<int>(i);

    };
};