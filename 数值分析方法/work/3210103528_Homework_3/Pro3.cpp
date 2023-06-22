#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
 
const int N = 1e2+10;
const double eps = 1e-8;
int n;
double a[N][N];  //存储线性方程组
int main()
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i ++ )
        for (int j = 1; j <= n + 1; j ++ )
            scanf("%lf", &a[i][j]);
 
    int r=1,c=1;//定义变量行与列
   
    for(r,c;c<=n;c++){ //枚举列。
        
        int t=r;
        //找这一列绝对值最大的一行
        for(int i=r;i<=n;i++){
            if(fabs(a[i][c])>fabs(a[t][c]))
                t=i;
        }
        
        //如果这一列都为0则考虑下一列
        if(fabs(a[t][c])==0)continue;
        
        //交换两行
        for(int i=c;i<=n+1;i++)swap(a[t][i],a[r][i]);
        
        // 将当前行的首位变成1
        for (int i = n+1; i >= c; i -- ) a[r][i] /= a[r][c];
        
        // 用当前行将下面所有的列消成0，注意当前行第一个数为1
        for (int i = r + 1; i <= n; i ++ )  
            if (fabs(a[i][c]) !=0) //不为0则消成0
                for (int j = n+1; j >= c; j -- ) 
                    a[i][j] -= a[r][j] * a[i][c];
        r++;
    }
    
    //转化为最简型
    for (int i = n-1 ; i >= 1; i -- )
        for (int j = i + 1; j <= n; j ++ )
            a[i][n+1] -= a[i][j] * a[j][n+1];
            
     for (int i = 1; i <= n; i ++ )
        {
            if (fabs(a[i][n+1]) < eps) a[i][n+1] = 0;//小于eps即为0；
            // printf("%.2lf\n", a[i][n+1]);
            cout << a[i][n+1]<<" ";
        }
    
}