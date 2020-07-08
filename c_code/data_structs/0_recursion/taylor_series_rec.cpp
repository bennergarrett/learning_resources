//taylor series using recursion
//e^x = 1 + x/1 + 2^2/2!
//

#include <iostream>
using std::cout;    using std::endl;

//n is precision
//
double taylor(int x, int n){

    static double p=1, f=1;
    //result
    //
    double r;
    //base case
    //
    if(n == 0){
        return 1;
    }
    //recursive
    //
    else{
        r = taylor(x, n-1);
        //power
        //
        p = p*x;
        //factorial
        //
        f = f*n;
        return r + p/f;
    }
}


int main(){
    cout << taylor(4, 10) << endl;
    return 0;
}