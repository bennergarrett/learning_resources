//reduces Taylor to O(n)
//
#include <iostream>

using std::cout;    using std::endl;

//loop method
//
double le(int x, int n){

    double s = 1;
    for(int i = s; n>0; --n){
        s = 1+s*x/n;
    }
    return s;
}

double re(int x, int n){
    static double s=1;
    //base case
    //
    if(n==0){
        return s;
    }
    //recursive
    //
    s = 1+x*s/n;
    return re(x, n-1);
}

int main(){
    int num = 1;
    int prec = 10;
    double looping, recursive;
    looping = le(num, prec);
    recursive = re(num, prec);
    cout << "looping answer: " << looping << endl;
    cout << "recursive answer: " << recursive << endl;

    return 0;
}