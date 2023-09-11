#include <iostream>
#include <cmath>
using namespace std;

int w[30];
bool dp[31][15'001];
int n;

void recursion(int count, int weights);

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++)
        cin >> w[i];

    recursion(0, 0);
    int k, tmp;
    cin >> k;
    for(int i = 0; i < k; i++)
    {
        cin >> tmp;
        if(tmp > 15'000) cout << "N ";
        else if(dp[n][tmp]) cout << "Y ";
        else cout << "N ";
    }


    return 0;
}

void recursion(int count, int weights)
{
    if(count > n || dp[count][weights]) return;
    dp[count][weights] = true;
    
    recursion(count + 1, weights + w[count]);
    recursion(count + 1, abs(weights - w[count]));
    recursion(count + 1, weights);
}