#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int N, M, V;

bool dfsVisited[1'001] = { false, };
bool bfsVisited[1'001] = { false, };

queue<int> q;
vector<int> connected[1'001];


void dfs(int a) {
    int tmp;
    dfsVisited[a] = true;
    cout << a << ' ';

    for(int i = 0; i < connected[a].size(); i++) {
        tmp = connected[a][i];
        if(!dfsVisited[tmp])
            dfs(tmp);
    }
}

void bfs(int a) {
    int curr, next;
    q.push(a);
    bfsVisited[a] = true;

    while(!q.empty()) {
        curr = q.front();
        q.pop();
        cout << curr << ' ';

        for(int i = 0; i < connected[curr].size(); i++) {
            next = connected[curr][i];
            if(!bfsVisited[next]) {
                q.push(next);
                bfsVisited[next] = true;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);

    int a, b;

    cin >> N >> M >> V;
    for(int i = 0; i < M; i++) {
        cin >> a >> b;
        connected[a].push_back(b);
        connected[b].push_back(a);
    }

    for(int i = 0; i < N; i++)
        sort(connected[i].begin(), connected[i].end());

    dfs(V);
    cout << '\n';
    bfs(V);

    return 0;
}