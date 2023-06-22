#include <iostream>
#include <cmath>
using namespace std;

double func(double x)
{
    return (-x*x*x-cos(x));
}

double derive_func(double x)
{
    return (-3*x*x+sin(x));
}
int main()
{
    int i = 1;
    double p_0 = 0;
    while (i<=100)
    {
        double p = p_0 - func(p_0)/derive_func(p_0);
        cout << i <<": "<< p << endl;
        if (abs(p-p_0)<1e-5)
        {   
            cout << "final root: " << p;
            break;  
        }
        i++;
        p_0 = p;
    }
}