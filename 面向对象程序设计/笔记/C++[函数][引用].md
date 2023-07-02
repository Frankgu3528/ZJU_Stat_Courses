> **函数**本身不难，但与引用，指针，重载等东西联动在一起就比较繁琐。

## [1.1]函数的默认参数
最普通的默认函数
```c
int add(int a,int b = 5,int c = 5)
{
    return a+b+c;
}
int main()
{
    cout<<add(10)<<endl;
}
```
### 关于默认参数
```c
void func2(int a,int b=10)
{
    cout<<"this is int a,int b"<<endl;
}

void func2(int a)
{
    cout<<"this is int a"<<endl;
}
```
如果你按上面写了两个函数，那么输入`func2(10)`编译器就会不知道调用哪个。
### 注意事项

1.  如果某个参数有了默认参数，那么它后面的参数也都得有默认参数。 
```cpp
int func(int a=5,int b,int c)
```

上面就是不行的，这与Python一致。~~虽然我不理解为什么要弄成这样，多不方便~~ 

2.  函数声明和函数实现只能有一个有默认参数。
（为了防止两个默认参数不一样出现问题） 
## [1.2]函数的占位参数
> 暂时还没什么用，先铺垫一下

```c
void func(int a,int)
{
	cout<"111"<<endl;
}

func(10,30);
// 调用的时候必须写个30（或者其他数字），不然就报错。
```
这样也是可以的：
```cpp
class A
{
public:
	A(int){cout << "aaa";} 
};
  
int main() {  
	A a(4);
    return 0;  
}  
```
## [1.3]函数重载
需要满足的条件：

-  在同一个作用域下 
-  函数名称相同 
-  函数的参数类型不同，或个数不同，或顺序不同 

编译器帮你选择哪个，一般来说，它会优先使用不需要类型转换的。如果你写了两个`f(float a), f(long a)`，却传入了一个int，这样会报错。
PS：无法重载仅有返回类型不同的函数
```c
void func()
{
    cout<<"11111"<<endl;
}

void func(int a)
{
    cout<<"22222"<<endl;
}

void func(int a,double b)
{
    cout<<"33333"<<endl;
}

void func(double a,int b)
{
    cout<<"44444"<<endl;
}

int main()
{
    func();
    func(3);
    func(3,3.12);
    func(4.23,2);
}
```
**输出：**
```
11111
22222
33333
44444
```
## [2.1]引用：
**引用的目的：**为了减少临时变量的copy(还没完全理解QAQ）
这个其实就是引用里面讲过的，变量用普通的，直接用10这种需要加个const。
```c
void func(int &a)
{
    cout<<"this is int &a"<<endl;
}

void func(const int &a)
{
    cout<<"this is const int &a"<<endl;
}
int main()
{
    int a = 10;
    func(a);
    func(10);
}

// out
this is int &a
this is const int &a
```
上面这是为什么呢？因为常量10是右值，而变量a是左值。
> ### 右值&左值
> - 左值就是可以取地址的变量，又分为常规左值变量和const 左值变量；
> - 右值是不可取地址的临时变量，包括常量、非引用函数返回值、表达式等；

:::success
### 四种引用

- int &ra = a;
即左值引用，只能引用左值
- const &rb1 = b;/const &rb1 = b;
即**const引用**，可引用右值和左值
- int &&rc = c;
即右值引用，只能引用右值
- const int &&rc = c;
即**const右值引用**，只能引用右值
:::
### std::move()
std::move()函数通常的解释是，将左值转变为右值。
std::move()是创建新临时变量，但原变量依然是左值的普通变量，而非临时变量。

