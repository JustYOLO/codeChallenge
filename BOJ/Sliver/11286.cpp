#include <iostream>
#include <queue>
#include <cstdlib>
using namespace std;

struct cmp // 비교 연산자 추가
{
    bool operator()(int a, int b) // a가 입력된 값, b가 우선순위 큐 안에 있는 값
    {
        if(abs(a) > abs(b)) // 절댓값이 a가 크면
            return true; // true: b보다 뒤에 추가
        else if(abs(a) == abs(b)) // 절댓값이 같으면
            return a > b; // 더 작은 수(음수 인 값)가 뒤로 가게 추가
        else // 절댓값이 b가 크면
            return false; // false: b보다 앞에 추가
    }

};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    priority_queue<int, vector<int>, cmp> pq; // priority_queue로 우선 순위 큐(절댓값이 작은 수 우선) 구현
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