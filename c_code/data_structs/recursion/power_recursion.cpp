//using recursion to do exponents
// n^n
//
#include <iostream>
using std::cout;    using std::endl;

int power(int m, int n){
    //base case
    //
    if(n == 0){
        return 1;
    }
    //simplify to reduce computation for recursive
    //
    //if even exponent using mod
    //
    if(n%2 == 0){
        return power(m*m, n/2);
    }
    //if odd exponent
    //
    else{
        return m*power(m*m, (n-1)/2);
    }
}


int main(){
    int r;
    r = power(3, 2);
    cout << r << endl;
    return 0;
    //EOF
    //
}