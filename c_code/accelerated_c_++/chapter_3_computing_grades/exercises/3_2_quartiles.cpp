//Write a program to compute and print the quartiles 
//(that is, the quarter of the numbers with the largest values,
//the next highest quarter, and so on) of a set of integers.
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
using std::setprecision;    using std::vector;

int main(){

    cout << "Input list of numbers to see Quartile output: " << endl;

    //for inputs
    //
    double x;

    vector<double> numbers;

    while(cin >> x){
        numbers.push_back(x);
    }

    //typedef vector<double>::size_type vec_size;
    //replaces the above
    //
    auto size = numbers.size();


    if(size < 4){
        cout << "Please input at least 4 numbers.  "
                "Try again." << endl;
        return 1;
    }

    sort(numbers.begin(), numbers.end());

    //compute quartile value
    //
    auto mid = size/2;
    auto upper = (size + mid)/2;
    auto lower = mid / 2;

    double median, lowerQt, upperQt;

    median = size % 2 == 0 ? (numbers[mid] + numbers[mid - 1]) / 2 : numbers[mid];
    lowerQt = mid % 2 == 0 ? (numbers[lower] + numbers[lower - 1]) / 2 : numbers[lower];
    upperQt = mid % 2 == 0 ? (numbers[upper] + numbers[upper - 1]) / 2 : numbers[upper];

    cout << lowerQt  <<  " " << median <<  " " << upperQt << endl;
    
 
    return 0;   
}