//Fibonacci series using recursion
//
//memoization allows for the reuse of previous answers
//otherwise execessive recursion
//
#include <iostream>
using std::cout; using std::endl;



int fib(int n){
    int t0=0, t1=1, s=0, i;
    //base case
    //
    if (n<=1){
        return n;
    }

    for(i=2; i<=n; ++i){
        s=t0+t1;
        t0=t1;
        t1=s;
    }
    return s;
}


int rfib(int n){
    //base case
    //
    if(n<= 1) return n;

    //recursive
    //
    return rfib(n-2) + rfib(n-1);
}

//Global for memoization
//
int F[10];

int mfib(int n){
    if(n<=1){
        F[n];
        return n;
    }
    //recursive
    //
    else{
        if(F[n-2] == -1)
            F[n-2]=mfib(n-2);
        if(F[n-1] == -1)
            F[n-1]=mfib(n-1);

        return F[n-2]+F[n-1];
    }
}

int main(){
    int i;
    for(i=0; i<10;++i){
        //-1 is not a fibonacci term
        //
        F[i]=-1;
    }
    int num = 10;
    cout << "loop is: "         << fib(num) << endl;
    cout << "Recursive is: "    << rfib(num) << endl;
    cout << "Memoization is: "    << mfib(num) << endl;
    return 0;
    //EOF
    //
}