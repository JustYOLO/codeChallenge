#include <iostream>
#include <algorithm>
using namespace std;

vector<vector<int>> lines;
int parent[10'001] = { 0, };
int V, E;

bool compare(const vector<int> &a, const vector<int> &b);

int get_parent(int x);
int connect_node(vector<int> line);

int solution()
{
    int sum = 0;
    int a, b;
    for(int i = 0; i < E; i++)
    {
        sum += connect_node(lines[i]);
    }
    return sum;
}

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int a, b, c;
    cin >> V >> E;

    for(int i = 1; i <= V; i++)
        parent[i] = i; // initialize parent

    for(int i = 0; i < E; i++)
    {
        cin >> a >> b >> c;
        
        lines.push_back(vector<int>());
        lines[i].push_back(a);
        lines[i].push_back(b);
        lines[i].push_back(c);
    }

    sort(lines.begin(), lines.end(), compare);

    cout << solution();

    return 0;
}

bool compare(const vector<int> &a, const vector<int> &b)
{
    return a[2] < b[2];
}

int get_parent(int x)
{
    if(parent[x] == x)
        return x;
    return parent[x] = get_parent(parent[x]);
}

int connect_node(vector<int> line)
{
    int x, y;
    x = get_parent(line[0]); y = get_parent(line[1]);
    if(x == y)
        return 0;
    else
    {
        parent[x] = y;
        return line[2];
    }
}