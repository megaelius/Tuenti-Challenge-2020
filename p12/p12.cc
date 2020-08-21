#include <iostream>
#include <vector>
#include <fstream>
#include <stdio.h>
using namespace std;

int main(){
    FILE *f=fopen("hex1.txt","r");
    unsigned long long p1;
    int ret = fscanf(f,"%x",&p1);
    cout << p1 << " " << ret << endl;
    fclose(f);
}
