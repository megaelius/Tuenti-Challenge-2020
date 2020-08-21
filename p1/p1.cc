#include<iostream>
using namespace std;

char RPS(char a, char b){
    if(a == b)return '-';
    else if(a == 'R'){
        if(b == 'S')return a;
        else return b;//b == 'P'
    }
    else if(a == 'P'){
        if(b == 'R')return a;
        else return b;//b == 'S'
    }
    else{
        if(b == 'P')return a;
        else return b;//b == 'R'
    }
}

int main(){
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; ++i){
        char a, b;
        cin >> a >> b;
        cout << "Case #" << i + 1 << ": "<< RPS(a,b) << endl;
    }
}
