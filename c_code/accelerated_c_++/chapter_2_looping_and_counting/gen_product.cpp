//program that generates product of numbers in
//given range

#include <iostream>
#include <string>

using std::cin; using std::cout;
using std::string; using std::endl;

int main(){
    const int prod_max = 10;
    int product = 1;
    for(int i = 1; i <= prod_max; ++i){
        product = product * i;
        cout << product << endl;

    }

    return 0;
}