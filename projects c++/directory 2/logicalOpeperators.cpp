#include <iostream>
#include <cmath>
// if you want to unpack all the standard objects and functions
using namespace std;

int main()
{
    // && and, checks if multiple conditions are true
    // || or, if one of the operations are true
    // ! not, reverses the boolean state of a datatype
    int x;
    cin >> x;
    x > 0 && x < 10 ? cout << "This is a number between 0 and 10" << endl : cout << endl;

    x > 0 || x < 10 ? cout << "This is a number either greater than 0 or less than 10" << endl : cout << endl;

    return 0;
}