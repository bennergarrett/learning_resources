// Write a program to report the length of the 
// longest and shortest string in its input.

#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>
#include <string>
#include <vector>

using std::cin;             using std::sort;
using std::cout;            using std::streamsize;
using std::endl;            using std::string;
using std::vector;     

int main(){

    cout << "Enter list of words: " <<endl;

    string temp;
    vector<string> words;

    while( cin >> temp && temp != ""){
        words.push_back(temp);
    }

    // a typedef suitable for holding a vectors size
    // or just use auto
    typedef vector<string>::size_type vec_size;
    vec_size size = words.size();

    //edge case
    //
    if(words.size() == 0){
        cout << "No words detected, please try again" <<endl;
        return 1;
    }

    
    int small_total =  words[0].size();
    int large_total = small_total;
    int temp_total = small_total;
    string small_w = words[0];
    string big_w = small_w;

    for(int x = 1; x < size; ++x){
        temp_total = words[x].size();

        if(temp_total < small_total ){
            small_total = temp_total;
            small_w = words[x];
        }
        if(temp_total > large_total){
            large_total = temp_total;
            big_w = words[x];
        }
    }
    cout << "Smallest word is: " << small_w << " at "
         << small_total << " letters" << endl;
    cout << "Largest word is: " << big_w << " at "
         << large_total << " letters" << endl;
    return 0;
}