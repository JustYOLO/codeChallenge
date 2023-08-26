#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int n, tmp, width, result = 0;
    stack<int> s;
    
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    for(int i = 0; i < n; i++)
    {
        while(s.size() != 0 && arr[s.top()] > arr[i])
        {
            tmp = s.top(); s.pop();

            if(s.size() == 0) width = i;
            else width = i - s.top() - 1;
            result = max(result, width * arr[tmp]);
        }
        s.push(i);
    }
    while(s.size() != 0)
    {
        tmp = s.top(); s.pop();

        if(s.size() == 0) width = n;
        else width = n - s.top() - 1;
        result = max(result, width * arr[tmp]);
    }
    cout << result;
    
    return 0;
}