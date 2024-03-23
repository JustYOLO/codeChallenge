#include <iostream>
#include <algorithm>
#include <queue>
#include <tuple>
using namespace std;

int N, M, H;
int storage[102][102][102] = { 0, };
int arrDays[102][102][102] = { 0, };
vector<tuple<int, int, int>> initial;

int Xdir[6] = {0, 0, 1, -1, 0, 0};
int Ydir[6] = {-1, 1, 0, 0, 0, 0};
int Zdir[6] = {0, 0, 0, 0, -1, 1};

void solution() {
    queue<tuple<int, int, int>> q;
    int nextX, nextY, nextZ;
    int currX, currY, currZ;
    for(tuple t: initial) 
        q.push(t);
    

    while(!q.empty()) {
        tuple t = q.front(); q.pop();
        currZ = get<0>(t); currX = get<1>(t); currY = get<2>(t);

        for(int i = 0; i < 6; i++) {
            nextX = currX + Xdir[i];
            nextY = currY + Ydir[i];
            nextZ = currZ + Zdir[i];
            if(nextX < 0 || nextX >= N || nextY < 0 || nextY >= M || nextZ < 0 || nextZ >= H)
                continue;
            if(arrDays[nextZ][nextX][nextY] >= 0)
                continue;

            arrDays[nextZ][nextX][nextY] = arrDays[currZ][currX][currY] + 1;
            q.push(make_tuple(nextZ, nextX, nextY));
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int tmp;

    cin >> M >> N >> H;

    for(int i = 0; i < H; i++)
        for(int j = 0; j < N; j++)
            for(int k = 0; k < M; k++)
            {
                cin >> tmp;
                storage[i][j][k] = tmp;
                if(tmp == 1)
                    initial.push_back(make_tuple(i, j, k));
                else if(tmp == 0)
                    arrDays[i][j][k] = -1;
            }

    solution();

    int days = -1;
    for(int i = 0; i <= H; i++)
        for(int j = 0; j <= N; j++)
            for(int k = 0; k <= M; k++) {
                if(arrDays[i][j][k] == -1) {
                    cout << -1;
                    return 0;
                }
                days = max(days, arrDays[i][j][k]);
            }
    cout << days;

    return 0;
}
