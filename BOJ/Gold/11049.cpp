#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int dp[501][501]; // dp 값(곱셈 연산의 수)을 저장할 배열
int matrix[501][2]; // 행렬의 값을 저장할 배열
int n; // 입력될 행렬의 수

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n;
    for(int i = 1; i <= n; i++)
        cin >> matrix[i][0] >> matrix[i][1]; // 행렬을 저장
    for(int i = 1; i < n; i++) // 간격 단위로 반복문 설정
    {
        for(int j = 1; j + i <= n; j++) // 시작점 기준 설정
        {
            if(i != 1) // 간격이 1인 경우 제외
            {
                dp[j][j + i] = INT_MAX; // 최댓값으로 지정
                for(int m = j; m <= j + i; m++) // 부분 간격 설정
                    dp[j][j + i] = min(dp[j][j + i], dp[j][m] + dp[m + 1][j + i] + matrix[j][0] * matrix[m][1] * matrix[j + i][1]);
                    // 현재까지 구한 최솟값과 부분 간격으로 설정한 곱셈 연산 수를 비교해 최솟값을 저장
            }
            else // 간격이 1이면 앞 뒤 곱한값 저장
                dp[j][j + i] = matrix[j][0] * matrix[j][1] * matrix[j + i][1];
        }
    }
    cout << dp[1][n] << '\n'; // 정답을 출력
    return 0;
}
