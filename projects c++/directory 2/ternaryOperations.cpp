#include <iostream>
#include <cmath>
// if you want to unpack all the standard objects and functions
using namespace std;

int main()
{
    // ternary operators are replacements to if/else statements
    // condition ? exp1 : exp 2
    // if ? then do this : else do this

    int lessThanHundred;
    cout << "Enter a number: ";
    cin >> lessThanHundred;
    lessThanHundred < 100 ? cout << "This is less than a hundred" << endl : cout << endl;

    return 0;
}