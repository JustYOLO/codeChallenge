#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

bool isHigher(pair<string, int> &a, pair<string, int>&b)
{
    if(a.second == b.second)
    {
        if(a.first.length() == b.first.length())
            return a.first < b.first;
        return a.first.length() > b.first.length();
    }
    return a.second > b.second;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    string word;
    map<string, int> vocaList;

    cin >> n >> m;
    for(int i = 0; i < n; i++)
    {
        cin >> word;
        if(word.length() >= m)
        {
            if(vocaList.find(word) != vocaList.end())
                vocaList[word]++;
            else
                vocaList[word] = 1;
        }
    }
    vector<pair<string, int>> output(vocaList.begin(), vocaList.end());
    sort(output.begin(), output.end(), isHigher);
    for(pair<string, int> s: output)
        cout << s.first << '\n';

    return 0;
}