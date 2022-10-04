#include <iostream>

// type conversions
// changing values for mutable variables

int main()
{
    int x = 12;
    // explicit
    x = 13;
    // implicit
    double z = (int)14.22;

    int correct = 12;
    int total = 20;
    // will give a 0 output because it is using int as  a data type
    // double score = (correct / total) * 100;
    double score = (correct / (double)total) * 100;

    std::cout << score << "%";

    return 0;
}