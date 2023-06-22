#include <iostream>
#include <cmath>
using namespace std;

double func(double x)
{   
    double t = exp(x)-x*x+3.0*x-2.0;
    return (t);
}
int main()
{
    double TOL = 1e-5;
    double a = 0.0;
    double b = 1.0;
    double mid = 0.0;
    int i = 0;
    double FA = func(a);
    while (i<1000)
    {   
        mid = (b+a)/2.0;
        cout << "i="<<i<<" "<<mid << endl;
        double FP = func(mid);
        if (FP==0.0 || (b-a)/2.0<TOL)
        {
            cout << mid;
            break;
        }
        i+=1;   
        if (FA*FP>0)
        {
            a = mid;
            FA = FP;
        } 
        else
            b = mid;
    }
    // cout << mid << endl;
    // cout << i;
    
}