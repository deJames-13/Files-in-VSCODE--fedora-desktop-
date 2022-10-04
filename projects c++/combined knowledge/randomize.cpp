#include <iostream>
#include <cmath>
#include <ctime>
// if you want to unpack all the standard objects and functions
using namespace std;

int main()
{
    srand(time(NULL));
    int bal = 1000;

    while (true)
    {
        const int isWin = rand() % 2;
        const int value = (rand() % 1000) + 101;
        string n;
        cout << "\nDo you want to gamble? y/N ";
        cin >> n;
        cout << endl;
        if (n == "N" || n == "n")
        {
            cout << "Thank you for gambling!!!\n\n";
            break;
        }
        else
        {
            if (isWin == 1)
            {
                bal += value;
                cout << "You won " << value << "!\nYour current balance is " << bal << ".\n";
            }
            else
            {
                bal -= value;
                cout << "You lost " << value << "!\nYour current balance is " << bal << ".\n";
            }
        }
    }

    return 0;
}