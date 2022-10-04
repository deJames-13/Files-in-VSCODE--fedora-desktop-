#include <iostream>

int main()
{
    int age;
    std::cin >> age;
    if (18 <= age < 100)
    {
        std::cout << "Welcome!";
    }
    else if (age >= 100)
    {
        std::cout << "Too old!";
    }
    else
    {
        std::cout << "Not old enough";
    }
}