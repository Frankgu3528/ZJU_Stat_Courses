#include<iostream>
#include<cmath>
using namespace std;
//use Eluer's method to approximate the solution for each of the following initial conditions value

double fn(double t,double w){
    return w/t-pow(w/t,2);
}

int main(){
    double w=1;
    double n=10;
    double h=0.1;
    double t=1;
    for(int i=0;i<n;i++){
        w=w+h*fn(t,w);
        t=t+h;
    }
    cout << w << endl;
}