//Write a program to count word freq
//original was to count distinct words but I misread
//would require to keep track of existing words using map or vector
//
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

    cout << "please input your list of words: " << endl;

    //temp variable
    //
    string x;

    //list of words
    //
    vector<string> words;

    //enter words
    //
    while(cin >> x && x != ""){
        words.push_back(x);

    }
    //a typedef suitable for holding a vectors size
    //
    typedef vector<double>::size_type vec_sz;
    vec_sz size = words.size();

    //edge case
    //
    if(words.size() == 0){
        cout << "No words detected, please try again" <<endl;
        return 1;
    }

    //total sum
    //
    int sum = 0;

    //temp sum
    //
    int counter = 0;

    //current word
    //
    string cur_w;

    //highest freq word
    //
    string top_w;


    //start at end to pop off word
    //
    while (words.size() > 0){
        cur_w = words.back();
        counter = count(words.begin(), words.end(), cur_w);

        //pop off last word so it is no longer used
        //alternative to create another vector storing found words
        //or use map possibly
        //
        words.pop_back();

        //if count is higher than sum, new word higher freq
        //
        if (counter > sum){
            sum = counter;
            top_w = cur_w;
        }
    }

    cout << "Top Word: " <<  top_w << endl;
    cout << "Frequency is: " << sum << endl;
    return 0;
}