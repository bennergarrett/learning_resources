//sum a natural number recursively
//
//it is faster to directly use formula
//n*(n+1)/2 which is constant time
//
//faster to also use loop
//

#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

int sumOf(int n){
    //base case
    //
    if(n==0){
        return 0;
    }

    //recursive case
    //
    else{
        return sumOf(n-1)+n;
    }
}

//iterative solution
//
int Isum(int n){
    int s=0;
    for(int i = 1; i <= n; ++i){
        s=s+i;
        //cout << "s is now: " << s << endl;
    }   
    return s;
}

int main(){
    int r;
    r = sumOf(5);
    int i;
    i = Isum(5);

    //outputs final values
    //
    cout << "recursive value: " << r << endl;
    cout << "iterative value: " << i << endl;

    return 0;
}