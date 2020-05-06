//asks for person's name, and greet the person
//
#include <iostream>
#include <string>

int main()
{
    //ask the person's name
    //
    std::cout <<"Please enter your first name:\n";

    //create and read in name
    //
    //variable object with name "name"
    //
    //object is part of computer memory with type
    //
    std::string name;

    //saves output into a buffer
    std::cin >> name;

    //greeting
    //
    std::cout << "Hello, " << name << "!\n\n" << std::endl;
    return 0;

    //EOF
    //
}