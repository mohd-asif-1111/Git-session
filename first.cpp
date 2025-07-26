#include<iostream>
int fib(int n)
{
    if(n >= 2)
    {
	return fib(n - 1) + fib(n - 2);
    }
    if(n == 0 || n == 1)
    {
	return n;
    }
}
int main()
{
    int f = fib(5);
    std::cout << f << std::endl;
    return 0;
}
