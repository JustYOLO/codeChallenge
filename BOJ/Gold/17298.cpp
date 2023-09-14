#include <iostream>
#include <stack>
using namespace std;

/*
배열의 뒤에서 부터 검사 (배열의 가장 오른쪽 원소의 오큰수는 무조건 -1)
가장 오른쪽 원소를 stack에 넣음

이후 각각의 원소를 tmp라 할때,:
while(!stack.empty)
{
    if(tmp < stack.top())
        tmp의 오큰수는 stack.top()
        break;
    else
        stk.pop();
}
if(stack.empty) // 오큰수가 없을때
    tmp의 오큰수는 -1
stack.push(tmp);
*/

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int N;
    cin >> N;
    int arr[N]; // 수열을 저장할 배열
    int ans[N]; // 오큰수를 저장할 배열
    stack<int> stk; // 원소를 저장할 스택 
    for(int i = 0; i < N; i++)
        cin >> arr[i]; // 입력한 수열을 배열에 저장
    ans[N - 1] = -1; // 수열의 가장 오른쪽 원소의 오큰수(-1)을 저장
    stk.push(arr[N - 1]); // 해당 원소를 스택에 push
    for(int i = N - 2; i >= 0; i--)
    {
        while(!stk.empty()) // 스택이 빌때 까지
        {
            if(arr[i] < stk.top()) // 오큰수를 찾으면
            {
                ans[i] = stk.top(); // 오큰수를 저장
                break;
            }
            else
                stk.pop(); // 없다면 스택을 pop
        }
        if(stk.empty()) // 비어 있다면 
            ans[i] = -1; // 오큰수는 -1
        stk.push(arr[i]); // 자기 자신을 스택에 push
    }
    for(int i: ans)
        cout << i << ' '; // 오큰수를 출력

    return 0;
}