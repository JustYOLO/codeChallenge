#include <iostream>
#include <string>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string name;
    cin >> name;
    if(name == "ENTER") cout << "yep";
    cin >> name;
}