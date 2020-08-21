#include <cstdio>
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <array>
using namespace std;

string exec(const char* cmd) {
    array<char, 128> buffer;
    string result;
    unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    if (!pipe) {
        throw runtime_error("popen() failed!");
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        result += buffer.data();
    }
    return result;
}

int main(){
    string command = "curl pre.steam-origin.contest.tuenti.net:9876/games/cat_fight/get_key";
    string out = exec(command.c_str());
    while(out == ""){
        out = exec(command.c_str());
    }
    cout << "FINAL:" << out;
}
