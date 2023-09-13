#include <iostream>
#include <string>
using namespace std;

/*
주어진 문자열의 앞 글자를 계속 추가해서 c4의 길이 이상이 되면 뒷 문자열을
c4문자열과 비교해서 같으면 삭제.
모든 문자열을 추가할때까지 반복.
*/

string original;
string ans = "";
string c4;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> original >> c4;
    for(char c: original) // 문자열을 하나씩 추가
    {
        ans += c; 
        if(ans.size() >= c4.size() && c == c4[c4.size() - 1])
        { // 임시저장한 문자열이 폭발 문자열보다 크고, 임시문자열의 끝 문자열이 폭발 문자열의 마지막과 같을때 (= 폭발 가능함)
            if(ans.substr(ans.size() - c4.size(), c4.size()) == c4)
                ans.erase(ans.end() - c4.size(), ans.end());
            // 임시저장한 문자열의 뒷부분을 c4문자열과 비교한다.
        }
    }
    if(ans.size() == 0)
        cout << "FRULA"; // 문자열이 비어있으면 FRULA를 출력
    else
        cout << ans;

    return 0;
}