#include <iostream>
#include <cmath>

int main()
{
    using std::cin;
    using std::cout;
    using std::string;

    double a, b;

    cout << "a-side: ";
    cin >> a;
    cout << "b-side: ";
    cin >> b;
    double c = sqrt(pow(a, 2) + pow(b, 2));
    cout << "The hypotenuse is " << c << std::endl;

    return 0;
}