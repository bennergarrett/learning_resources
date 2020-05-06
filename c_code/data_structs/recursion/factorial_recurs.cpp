//example using recursion to get factorial
// N! = 1*2*3*4....*n
//
#include <iostream>
#include <string>

using std::cout;    using std::endl;


int fact(int n){
    //base case now including case for negative value
    //
    if(n == 0 || n < 0){
        return 1;
    }

    //recursion
    //
    else{
        return fact(n-1)*n;
    }
}

int Ifact(int n){
    int f=1;
    for(int i=1; i<=n;++i){
        f=f*i;
    }
    return f;
}

int main(){
    int r;
    r = fact(5);
    cout << r <<endl;
    return 0;

    //EOF
    //
}