#include<iostream>

using namespace std;

int main()
{

    int a = 0;
    int b = 20;

    cout << "Before Swap: \n";
    cout<< "A: " << a << " & B: "<< b << endl;
    a = a ^ b;
    cout << a << endl;

    b = a ^ b;
    cout << b << endl;

    a = a ^ b;
    cout << a << endl;
    
    cout << "After Swap: \n";
    cout<< "A: " << a << " & B: "<< b << endl;

    return 0;
}