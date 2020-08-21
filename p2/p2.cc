#include <iostream>
using namespace std;

int main(){
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; ++i){
        int N;
        cin >> N;
        int best;
        for(int j = 0; j < N; ++j){
            int A,B,C;
            cin >> A >> B >> C;
            int w = (C) ? A : B;
            //we check if someone has won our best player so far
            if(j == 0 or ((B == best or A == best) and w != best))best = w;
        }
        cout << "Case #" << i + 1 << ": " << best << endl;
    }
}
