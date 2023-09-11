#include <iostream>
#include <algorithm>
using namespace std;

int dp[100'000]; // idx는 무게를, 값은 해당 idx의 무게일때 최대의 가치를 저장한다.

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;
    int prod[n][2]; // [][0]은 무게, [][1]은 가치
    for(int i = 0; i < n; i++)
        cin >> prod[i][0] >> prod[i][1];
    
    for(int i = 0; i < n; i++) // 1개의 물품을 넣어본다
    {
        for(int j = k; j >= 1; j--) // k부터 1까지 확인
        {
            if(prod[i][0] <= j)
                dp[j] = max(dp[j], prod[i][1] + dp[j - prod[i][0]]);
        }
    }

    cout << dp[k] << '\n';
    return 0;
}