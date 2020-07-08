#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

int main(){


    ///////////////
    /////for c/////
    ///////////////

    // pointers for dynamic array
    // 
    int *p, *q;

    // int type pointer using malloc to size for 5 ints
    //
    p=(int *)malloc(5*sizeof(int));
    p[0]=3;p[1]=5;p[2]=7;p[3]=9;p[4]=11;

    // to resize
    //
    q=(int *)malloc(10*sizeof(int));
    int i;

    for(i=0; i<5; i++){
        q[i] = p[i];
    }

    //delete previous array to free memory
    //
    free(p);

    //point p to q
    //
    p=q;

    //q not pointing anywhere
    //
    q=NULL;
    for(i=0;i<5;++i)
        cout << p[i] << endl;


    ///////////////
    ////for c++////
    ///////////////

    //for dynamic storage
    //
    int *s = new int(5);
    int *r = new int(10);
    s[0]=3;s[1]=5;s[2]=7;s[3]=9;s[4]=11;
    

    //copy contents to larger array
    //
    for(i=0;i<5; ++i){
        r[i]=s[i];
    }

    //free s array and change pointer
    //
    delete [] s;
    s = r;

    //remove non used pointer
    //
 

    for(i=0;i<5;++i)
        cout << s[i] << endl;
    
    delete s;
    // delete r;

    return 0;
}