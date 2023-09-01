#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
/*
공유기의 간격이 동일하게(동일한 간격으로 세워지면 가장 인접한 공유기의 길이가 최대가 됨)
설치되는것이 목표
*/

vector<int> house; // 집의 좌표를 담는 vector
int C; // 공유기의 대수를 저장하는 변수
int getLen(int small, int big); // 가장 인접한 공유기의 길이가 최대인 값을 찾는 함수

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N, tmp; // tmp는 집의 좌표를 임시로 받는 변수
    cin >> N >> C; // N은 집의 갯수, C는 공유기의 대수
    for(int i = 0; i < N; i++)
    {
        cin >> tmp;
        house.push_back(tmp); // 집의 위치를 house에 저장
    }
    sort(house.begin(), house.end()); // 오름차순 정렬
    cout << getLen(1, house[house.size()-1] - house[0]);
}

int getLen(int small, int big)
{
    int mid = (big + small) / 2; // 길이의 중간값 설정
    int routers = 1; // 최초 공유기 설치
    int pos = house[0]; // 최초로 공유기를 설치한 집(좌표가 가장 작은 집)의 좌표로 초기화
    while(pos + mid <= house[house.size()-1]) // mid보다 크거나 같은 거리에 있는 집으로
    {
        pos += mid; // mid만큼 이동
        pos = *lower_bound(house.begin(), house.end(), pos); // 현재 위치(mid를 더한 값)에서 같거나 먼 집으로 이동
        routers++; // 해당 위치에 공유기 설치
    }
    if(routers >= C) // 공유기의 대수가 목표이상일때
    {
        if(mid + 1 > big) return mid; // 모든 경우의수를 확인 한 경우 mid 리턴
        else return getLen(mid + 1, big); // 아닌 경우 mid 보다 큰값 확인
    }
    else // 공유기 대수가 목표 미만 일때
        return getLen(small, mid - 1); // 길이를 줄여서 확인
}
