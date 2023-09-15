#include <iostream>
#include <stack>
using std::cout, std::cin, std::stack;

/*
오큰수와 기본은 비슷하지만 비교하는 값이 원소 크기 자체가 아닌 원소의 등장
횟수이므로 등장횟수를 map에 저장
==>time exceeded -> stack에 원소만 저장해서?

-> stack에 pair로 원소와 등장횟수를 동시에 저장해보기
==>time exceeded

-> int array 사용 -> 통과
vector로 사용해도 될것같다.
*/

int count[1'000'001];

int main()
{
    int N; // 수열의 크기를 저장할 변수
    cin >> N;
    int arr[N]; // 수열을 저장할 int 배열
    for(int i = 0; i < N; i++)
    {
        cin >> arr[i];
        count[arr[i]]++;
    }
    int ans[N]; // 오등큰수를 저장할 배열
    stack<int> stk; // 원소를 저장할 스택 

    ans[N - 1] = -1; // 수열의 맨끝 원소의 오등큰수는 무조건 -1
    stk.push(arr[N - 1]); // 해당 원소를 스택에 push

    for(int i = N - 2; i >= 0; i--)
    {
        while(!stk.empty()) // 스택이 빌때 까지
        {
            if(count[arr[i]] < count[stk.top()]) // 오등큰수를 찾으면
            {
                ans[i] = stk.top(); // 오등큰수를 저장
                break;
            }
            else
                stk.pop(); // 없다면 스택을 pop
        }
        if(stk.empty()) // 비어 있다면 
            ans[i] = -1; // 오등큰수는 -1
        stk.push(arr[i]); // 자기 자신을 스택에 push
    }
    for(int i: ans)
        cout << i << ' '; //오등큰수를 출력

    return 0;
}