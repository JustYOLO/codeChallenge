#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s1 = "123";
    s1 = s1.substr(0, 0);

    cout << s1 << endl;

    return 0;
}