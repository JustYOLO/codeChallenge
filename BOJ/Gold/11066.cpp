#include <iostream>
#include <algorithm>
#include <climits> // INT_MAX 사용
using namespace std;

int pages[501]; // 해당 챕터의 페이지 수를 저장할 배열
int sum[501]; // 해당 챕터 까지의 페이지 수 합을 저장할 배열
int dp[501][501]; // dp의 결과값 저장을 위한 배열

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t; // 테스트 케이스의 수
    cin >> t;
    while(t--)
    {
        int k; // 책의 챕터 수
        cin >> k; 
        sum[0] = 0; // 0번째 인덱스는 사용하지 않음
        for(int i = 1; i <= k; i++)
        {
            cin >> pages[i];
            sum[i] = sum[i - 1] + pages[i]; // 합을 저장
        }
        for(int i = 1; i <= k; i++)
        { 
            for(int j = 1; j <= k - i; j++)
            { // j는 시점, j + i는 종점
                dp[j][j + i] = INT_MAX; // 기본값을 크게 설정
                for(int m = j; m <= j + i; m++)
                { // m은 j와 j+i 사이의 중간 지점을 설정
                    dp[j][j + i] = min(dp[j][j + i], dp[j][m] + dp[m + 1][j + i] + sum[j + i] - sum[j - 1]);
                    // 기존 dp 값과 m으로 중간지점을 삼은 값이 더 큰지 비교
                }
            }
        }
        cout << dp[1][k] << '\n'; // 1 ~ k의 dp 값을 출력 = 답
    }
    return 0;
}