#include <iostream>
#include <stack> // using stack
using namespace std;

int main(void)
{
    bool flag;
    int n;
    char b[51];
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        flag = false;
        stack<int> s;
        cin >> b;
        if(b[0] == ')')
        {
            cout << "NO\n";
            continue;
        }
        int j = 0;
        while(b[j] != '\0')
        {
            if(b[j] == '(')
                s.push(1);
            else
            {
                if(s.empty())
                {
                    cout << "NO\n";
                    flag = true;
                    break;
                }
                else
                    s.pop();
            }
            j++;
        }
        if(!flag)
        {
            if(s.empty())
                cout << "YES\n";
            else
                cout << "NO\n";
        }
    }

    return 0;
}