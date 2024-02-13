#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void dfs(int t);

int visited[100'001] = { 0, };
vector<int> lines[100'001];
int result[100'001];
int N, M, R;
int cnt = 1;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N >> M >> R;
    int a, b;
    for(int i = 0; i < M; i++)
    {
        cin >> a >> b;
        lines[a].push_back(b);
        lines[b].push_back(a);
    }
    for(int i = 1; i <= N; i++)
    {
        sort(lines[i].begin(), lines[i].end(), greater<int>());
    }

    dfs(R);
    
    for(int i = 1; i <= N; i++)
    {
        cout << result[i] << "\n";
    }

    return 0;
}

void dfs(int t)
{
    if(visited[t] == 1)
        return;
    result[t] = cnt++;
    visited[t] = 1;
    for(int i : lines[t]) {
        dfs(i);
    }
}
