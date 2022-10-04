#include <iostream>
#include <cmath>
// if you want to unpack all the standard objects and functions
using namespace std;

int main()
{
    // while(condition){do something}
    int x = 0;
    while (x < 10)
    {
        cout << x << endl;
        x++;
    }
    cout << "Done";
    // do while loops
    int p;
    do
    {
        cout << "\nEnter a positive num: ";
        cin >> p;
    } while (p < 0);
    cout << "this is a # " << p << endl;

    return 0;
}