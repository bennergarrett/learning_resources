//short program that counts from 10 down to -5
//
#include <iostream>
#include <string>

using namespace std;

int main(){
    int start = 10;
    const int end = -5;

    for(int num = start; num >= end; --num){
        cout << num << endl;
    }
    return 0;
}