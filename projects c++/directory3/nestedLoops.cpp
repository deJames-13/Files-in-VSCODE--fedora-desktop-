#include <iostream>
#include <cmath>
// if you want to unpack all the standard objects and functions
using namespace std;

int main()
{
    for (int i = 10; i > 0; i--)
    {
        for (int j = 1; j < 10; j++)
        {
            cout << j << " loop " << i << endl;
        }
    }
    return 0;
}