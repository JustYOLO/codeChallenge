#include <iostream>
using namespace std;

int m, n; // m은 세로, n은 가로
int dp[502][502]; // dp는 해당 좌표에서 목적지까지 도달한 경로의 객수
int height[502][502]; // 해당 칸의 높이

int search(int a, int b);

int main()
{
    cin >> m >> n;
    for(int i = 0; i <= m + 1; i++)
    {
        for(int j = 0; j <= n + 1; j++)
        {
            if(i == 0 || i == m + 1 || j == 0 || j == n + 1)
                height[i][j] = - 1; // 경계 설정
            else
                cin >> height[i][j]; // 높이를 저장
            dp[i][j] = -1; // 도착하지 않은 칸은 -1로 초기 설정
        }
    }

    cout << search(1, 1) << '\n';
    return 0;
}

int search(int a, int b) // 시작점부터 계산
{
    if(a == m && b == n) // 끝점에 도달할시
        return 1;
    else if(dp[a][b] != -1) // -1이 아니면 이전에 도달한적 있는 칸
        return dp[a][b];
    
    dp[a][b] = 0; // a, b에 도달하면 0으로 초기화 (새롭게 도달한 칸)
    if(height[a][b - 1] < height[a][b])
        dp[a][b] += search(a, b - 1);
        // 자신의 왼쪽에 있는 칸을 확인
    if(height[a - 1][b] < height[a][b])  
        dp[a][b] += search(a - 1, b);
        // 자신의 위에 있는 칸을 확인
    if(height[a][b + 1] < height[a][b])
        dp[a][b] += search(a, b + 1);
        // 자신의 오른쪽에 있는 칸을 확인
    if(height[a + 1][b] < height[a][b])
        dp[a][b] += search(a + 1, b);
        // 자신의 아래에 있는 칸을 확인

    return dp[a][b];
}