### 为什么要有模板？
> 比如在c++里要写一个交换函数，因为声明函数的时候要写明传进去变量的数据类型，所以如果想写一个能交换所有数据类型的函数就异常麻烦，（~~Python里很方便~~）, 所以我们引入**模板**的概念，用来泛化的代替未定的数据类型。

# 函数模板
### 函数模板语法
```cpp
#include <iostream>
using namespace std;

template <class T> // 这里用class和typename都是可以的，推荐都用前者。
void swag(T&a,T&b)
{
    T temp = a;
    a = b;
    b = temp;
}
int main()
{
    int a = 10;
    int b = 5;
    swag(a,b);
    cout<<a<<endl;
    cout<<b<<endl;
}
```
上面有个大坑，就是我一开始函数名叫swap，然后一直报错。后来经过高人指点，发现std中对swap已经进行了定义，这里就重复了所以报错，所以尽量不要一下就整个把std扔进来or使用奇怪一点的函数名字。
### 函数模板注意事项

- 自动推导类型，必须推到出一致的数据类型才能使用 (下面是个反例）
```cpp
int a = 10;
char c = 'A';
swag(a,c);
```
但C++也有一个**隐式类型转换**的功能。如下面：编译器把‘c’转换成了它的ASCII码99代入运算。
```python
int addnum(int a,int b)
{
    return a+b;
}

int main()
{
    int a = 10;
    char c = 'c';
    cout << addnum(a,c) << endl;
}

// output : 109
```
当时用函数模板时，自动类型推导是不会发生隐式类型转换的，而显示指定类型`addnum<int>(a,b)`可以。
**普通函数和函数模板的调用规则：**

- 如果函数模板和普通函数都可以实现，优先调用普通函数。
- 如果函数模板和普通函数都可以实现，可以听过空模板参数列表，强制调用函数模板
```python
void myprint(int a ,int b)
{
    cout << "普通函数" << endl;
}

template <class T>
void myprint(T a,T b)
{
    cout << "模板调用" << endl;
}
int main()
{
    myprint<>(10,20); // 加不加尖括号是两种输出
}
```
## 类模板
### 基本语法
```python
template <class T1,class T2>
class Person
{
public:
    T1 name;
    T2 age;

    Person(T1 mname,T2 mage)
    {
        name = mname;
        age = mage;
    }
};
int main()
{
    Person<string,int> P("frank",19);
    cout << P.name <<endl;
    cout << P.age <<endl;
}
```
### 类模板与函数模板区别

1. 类模板没有自动类型推导的方式（函数模板可以让编译器自动推导或者显式指定）
2. 在模板参数列表可以有默认参数。
```python
template <class T1,class T2=int>
class Person
{
    // code 
};
```
### 特例化的模板
编译器匹配的顺序：

1. 完全匹配的非模板函数（非模板函数优先级最高）。
2. 特例化的模板。如果有与特定类型或特定模板参数完全匹配的特例化模板，将优先使用特例化模板的实现。
3. 通用模板。如果没有特例化的模板或特例化模板无法匹配，编译器将使用通用模板进行实例化。
```cpp
void print(const T &value) {  
    std::cout << "General template: " << value << std::endl;  
}  
  
template <>  
void print<int>(const int &value) {  
    std::cout << "Specialized template for int: " << value << std::endl;  
}  
int main() {  
	print(3.3);
	print(4);
}

//out
General template: 3.3
Specialized template for int: 4
```
