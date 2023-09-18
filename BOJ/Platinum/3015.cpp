#include <iostream>
#include <vector>
#define MAX_ARR 500'000
using namespace std;

/*
stack에 항상 내림차순으로 정렬 -> 현재까지 볼수있는 원소들을 모아놔야 한다.
stack의 top과 확인하는 원소가 같다면 -> 어디까지 볼수 있는지 모름
ex) top -> 8, 9, 10 인 stack에서 키가 8인 사람이 오면 8, 9까지 볼수 있지만 10은 볼수 없음.
*/

int main()
{
    int N, curr;
    long long ans = 0;
    cin >> N; // 입력받는 원소의 갯수
    vector<pair<int, int>> stack; // 현재까지 볼수있는 원소들을 저장 (top을 시작점으로 볼때 내림차순으로 정렬)
    // pair의 first는 키, second는 현재까지 같은 원소의 갯수를 저장
    stack.reserve(MAX_ARR); // vector 속도를 빠르게
    while(N--)
    {
        cin >> curr;
        int nums = 1;
        while(!stack.empty() && stack.back().first < curr)
        { // 스택안에 볼수 있는 사람이 있을때까지
            ans += stack.back().second;
            stack.pop_back();
        }
        if(!stack.empty())
        { // 비어있지 않으면
            if(stack.back().first == curr)
            {
                ans += stack.back().second;
                nums = ++stack.back().second;
                if(stack.size() > 1)
                    ans++;
                stack.pop_back();
            }
            else
                ans++;
        }
        stack.push_back(make_pair(curr, nums));
    }
    cout << ans;

    return 0;
}
