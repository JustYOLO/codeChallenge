#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    set<string> name;
    int n, ans = 0;
    string tmp;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> tmp;
        if(tmp == "ENTER") name.clear();
        else
        {
            if(name.count(tmp) == 0)
            {
                ans++;
                name.insert(tmp);
            }
        }
    }
    cout << ans;
    return 0;
}