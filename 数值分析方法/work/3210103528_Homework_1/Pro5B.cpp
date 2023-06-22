#include <iostream>
#include <cmath>
using namespace std;
double func2(double x)
{
    return (x*cos(x)-2*x*x+3*x-1);
}
int main()
{
    double TOL = 1e-5;
    double a = 1.2; // 1.2
    double b = 1.3; // 1.3
    double mid = 0.0;
    int i = 0;
    double FA = func2(a);
    while (i<1000)
    {   
        mid = (b+a)/2.0;
        cout << "i="<<i<<" "<<mid << endl;
        double FP = func2(mid);
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
    // cout << endl;
    // cout << "final root I get is:"<<mid;
    
}


