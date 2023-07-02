> C++和Python同为面向对象语言，相比c等很重要的一点就是引入了面向对象的概念。当然正式的面向对象是下学期的课，这里只是针对数据结构的要求佛系的写一点。

## [0.0]关于类&对象的概念
比如人这个东西，每个人都有身高，体重等特性，就可以抽象成一个具体的类（class），身高，体重就是类的属性。
## [1]构造函数

-  没有返回值，不用写void 
-  函数名与类名相同 
-  构造函数可以有参数，可以发生重载 
- 如果一个类定义了带有参数的构造函数（例如`**A(int a){}**`），那么编译器就不会为该类提供默认的无参构造函数,，所以这时候再`A a;`想创建一个对象会报错。
-  创建对象的时候，构造函数会自动调用，而且只调用一次
（如果不自己写构造函数，编译器也会写一个，但里面啥也没有） 
- 可以通过 = default; 或者 = delete; 控制让编译器产不产生一个默认的构造函数。
```cpp
class A
{
public:
	A(){cout << "AA";}
};

int main()
{	
    A a;
	A a = A();
    A a();
	return 0;
}
```
在上面的例子里，第一和第二都能创建A的对象，并输出AA；而第三行其实被编译器理解为一个声明了一个返回值为A，名字为a的函数而已。
### [1.1]拷贝构造函数
**拷贝构造函数**是一种特殊的构造函数，它在创建对象时，是使用同一类中之前创建的对象来初始化新创建的对象。拷贝构造函数通常用于：

- 通过使用另一个同类型的对象来初始化新创建的对象。
- 复制对象把它作为参数传递给函数。
- 复制对象，并从函数返回这个对象。

下面是一个写法，其实有好多种写法，选一个就可以啦。
```cpp
class Person
{
public: 
    int m_age;
    //含参构造函数
    Person(int age)
    {
        m_age = age;
    }
    //拷贝构造函数
    Person(const Person &p)
    {
        m_age = p.m_age;
    }

    ~Person()
    {
        cout<<"这是析构函数"<<endl;
    }
};

int main()
{
    Person P1(10);
    Person P2(P1);
    cout<<P2.m_age<<endl;

}
```
### [1.2]member initializer lists
```cpp
class Point {
    int x, y;
public:
    Point(int x, int y) : x(x), y(y) {}
};
```
相当于：
```cpp
class Point {
    int x, y;
public:
	Point(int x,int y){
		this->x = x;
		this->y = y;
	}
};

```
### [1.3]委托构造函数（delegating constructor）
```cpp
class MyClass {  
public:  
    MyClass() : MyClass(0, 0) {cout <<"111"<<endl;}  // 委托构造函数  
  
    MyClass(int a, int b) : x(a), y(b) {  
        cout << "222"<<endl;
    }  
  
private:  
    int x;  
    int y;  
};  
  
int main() {  
    MyClass obj1;           // 调用 MyCLass() 构造函数  
    MyClass obj2(10, 20);   // 调用 MyClass(int a, int b) 构造函数  
  
    return 0;  
}  

//out 
222
111
222
```
## [2]析构函数
与构造函数一样，析构函数也是一种特殊的函数。构造函数在实例化对象时被调用，而析构函数 在对象销毁时自动被调用。
```cpp
class Human 
{ 
    public: 
    ~Human() 
    { 
        // destructor code here 
    } 
};
```
每当对象不再在作用域内或通过 delete 被删除进而被销毁时，都将调用析构函数。这使得析构函 数成为重置变量以及**释放动态分配的内存和其他资源**的理想场所.
```cpp
    // 构造函数
    Birds()
    {
        cout<<"here comes a bird"<<endl;
        name = new char [256];
        name[0] = 'G';
        name[1] = 'G';
        name[2] = 'F';
    }
   
    // 惨叫函数
    ~Birds()
    {
        cout<<"I am dying"<<endl;
        delete [] name;	//回收内存，不然会有泄露
    }
};
```
## [3]封装权限

-  public 类内类外皆可以 
-  protected 只有类内可以 
-  private 只有类内可以 

