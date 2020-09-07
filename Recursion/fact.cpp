#include<iostream>

using namespace std;

int factorial(int x)
{
    cout << "I am calculating F("<<x<<")"<< endl;
    if(x == 0)
    {
        return 1;
    }
        return x * factorial(x-1);
}

int recursiceFibo(int n)
{
    if(n <= 1)
    {
        return n;
    }else {
        return recursiceFibo(n-1) + recursiceFibo(n-2);
    }
    
}


int main()
{
    int n;
    cout << "Give a number to calculate the factorial: ";
    cin >> n;
    int result = recursiceFibo(n);
    cout << result << endl;
    return 0;
}