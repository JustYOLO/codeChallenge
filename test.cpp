#include <iostream>
#include <stack>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    stack<int> s;
    s.push(1);
    s.push(2);
    s.push(3);

    cout << s.top();
}