#include <iostream>
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, num;
    int min = 1'000'001;
    int max = -1'000'001;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> num;
        if(num < min)
            min = num;
        if(num > max)
            max = num;
    }
    cout << min << " " << max;
}