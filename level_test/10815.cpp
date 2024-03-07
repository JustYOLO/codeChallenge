#include <iostream>
#include <algorithm>
using namespace std;

int N, M;
vector<int> cards; // or use int arr[500'000] ?

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int tmp;

    cin >> N;
    for(int i = 0; i < N; i++)
    {
        cin >> tmp;
        cards.push_back(tmp);
    }
    sort(cards.begin(), cards.end());
    cin >> M;
    for(int i = 0; i < M; i++)
    {
        cin >> tmp;
        if(binary_search(cards.begin(), cards.end(), tmp))
            cout << "1 ";
        else
            cout << "0 ";
    }


    return 0;
}