（后两个的区别是private的东西子类不能用，protected 子类可以）
### [3.1]struct和class的区别
(感觉struct能干的class都能干……所以cpp用class更多吧（我猜））
struct默认是public权限，class默认是private权限
```cpp
#include <iostream>
#include <string>
using namespace std;
class Human 
{
    int a = 0;
};

struct People
{
    int b = 0;
};
int main(){
    // Human H1;
    // cout<<H1.a<<endl;
    // 这里就会报错
    
    People P1;
    cout<<P1.b<<endl;
    return 0;
}
```
## 继承&多态

- 如果基类指针/引用指向基类，那就正常调用基类的相关成员函数 
- 如果基类指针指向派生类，则调用的时候会调用派生类的成员函数 
- 派生类指针不能指向基类  
```cpp
class A{
public:
    virtual void foo(){
    cout<<"A"<<endl;
}
};
class B : public A{
public:
    virtual void foo(){
    cout<<"B"<<endl;
}
};
int main()
{
    A *a=new B;
    a->foo(); //结果为B
    return 0;
}
```
上面这个写法其实有点不符合我的风格, 其实跟这个是一样的：
```cpp
int main()
{
    B b;
    A *a = &b;
    a->foo();
    return 0;
}
```
当**`foo`**函数被调用时，若基类A，B有默认参数值，会用A的。即使在运行时，实际执行的是派生类B的函数体，但默认参数值仍然来自于基类A。
### 继承顺序
```cpp
class A
{
public:
    A(){cout <<"A()"<<endl;}
    ~A(){cout <<"~A()"<<endl;}
};

class B : public A
{
public:
    B(){cout <<"B()"<<endl;}
    ~B(){cout <<"~B()"<<endl;}
};
int main() {
    A a;
    B b;
}

// out
A()
A()
B()
~B()
~A()
~A()
```
## [4]this 指针
在 C++ 中，每一个对象都能通过 this 指针来访问自己的地址。this 指针是所有成员函数的隐含参数。因此，在成员函数内部，它可以用来指向调用对象。
在 C++中，一个重要的概念是保留的关键字 this。在类中，关键字 this 包含当前对象的地址，换句话说，其值为&object。当您在类成员方法中调用其他成员方法时，编译器将隐式地传递 this 指针—函数调用中不可见的参数。
```cpp
class Human 
{ 
private: 
 void Talk (string Statement) 
 { 
 9.8 将 sizeof( )用于类 173
 cout << Statement; 
 } 
public: 
 void IntroduceSelf() 
 { 
 Talk("Bla bla"); // same as Talk(this, "Bla Bla") 
 } 
}; 
```
在这里，方法 IntroduceSelf( )使用私有成员 Talk( )在屏幕上显示一句话。实际上，编译器将在调用Talk 时嵌入 this 指针，即 Talk(this, “Bla Bla”)。
** 从编程的角度看，this 的用途不多，且大多数情况下都是可选的。  **~~好勒，知道这句话就行了~~
## [5]访问对象属性的方法
可以通过两种写法（直接/指针），个人明显喜欢第一种
```cpp
class Building
{
public:
   int ant  = 10;
};

void test1(Building *build)
{
   cout<<build->ant<<endl;
}

void test2(Building build2)
{
   cout<<build2.ant<<endl;
}
int main()
{
   Building build;
   test1(&build);

   Building build2;
   test2(build);
}

输出：
10
10
```
## [6] 友元
> 友元的作用用来访问类内的private和protected属性的东西。

e.g. 类是一个房子，别人能进来玩，但仅限于客厅这种public的地方（因为你的卧室是private）。但如果是你的好基友，你可以把他设为friend，这样他也能进来了。

- 全局函数做友元
- 类做友元
- 成员函数做友元
### [6.1] 全局函数做友元
```cpp
class Building 
{
    friend void goodgay(Building build);//不加这行就不行了
private:
    int bedroom = 10;
public:
    int living = 20;
};

void goodgay(Building build)
{
    cout << build.bedroom <<endl;
}

int main()
{
    Building build;
    goodgay(build);
}
```
### [6.2] 类做友元
:::success
这里有个点：很多时候我们对于成员函数，都采用类内声明，类外实现的方法。
即类内只写一个函数声明，在类外用`::`作用域解析符写实现。
:::
```cpp
class Buiding
{
friend class goodgay; // 就是这行！
};
class goodgay
{
/……
};
```
上面通过在Building 类中声明`friend class goodgay;`, 就可以在goodgay类中访问Building类的私有和共有属性了。
### [6.3] 成员函数做友元
通过友元技术让Goodgay 中的成员函数visit(）可以访问Building中的私有属性。
```python
class Building
{
    friend void Goodgay::visit();
};
```
## [7]new&delete
new 表达式是 **唯一** 的用来创建动态生命周期对象的方式（因为 malloc 只是开辟内存，并不创建对象)
果 p 在 new 的时候创建的是单个对象，则应该用 delete p; 的形式 (single-object delete expression) 回收；如果 p 在 new 的时候创建的是数组，则应该用 delete[] p; (array delete expression) 的形式回收.
## [8]类型转换符函数
格式：`operator xxx() {return aaa;}`
```cpp
class MyNumber {  
private:  
    int value;  
public:  
    MyNumber(int val) : value(val) {}  
  
    operator int() {  
        return value; // 将自定义类型 MyNumber 转换为 int 类型  
    }  
};  
  
int main() {  
    MyNumber num(42);  
    int x = num; // 隐式调用 MyNumber 类的类型转换符函数将 num 转换为 int 类型  
    std::cout << x << std::endl; // 输出: 42  
    return 0;  
}
```
## 杂七杂八
### const
```c
class A
{
private:
	int a = 10;	
public:
	void sss(){a = a-1;cout<<a;}
	void aaa() const
	{
		a = a-1;
	}
};
```
const修饰成员函数，这样这个函数不能更改里面的变量。（aaa函数会报错）
下面是const修饰对象，这样这个常量对象只能调用常量成员函数。
```cpp
class MyClass {  
private:  
    int value;  
public:  
    MyClass(int num) : value(num) {}  
      
    // 非常量成员函数  
    void setValue(int num) const{  
       cout << "hh";
    }  
      
    // 常量成员函数  
    int getValue() const {  
        return value;  
    }  
};  
  
int main() {  
    const MyClass obj(10); // 常量对象  
      
    obj.setValue(20); // 错误，不能在常量对象上调用非常量成员函数  
      
    int val = obj.getValue(); // 可以在常量对象上调用常量成员函数  
      
    return 0;  
}
```
 构成重载关系的时候，const类型的对象只能调用const类型的成员函数，不 能调用non-const，而非const类型的对象优先调用non-const的成员函数， 如果没有non-const再调用const类型的  
```c
class A 
{
public:
    void foo() {
    cout << "A::foo();" << endl;
	}
    void foo() const {
    cout << "A::foo() const;" << endl;
	}
};
int main()
{
    A a;
    a.foo(); //访问的是非const类型的foo
    const A aa;
    aa.foo(); //访问的是const类型的foo
    return 0;
}
```
