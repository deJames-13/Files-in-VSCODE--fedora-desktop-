#include <iostream>
#include <cmath>

int main()
{
    double x = 2;
    double y = 3;
    double z = 4;
    double p;
    // max, min
    // p = std::max(x, y, z);
    // p = std::min(x, y, z);
    // power
    p = pow(x, z);
    // sqrt
    p = sqrt(9);
    // absolute
    p = abs(-10);
    // round
    p = round(129.3);
    // ceiling
    p = ceil(129.3);
    // floor
    p = floor(129.6);

    return 0;
}