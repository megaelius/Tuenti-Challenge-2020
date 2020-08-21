#include<iostream>
#include<vector>
using namespace std;

bool fortress(int n, int& mh, int& ma)

int main(){
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; ++i){
        int n;
        cin >> n;
        int max_h, max_amount;
        bool out = fortress(n,max_h,max_amount);
        if(out){
            cout << "Case #" << i+1 << ": " << max_h << " " << max_amount << endl;
        }
        else cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
    }
}
