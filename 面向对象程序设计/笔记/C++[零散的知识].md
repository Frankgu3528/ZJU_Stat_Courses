### 条件运算符 ? :
`Condition ? X : Y`
如果 Condition 为真 ? 则值为 X : 否则值为 Y。
```cpp
if(y < 10){ 
    var = 30;
}else{
    var = 40;
}

// 等价于
var = (y < 10) ? 30 : 40;
```
### 文件处理
文件包含实际上是将被包含的文件在代码中展开。经典例子是包含头文件。其语法是：
#include <_FILE_NAME_>          在系统库中寻找文件
#include "_FILE_NAME_"            现在当前工作目录中寻找文件，找不到再去系统库寻
### return;
`return;`用在void函数中，类似循环中的`break;`,相当于在这个点结束这个函数。
```cpp
int a[10];
void func()
{
   a[1] = 1;
   return;
   a[2] = 2;
}
int main()
{  
   func();
   cout << a[0] <<endl;
   cout << a[1] <<endl;
   cout << a[2] <<endl;
}

//输出：
0
1
0
```
### 内存四区
[[c++]内存四区](https://www.yuque.com/docs/share/c406eaa9-a520-4e37-ba35-8f23527ee100?view=doc_embed)
### 数组初始化
C语言规定，普通数组没有赋初值，默认的数组元素值是随机数，不是0。
如果在定义数组时，数据类型前面加上关键字`static`，数组变成了**静态数组**；或者把数组定义在函数的外面，成为**全局变量数组**，这时数组元素的值自动赋值为0。
### INT_MAX和INT_MIN
INT_MAX = 2^31-1，INT_MIN= -2^31.
可以看出是一个相当大的数和一个相当小的数，如果想要得到数组中最小值，可以先将最小值赋值为INT_MAX ；同理如果想要得到数组中最大值，可以先将最大值赋值为INT_MIN ；
### string-->int
```java
string s = "123";
int num = atoi(s.c_str());
```
### 奇怪的写法
C++11除了使用 `for (int i = 0; i < v.size(); i++) sum += v[i];`的方式遍历以外，还可以这样写：`for (auto a : v) sum += a;`。
在做 LeetCode 的绝大多数场景下，我们可以使用`for (auto &a : v)`，加上一个引用。加上这个引用后就不会在遍历的过程中每次循环都构造一个临时变量，在遍历二维`vector`的时候尤为有意义。当然加上引用后对这个变量`a`做的改动会真实地影响到`vector v`。
![来自xyx](https://cdn.nlark.com/yuque/0/2022/jpeg/641515/1664503066712-6d6aa131-3cb0-4dfb-b53e-aec90bc84cbf.jpeg#averageHue=%23f6f4f3&from=url&height=369&id=K4gzn&originHeight=492&originWidth=807&originalType=binary&ratio=1&rotation=0&showTitle=true&status=done&style=none&title=%E6%9D%A5%E8%87%AAxyx&width=605 "来自xyx")
### pair
pair 可以将两个不必相同的类型攒起来，例如`pair<int, int> p1;`或者`pair<int, string> p2;`
```
pair<int,double> p{1,1.11};
cout << p.first <<" "<< p.second;
```
### struct 的构造函数
这个其实跟class的member initializer lists是一样的
![image.png](https://cdn.nlark.com/yuque/0/2022/png/26249904/1664800906802-fc3e67da-dc3a-4e81-a13e-f089e274bd12.png#averageHue=%23849689&clientId=u0c1edd40-85b2-4&from=paste&height=327&id=u42609148&originHeight=715&originWidth=1747&originalType=binary&ratio=1&rotation=0&showTitle=false&size=106253&status=done&style=none&taskId=u60dc64ce-29b4-4451-a6e8-3edea17a18f&title=&width=798.6285714285714)
### double&float
在C++中，浮点数字面值默认被解释为**`double`**类型。这意味着，如果你传入的值为**`5.6`**，编译器会将其视为**`double`**类型。
如果你希望将其解释为**`float`**类型，可以在数字后面添加后缀**`f`**或**`F`**，表示这是一个**`float`**类型的字面值。例如，使用**`5.6f`**或**`5.6F`**来明确指定值的类型为**`float`**。
### using
```cpp
using myInt = int;  
myInt x = 5;  // 使用 myInt 作为 int 的别名  
std::cout << x;
```
### 指针常量和常量指针
```c
int num = 10;  
int* const ptr = &num; // const 指针，指针本身是常量  
*ptr = 20; // 可以修改指针指向的内容  
// ptr = &anotherNum; // 错误，不能修改指针本身的值  
```
```c
int num = 10;  
const int* ptr = &num; // 指向常量的指针，指向的内容是常量  
// *ptr = 20; // 错误，不能修改指针指向的内容  
ptr = &anotherNum; // 可以修改指针指向的变量  
```
### explicit
在构造函数前面加上explicit可以防止隐式类型转换。
```cpp
class Foo {
public:
    explicit Foo(int i) {}
};

class Bar {
public:
    Bar(int i) {}
};

void foo(Foo f);
void bar(Bar b);

int main() {
    Foo f = Foo(1); // OK, explicit conversion
    Foo g = 1;      // Error: no valid conversion
    foo(1);         // Error: no valid conversion
    Bar b = Bar(1); // OK, explicit conversion
    Bar c = 1;      // OK, implicit conversion
    bar(1);         // OK, implicit conversion
}
```
```cpp
class Foo {
public:
    explicit Foo(int i) {cout <<"c";}
	Foo (double t)
	{
		cout << "ddd";
	}
};


int main() {
	Foo c = 10;
}
// out 
ddd
```
### extern
通过在变量的声明前加上 **`extern`** 关键字，可以将变量声明为一个外部变量。这表示该变量是在其他源文件中定义的，这样在当前源文件中可以使用该变量而无需重新定义。
```cpp
#ifndef FILE1_H  
#define FILE1_H  
  
extern int globalVariable;   // 外部变量的声明  
  
void externalFunction();    // 外部函数的声明  
  
#endif // FILE1_H  
```
```cpp
#include "file1.h"  
  
int main() {  
    externalFunction();  // 调用外部函数  
    return 0;  
}  
```
```cpp
#include "file1.h"  
  
int globalVariable = 10;   // 外部变量的定义  
  
void externalFunction() {  
    // 外部函数的定义  
}  
```
### static

1. 声明为静态变量，在整个程序声明周期中只会分配一次内存，所以能保留上一次的值。所以在多个函数中共享数据很方便。
2. 静态函数：在类中声明的成员函数可以使用 **`static`** 关键字来定义为静态函数。静态函数与类的实例无关，可以直接通过类名调用，而无需创建对象。静态函数没有隐含的 **`this`** 指针，因此不能访问非静态成员变量和非静态成员函数，只能访问其他静态成员。
3. 静态类成员变量：在类中声明的成员变量可以使用 **`static`** 关键字来定义为静态成员变量。一个静态成员变量在所有类的实例之间是共享的，只需要分配一份内存。可以通过类名和作用域运算符直接访问静态成员变量，而无需创建类的实例。
```cpp
void myFunction() {  
    static int count = 0;   // 静态变量，会保留上一次的值  
    count++;  
    std::cout << "Count: " << count << std::endl;  
}  
int main() {  
    myFunction();   // 输出：Count: 1  
    myFunction();   // 输出：Count: 2  
}
```
其实这也也是上面的效果：
```cpp
int count = 0;  
void myFunction() {  
    count++;  
    std::cout << "Count: " << count << std::endl;  
}  
int main() {  
    myFunction();   // 输出：Count: 1  
    myFunction();   // 输出：Count: 2  
}
```
### a++和++a
这两个都能让a的值+1（所以在写一个`for (int i=1;i<=n;i++)`中i++和++i是完全一样的。
但是（++a）这个值是新的值，（a++）这个值是老的值。
```cpp
int a=0;int b = 0;
int c = a++;int d= ++b;
cout << a << "  " << b <<endl;
cout << c << "  " << d <<endl;

// out 
1  1
0  1
```
### 变量初始化
第一行其实只是对b初始化为0，第二行把a,b都初始化为0了。
```cpp
int a,b=0;
int a=0,b=0;
```
