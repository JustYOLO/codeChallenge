#include <iostream>
#include <vector>
#define MAX_ARR 500'000
using namespace std;

int N;
vector<int> arr;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    int tmp;
    arr.reserve(MAX_ARR);
    for(int i = 0; i < N; i++)
    {
        cin >> tmp;
        arr.push_back(tmp);
    }
    long long ans = 0;
    int highest, target;
    for(int i = 0; i < N; i++)
    {
        target = arr.back(); arr.pop_back();
        highest = arr.back();
        for(int j = arr.size() - 1; j > 0; j--)
        {
            if(target < arr[j])
            {
                ans++;
                break;
            }
            else if(highest <= arr[j])
            {
                ans++;
                highest = arr[j];
            }
        }
    }
    cout << ans;


    return 0;
}