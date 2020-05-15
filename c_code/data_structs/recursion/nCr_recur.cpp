//codes showing how to do combination formula using recursion
// ncr = n!/r!(n-r)!

#include <iostream>
using std::cout; using std::endl;


int fact(int n){
    if(n==0) return 1;
    return fact(n-1)*n;
}

int nCr(int n, int r){
    int num, den;
    num = fact(n);
    den = fact(r)*fact(n-r);
    
    return num / den;
}

//recursive
//
int NCR(int n, int r){
    //base case
    //
    if(n==r || r==0){
        return 1;
    }
    //recursive
    //
    return NCR(n-1, r-1) + NCR(n-1, r);
}


int main(){

    cout << "nCr is: " << NCR(4, 2) << endl;
    return 0;
}