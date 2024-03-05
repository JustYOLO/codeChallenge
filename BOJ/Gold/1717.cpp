/*
1st try: time exceeded
2nd try: added parent[x] = getParent(parent[x]);
*/

#include <iostream>
#include <algorithm>
using namespace std;

int parent[1'000'001];

int getParent(int x)
{
    if(parent[x] == x) 
        return x;
    else 
        return parent[x] = getParent(parent[x]);
}

void mergeNodes(int x, int y)
{
    x = getParent(x);
    y = getParent(y);
    if(x == y)
        return;
    else
        if(x > y)
            parent[x] = y;
        else
            parent[y] = x;
}

void find(int x, int y)
{
    if(getParent(x) != getParent(y))
        cout << "NO\n";
    else
        cout << "YES\n";
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m, a, b, c;
    cin >> n >> m;
    for(int i = 1; i <= n; i++)
        parent[i] = i;
    for(int i = 0; i < m; i++)
    {
        cin >> a >> b >> c;
        if(a == 0)
            mergeNodes(b, c);
        else
            find(b, c);
    }
    
    return 0;
}