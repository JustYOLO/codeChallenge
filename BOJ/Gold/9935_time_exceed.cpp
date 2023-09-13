/*
using deqeue -> time exceeded
*/

#include <iostream>
#include <string>
#include <deque>
using namespace std;

string original;
string c4;
deque<char> d; // 문자를 담는 deque
bool isDel = false;
bool ongoing = false;

int main()
{
    cin >> original >> c4;
    for(char c: original) // deque에 문자열을 넣는다.
        d.push_back(c);

    while(true)
    {
        isDel = false;
        ongoing = false;
        int cLen = 0;
        int oLen = d.size();
        for(int i = 0; i < oLen; i++)
        {
            char tmp = d.front(); d.pop_front();
            if(tmp == c4[0])
            {
                cLen = 1;
                ongoing = true;
            }
            else if(tmp == c4[cLen] && ongoing)
                cLen++;
            else
                ongoing = false;
            
            d.push_back(tmp);
            
            if(cLen == c4.size())
            {
                for(int j = 0; j < cLen; j++)
                    d.pop_back();
                cLen = 0;
                isDel = true;
            }
        }
        if(!isDel)
            break;
    }

    if(d.empty())
    {
        cout << "FRULA";
    }
    else
    {
        while(!d.empty())
        {
            cout << d.front();
            d.pop_front();
        }
    }

    return 0;
}
