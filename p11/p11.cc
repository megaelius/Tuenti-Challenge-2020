#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <string>
#include <set>
#include <map>
using namespace std;

//nice, but we can do better
int sumandos(int n, set<int> permit){
    if(permit.empty() or n < 0)return 0;
    else if(n == 0) return 1;
    else{
        set<int> permit2 = permit;
        int max = *(--permit2.end());
        permit2.erase(max);
        return sumandos(n,permit2) + sumandos(n - max,permit);
    }
}

//yes sir, perfect for dynamic programming.
int sumandos_dyno(int n, set<int> permit, vector<vector<int>>& M){
    if(permit.empty() or n < 0)return 0;
    int& res = M[permit.size()][n];
    if(res == -1){
        if(n == 0) res = 1;
        else{
            set<int> permit2 = permit;
            int max = *(--permit2.end());
            permit2.erase(max);
            res = sumandos_dyno(n,permit2,M) + sumandos_dyno(n - max,permit,M);
        }
    }
    return res;
}

int main(){
    string line;
    getline(cin,line);
    istringstream iss1(line);
    int cases;
    iss1 >> cases;
    for(int i = 0; i < cases; ++i){
        string line2;
        getline(cin,line2);
        istringstream iss2(line2);
        int n;
        iss2 >> n;
        set<int> permit;
        for(int j = 1; j < n; ++j) permit.insert(j);
        int r;
        while(iss2 >> r)permit.erase(r);
        vector<vector<int>> M(n,vector<int>(n + 1,-1));
        cout << "Case #" << i+1 << ": " << sumandos_dyno(n,permit,M) << endl;
    }
}
