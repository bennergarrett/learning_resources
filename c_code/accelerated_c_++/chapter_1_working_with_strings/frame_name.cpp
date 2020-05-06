#include <iostream>
#include <string>

using namespace std;

int main(){

cout << "Please Enter Your Name:\n";
string name;
cin >> name;

//build message to write
//
const string greeting = "Hello, " + name + "!";

//build lines of output
//
const string spaces(greeting.size(), ' ');
const string second = "* " + spaces + " *";

//build first and fifth lines
//
const string first(second.size(), '*');

//write all out
//
cout << endl;
cout << first << endl;
cout << second << endl;
cout << "* " << greeting << " *" << endl;
cout << second << endl;
cout << first << endl;

//EOF
//
}