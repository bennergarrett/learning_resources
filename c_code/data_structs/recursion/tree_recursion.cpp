//implementation of tree recursion
//
#include <iostream>

using std::cout;
using std::endl;

//recursion statement
//
void fun(int n){
    //if n is more than 0
    //
    if(n>0){
        //output n
        //
        cout<<n<<endl;
        //self call
        //
        fun(n-1);
        //next only happens after previous has ended
        //
        fun(n-1);
    }
}


int main(){

    fun(3);
    return 0;

    // EOF
}