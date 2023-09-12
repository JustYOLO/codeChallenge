#include <iostream>
#include <algorithm>
using namespace std;

/*
dp[i][j]는 i번째 app까지 확인했을때 j의 비용이 들때 확보하는 메모리의 최대값이 value이다.

i번째 앱의 j비용을 최대 메모리 값은
dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - apps[i][1]] + apps[i][0]);
으로, j - cost(i)의 값이 음수가 아니면 실행,
i번째 앱을 사용하지 않을때 최대 값인 dp[i - 1][j]와 해당 cost에서 i번째 앱을 재실행 할때 드는 비용을 추가로 더한 값중 큰 값이 dp[i][j]에 들어간다.

j - cost(i)의 값이 음수 -> i번째 앱의 cost가 크다.
-> dp[i][j] = dp[i - 1][j] 이전 결과와 동일하다.
*/

int dp[100][10'001];
int apps[100][2]; // 앱의 메모리와 재시작시 드는 cost를 저장
int N, M; // N은 앱의 갯수, M은 확보해야하는 메모리의 크기

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int costSum = 0; // cost값의 최대치를(합) 구함(임계값)
    cin >> N >> M;
    for(int i = 0; i < N; i++)
        cin >> apps[i][0]; // idx = 0은 사용하는 mem
    for(int i = 0; i < N; i++)
    {
        cin >> apps[i][1]; // idx = 1은 재시작시 cost
        costSum += apps[i][1]; // 합에 값을 추가
    }
    
    for(int i = 0; i <= costSum; i++) // idx = 0의 앱을 확인
    {
        if(apps[0][1] <= i) // 앱의 cost 이상의 i부터 저장
        {
            dp[0][i] = apps[0][0];
        }
    }

    for(int i = 1; i < N; i++) // idx = 1부터 앱을 하나씩 확인
    {
        for(int j = 0; j <= costSum; j++) // cost = 0부터 임계값까지 확인
        {
            if(j - apps[i][1] >= 0) // 현재 확인하는 app의 cost 값을 사용할수 있을때(음수를 만들지 않을때)
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - apps[i][1]] + apps[i][0]);
            
            else // cost값이 클 경우 (음수를 만들 경우)
                dp[i][j] = dp[i - 1][j]; // 이전의 결과와 같음
        } 
    }
    for(int i = 0; i <= costSum; i++)
    { // cost = 0에서 부터
        if(dp[N - 1][i] >= M) // 목표로 하는 M값 이상인 cost를 찾는다.
        {
            cout << i;
            break; // 찾으면 출력후 반복문 탈출
        }
    }

    return 0;
}