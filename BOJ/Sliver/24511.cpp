#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int sqSize;
    int valueSize = 0;
    int isSQ[100'000];

    cin >> sqSize;
    for(int i = 0; i < sqSize; i++)
    {
        cin >> isSQ[i];
        if(isSQ[i] == 0) valueSize++;
    }
    vector<int> sqValue;
    int tmp;
    for(int i = 0; i < sqSize; i++)
    {
        cin >> tmp;
        if(isSQ[i] == 0) sqValue.push_back(tmp);
    }

    int inputSize;
    cin >> inputSize;
    vector<int> nums;
    for(int i = 0; i < inputSize; i++)
    {
        cin >> tmp;
        nums.push_back(tmp);
    }
    reverse(nums.begin(), nums.end());
    while(inputSize-- > 0)
    {
        if(sqValue.empty())
        {
            tmp = nums.back();
            nums.pop_back();
        }
        else
        {
            tmp = sqValue.back();
            sqValue.pop_back();
        }
        cout << tmp << ' ';
    }

    return 0;
}