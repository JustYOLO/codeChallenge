#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <map>
#include <cmath>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    int start, end;
    cin >> start >> end;
    set<int> s;
    s.insert(1);
    s.insert(2);
    s.insert(4);
    s.insert(5);
    s.insert(8);
    s.insert(9);
    
    int mid = (start + end) / 2;
    int bigger = *s.upper_bound(mid);
    int smaller = *--s.upper_bound(mid);
    if(s.find((start + end) / 2) != s.end()) cout << mid;
    else if(bigger - mid > smaller - mid) cout << smaller;
    else cout << bigger;

    return 0;
}