#include <iostream>
#include <string>

using std::cin;     using std::endl;
using std::cout;    using std::string;

int main()
{
    //ask for the name
    //
    cout << "what is your name?\n";

    //read name
    //
    string name;
    cin >> name;

    //build the message that we want to write
    //
    const string greeting = "Hello, " + name + "!";

    //loop for constructing frame
    //

    //number of blanks surrounding greeting
    //
    const int pad = 1;

    //total rows to write
    //
    const int rows = pad * 2 + 3;

    //write rows of output
    //
    //int r = 0;

    //ensuring each column has same length in relation to input
    //
    const std::string::size_type cols = greeting.size() + pad * 2 + 2;

    //seperate output from input
    //
    cout << endl;

    //while loop
    //
    for (int r= 0; r != rows; ++r) {
        //write a row of output
        //
        //written c characters so far
        //
        std::string::size_type c = 0;

        //while not longer than frame columns
        //
        while (c != cols){
            //is it time to write greeting?
            //
            if (r == pad+1 && c == pad + 1){
                cout << greeting;
                c += greeting.size();
            }
            else {
                //are we on border?
                //
                if (r == 0 || r == rows - 1 ||
                    c == 0 || c == cols - 1)
                    cout << "*";   
                else
                    cout << " ";    
                ++c;
            }
        }
        cout << endl;
    }
    cout << endl;
    return 0;
    
    //EOF
    //
}