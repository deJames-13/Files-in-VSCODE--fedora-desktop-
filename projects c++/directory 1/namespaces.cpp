#include <iostream>

// namespaces are for displaying variables with same name
namespace first
{
    int x = 1;
}

namespace second
{
    int x = 2;
}

int main()
{
    // namespace standard
    using std::cout;
    using std::string;

    // displaying namespaces
    cout << first::x << std::endl;
    cout << second::x << std::endl;
    return 0;
}