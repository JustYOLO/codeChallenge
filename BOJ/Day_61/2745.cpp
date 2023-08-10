#include <iostream>
#include <string>
#include <cmath>
using std::cout;
using std::cin;
using std::string;

int num(char c)
{
    if(isdigit(c)) return static_cast<int>(c) - '0';
    else return static_cast<int>(c) - 55;
}

int main()
{
    string s;
    int n;
    long long int a = 0;
    cin >> s >> n;
    
    for(int i = 0; i < s.length(); i++)
    {
        a += num(s[s.length() - i - 1]) * pow(n, i);
    }
    
    cout << a << '\n';
    return 0;
}
