#include <iostream>
#include <cmath>
using namespace std;
double func(double x)
{
    return (-sqrt(exp(x)/3));
}
int main()
{
    int i = 1;
    double TOL = 0.01;
    double p0 = -1.0;
    double p;
    while (i<1000)
    {
        p = func(p0);
        cout << "p"<<i<<" = "<<p<< endl;
        if (abs(p-p0)<TOL)
        {
            cout << p << endl;
            break;
        }
        i+=1;
        p0 = p;
    }
    cout << i;
}