#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

int main(){
    // one method for 2D array
    //
    //array of pointers
    //
    int *A[3];

    //each pointer points to array size 4
    //
    A[0] = new int[4];
    A[1] = new int[4];
    A[2] = new int[4];
    
    //example on how to access
    //
    A[1][2] = 15;




    //everything in heap
    //

    //double pointer
    //
    int **B;

    //first array of pointers
    //
    B = new int*[3];

    //second array
    //
    B[0] = new int[4];
    B[1] = new int[4];
    B[2] = new int[4];

    //accessed using nested for loops
    //row by columns
    //
    for(int i=0;i<3;++i)
        for(int j=0;j<4;++j)
            A[i][j] = i+1;

// completely in stack
//
//3 by 4
//
int C[3][4] = {{1,2,3,4}, {2,4,6,8}, {1,3,5,7}};

    return 0;
} 