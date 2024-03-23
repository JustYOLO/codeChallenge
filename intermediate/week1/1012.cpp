#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

bool field[52][52] = { false, };
bool visited[52][52] = { false, }; // don't use 0th index;
int T, M, N, K;
int result = 0;

int Xdir[4] = {0, 0, -1, 1};
int Ydir[4] = {-1, 1, 0, 0}; // 1st index - 1 -> 0th index


void dfs(int a, int b) {
    int nextX, nextY;
    stack<pair<int, int>> s;
    visited[a][b] = true;
    s.push(pair<int, int>(a, b));
    while (!s.empty())
    {
        pair<int, int> curr = s.top();
        s.pop();

        if(!visited[curr.first][curr.second])
            visited[curr.first][curr.second] = true;

        for(int i = 0; i < 4; i++) {
            nextX = curr.first + Xdir[i];
            nextY = curr.second + Ydir[i];

            if(field[nextX][nextY])
                if(!visited[nextX][nextY])
                    s.push(pair<int, int>(nextX, nextY));
        }
    }
    
    result++;
}

void initialize() {
    for(int i = 0; i < 52; i++)
        for(int j = 0; j < 52; j++) {
            field[i][j] = false;
            visited[i][j] = false;
        }
    result = 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int a, b;

    cin >> T;
    for(int i = 0; i < T; i++) {
        initialize();
        vector<pair<int, int>> cabbage;

        cin >> M >> N >> K;

        for(int j = 0; j < K; j++) {
            cin >> a >> b;
            field[a + 1][b + 1] = true;
            cabbage.push_back(pair<int, int>(a + 1, b + 1));
        }
        for(pair<int, int> p: cabbage) {
            if(visited[p.first][p.second])
                continue;
            else
                dfs(p.first, p.second);
        }

        cout << result << '\n';
    }

    return 0;
}
