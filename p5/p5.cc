#include <iostream>
#include <cmath>
using namespace std;

long long int tuentisumandos(long long int& N){
    long long int D = N/20;
    if(D == 0)return 0;
    int R = N%20;
    if(double(R)/D <= 9)return D;
    else return 0;
}

int main(){
    int cases;
    cin >> cases;
    long long int N,result;
    for(int i = 0; i < cases; ++i){
        cin >> N;
        result = tuentisumandos(N);
        if(result == 0){
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        }
        else cout << "Case #" << i+1 << ": " << result << endl;
    }
}
