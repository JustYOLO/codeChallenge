#include <iostream>
#include <algorithm>
using namespace std;

/*

점화식: dp[num] = dp[num] + dp[num - coins[idx]]
num은 동전의 합, idx는 현재 동전의 idx를 의미.

dp[0] = 1로, 0을 만드는 경우의 수는 1개(아무것도 선택하지 않는 것)

*/

int n, k;
int coins[100];
int dp[10'001] = {0};


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> k;
    dp[0] = 1; // idx = 0은 아무것도 선택하지 않는 경우의 수.
    for(int i = 0; i < n; i++) // 동전을 입력받음
        cin >> coins[i];
    for(int i = 0; i < n; i++) // 동전을 하나씩 넣어본다.
    {
        if(coins[i] > k) continue;
        for(int j = coins[i]; j <= k; j++) // 해당 동전의 값부터 시작
            dp[j] += dp[j - coins[i]];
    }

    cout << dp[k] << '\n';
    return 0;
}