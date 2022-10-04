#include <iostream>

int main()
{
    using std::cin;
    using std::cout;
    using std::string;

    string name;
    int age;
    cout << "What is your name? ";
    std::getline(cin >> std::ws, name);
    cout << "What is your age? ";
    cin >> age;
    cout << "\nHello " << name << "!\nYou are " << age << " years old.\n";

    return 0;
}