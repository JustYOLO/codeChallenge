#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

void bfs(int t);
bool isVisited(int t);

int visited[100'001] = { 0, };
vector<int> lines[100'001];
int result[100'001];
int N, M, R;
int cnt = 1;
queue<int> q;

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

    bfs(R);
    
    for(int i = 1; i <= N; i++)
    {
        cout << result[i] << "\n";
    }

    return 0;
}

void bfs(int t)
{
    visited[t] = 1;
    result[t] = cnt++;
    q.push(t);
    int u;
    while(!q.empty())
    {
        u = q.front();
        q.pop();
        for(int i: lines[u])
        {
            if(!isVisited(i))
            {
                visited[i] = 1;
                result[i] = cnt++;
                q.push(i);
            }
        }
    }
}

bool isVisited(int t)
{
    if(visited[t] == 1)
        return true;
    else
        return false;
}
