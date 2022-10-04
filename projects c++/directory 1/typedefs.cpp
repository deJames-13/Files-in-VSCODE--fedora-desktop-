#include <iostream>
#include <vector>

// like an alias for a very looong datatype
// typedef std::vector<std::pair<std::string, int>> pairlist_t;
typedef std::string txt_t;

// another way
using mkStr = std::string;

int main()
{
    // pairlist_t pairlist;
    txt_t anStr = "looool";
    mkStr anStr2 = "looool";

    return 0;
}