#include <iostream>
#include <cmath>
// if you want to unpack all the standard objects and functions
using namespace std;

int main()
{
    string myString = "abcdefg";
    cout << myString << endl;
    cout << myString.length() << endl;
    cout << myString[1] << endl;
    cout << myString.find('g') << endl;
    // string splicing
    cout << myString.substr(0, 3) << endl;
    cout << myString.empty() << endl;
    myString.clear();
    myString.append("newStringsAdded");
    myString.insert(0, "1");
    myString.erase(0, 10);
    cout << myString << endl;

    return 0;
}