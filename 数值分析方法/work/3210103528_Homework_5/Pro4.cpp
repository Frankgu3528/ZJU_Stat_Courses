#include<iostream>
#include<cmath>
using namespace std;

// 四道题的函数写在一起了
// double fn(double x){
//     return pow(cos(x),2);
// }
double fn(double x){
    return x*log(x+1);
}
// double fn(double x){
//     return pow(sin(x),2)-2*x*sin(x)+1;
// }
// double fn(double x){
//     return 1/(log(x)*x);
// }
int main(){
    double R33,R32,R31,R22,R21,R11;
    double h;
    double a,b;
    a=-0.75,b=0.75; // 上下限
    h=b-a;
    R11=(h/2)*(fn(a)+fn(b));
    R21=(h/4)*(fn(a)+2*fn(a+h/2)+fn(b));
    R31=(h/8)*(fn(a)+2*(fn(a+h/4)+fn(a+h/2)+fn(a+3*h/4))+fn(b));
    R32=R31+(R31-R21)/3;
    R22=R21+(R21-R11)/3;
    R33=R32+(R32-R22)/15;
    cout << R33 << endl;
}