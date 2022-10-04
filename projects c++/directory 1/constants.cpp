#include <iostream>

int main()
{
    double pi = 3.14;
    double radius = 10;
    double circ = 2 * pi * radius;

    // constants
    // are immutable datatypes, they cannot be change
    // ver useful
    const double PI = 3.14;
    double newcirc = 2 * PI * radius;

    std::cout << newcirc << "cm";
    return 0;
}