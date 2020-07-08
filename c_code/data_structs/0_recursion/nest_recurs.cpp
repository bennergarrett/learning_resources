//example code showing nested recursion
//
#include <iostream>

using std::cout;
using std::endl;

//recursive function that uses nested recursion
//
int fun(int n){
    if(n>100){
        return n-10;
    }
    return fun(fun(n+11));
}

//main code
//
int main(){
    int r;
    r = fun(95);
    cout << r << endl;
    return 0;

    //EOF
    //
}