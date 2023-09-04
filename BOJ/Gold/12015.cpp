#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
수열을 출력하는것이 아닌 길이만을 출력함으로 실제 vector<int> sq에 있는 수열은 
가장 긴 증가하는 수열이 아닌, 해당 수열의 길이를 알아내기 위해 사용된다.
*/ 

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;
    int arr[n]; // 주어진 수를 받을 int 배열
    for(int i = 0; i < n; i++)
        cin >> arr[i];
    
    vector<int> sq; // 증가하는 수열의 길이를 찾기위해 사용되는 vector
    sq.push_back(arr[0]); // 맨 처음 수를 vector에 입력

    /*
    가장 긴 증가하는 수열 -> 수열이 길어야함 -> 수 사이의 간격이 작아야 유리함
    따라서 수열의 원소와 상관없이 간격이 작게 수열을 만들면 "가장 긴 증가하는 수열"의
    길이와 동일하게 된다.
    */
    int idx; // 비교할 수와 같거나 큰 수의 인덱스를 저장할 int 변수
    for(int i = 1; i < n; i++)
    {
        if(sq[sq.size() - 1] < arr[i]) // 주어진 수가 수열의 가장 큰수보다 크다면
            sq.push_back(arr[i]); // 수열의 끝에 추가
        else // 주어진 수가 수열의 가장 큰수보다 작다면
        {
            idx = lower_bound(sq.begin(), sq.end(), arr[i]) - sq.begin(); // 수열의 원소중 같거나 큰 수의 idx를 얻는다.
            sq[idx] = arr[i]; // 해당 위치에 주어진 수를 넣는다.
        }
    }

    cout << sq.size(); // 수열의 길이를 출력
    return 0;
}