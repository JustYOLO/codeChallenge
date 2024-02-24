#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

bool visited[101] = {false, };
int num = 0;
vector<int> lines[101];

void dfs(int p);

int main(void) 
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    int a, b;
    cin >> n >> m;
    for(int i = 0; i < m; i++)
    {
        cin >> a >> b;
        lines[a].push_back(b);
        lines[b].push_back(a);
    }

    // for(int i = 1; i <= n; i++)
    // {
    //     sort(lines[i].begin(), lines[i].end());
    // }

    dfs(1);
    cout << num - 1;

    return 0;
}

void dfs(int p)
{
    visited[p] = true;
    num++;
    for(int i: lines[p])
    {
        if(!visited[i]) dfs(i);
    }
}