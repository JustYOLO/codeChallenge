#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
using namespace std;

int N, M;
bool maze[101][101] = { false, };
int length[101][101] = { 0, }; // if length = 0, vertex has not visited

int Xdir[4] = {0, 0, -1, 1};
int Ydir[4] = {-1, 1, 0, 0}; // 1st index - 1 -> 0th index


void solution() {
    queue<pair<int, int>> q;
    int nextX, nextY;
    
    q.push(pair<int, int>(1, 1));
    length[1][1] = 1; // length also contains start & end vertex

    while(!q.empty()) {
        pair<int, int> curr = q.front();
        q.pop();

        for(int i = 0; i < 4; i++) {
            nextX = curr.first + Xdir[i];
            nextY = curr.second + Ydir[i];

            if(!maze[nextX][nextY])
                continue;
            else
                if(length[nextX][nextY] == 0) {
                    q.push(pair<int, int>(nextX, nextY));
                    length[nextX][nextY] = length[curr.first][curr.second] + 1;
                }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    for(int i = 1; i <= N; i++)
    {
        string s;
        cin >> s;
        for(int j = 0; j < M; j++) {
            if(s[j] == '1')
                maze[i][j+1] = true;
        }
    }
    solution();
    cout << length[N][M];

    return 0;
}
