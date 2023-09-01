#include <iostream>
#include <algorithm>
using namespace std;

long long count(long long x);
long long getNum(long long small, long long big);

long long N, k;
int main()
{
    cin >> N >> k;
    cout << getNum(1, N*N);
}

long long count(long long x)
{
    long long sum = 0;
    for (int i = 1; i <= N; i++)
        sum += min(x / i, N); // i행의 배수와 행에서의 최댓값을 비교해 갯수를 셀수 있음
    return sum;
}

long long getNum(long long small, long long big)
{
    if(small > big) return small; // small이 더 커지면 recursion 종료
    long long mid = (small + big) / 2; 
    long long total = count(mid); // 중간값의 갯수 저장
    
    if(total >= k)
        return getNum(small, mid - 1);
    else
        return getNum(mid + 1, big);
}
