#include <iostream>
using namespace std;
  
int pageFaults(int n, int c, int pages[])
{
    int count = 0;
    vector<int> v;
    unordered_map<int, int> mp;
  
    int i;
    for (i = 0; i <= n - 1; i++) {
        auto it = find(v.begin(), v.end(), pages[i]);
        if (it == v.end()) {
            if (v.size() == c) {
                mp[v[0]]--;
                v.erase(v.begin());
            }
  
            v.push_back(pages[i]);
            mp[pages[i]]++;
            count++;
        }
        else {
            mp[pages[i]]++;
            v.erase(it);
            v.push_back(pages[i]);
        }
  
        int k = v.size() - 2;
  
        while (mp[v[k]] > mp[v[k + 1]] && k > -1) {
            swap(v[k + 1], v[k]);
            k--;
        }
    }
  
    return count;
}
  
int main(){  
    int pages[] = { 1, 2, 3, 4, 2, 1, 5 };
    int n = 7, c = 3; 
    cout << "Page Faults = " << pageFaults(n, c, pages)<< endl;
    cout << "Page Hits = " << n - pageFaults(n, c, pages);
    return 0;
}