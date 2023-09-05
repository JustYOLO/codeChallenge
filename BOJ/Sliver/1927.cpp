    #include <iostream>
    #include <queue>
    using namespace std;

    int main()
    {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        
        priority_queue<int, vector<int>, greater<int>> pq; // priority_queue로 우선 순위 큐(작은 수 우선) 구현
        int n, tmp;
        cin >> n;
        for(int i = 0; i < n; i++)
        {
            cin >> tmp;
            if(tmp == 0) // 입력이 0일경우(출력)
            {
                if(pq.empty() == true) // 큐가 비어있으면
                    cout << "0\n"; // 0을 출력
                else // 비어있지 않으면
                {
                    cout << pq.top() << "\n"; // 최솟값 출력
                    pq.pop();
                }
            }
            else // 0이 아닌 경우 (입력)
                pq.push(tmp); // 큐에 입력한 자연수 추가
        }

        return 0;
    }