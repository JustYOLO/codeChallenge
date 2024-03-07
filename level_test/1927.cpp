#include <iostream>
#include <queue> // using priority_queue
using namespace std;

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    priority_queue<int, vector<int>, greater<int>> pq;
    // min priority queue using comparison func greater<int>
    int n, num;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> num;
        if(num == 0)
        {
            if(pq.empty() == true)
                cout << "0\n";
            else
            {
                cout << pq.top() << "\n";
                pq.pop();
            }
        }
        else
            pq.push(num);
    }

    return 0;
}