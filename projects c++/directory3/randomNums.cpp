#include <iostream>
#include <ctime>
// if you want to unpack all the standard objects and functions
using namespace std;

int main()
{
    // pseudo-random
    srand(time(NULL));
    int num = (rand() % 100) + 1;
    cout << num << endl;
    return 0;
}