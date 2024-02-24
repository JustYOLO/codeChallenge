#include <iostream>
#include <algorithm>
#include <queue>
#define MAX 32001
using namespace std;

int N, M;
vector<int> lines[MAX];
int steps[MAX];

void func();

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;
    int a, b;
    for(int i = 0; i < M; i++)
    {
        cin >> a >> b;
        lines[a].push_back(b);
        steps[b]++;
    }

    func();

    return 0;
}

void func()
{
    queue<int> q;
    int a;

    for(int i = 1; i <= N; i++)
    {
        if(steps[i] == 0) q.push(i);
    }
    while(!q.empty())
    {
        a = q.front(); q.pop();
        cout << a << " ";
        for(int b: lines[a])
        {
            if(--steps[b] == 0) q.push(b);
        }
    }
}
