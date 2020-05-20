#include <algorithm>
#include <iomanip>
#include <ios>
#include <iostream>
#include <string>
#include <vector>
using std::cin; using std::sort;
using std::cout; using std::streamsize;
using std::endl; using std::string;
using std::setprecision; using std::vector;

int main(){
    //ask for students name
    //
    cout << "Please enter your first name:" << endl;
    string name;
    cin >> name;
    cout << "Hello, " << name << "!" << endl;

    //ask for and read the midterm and final grades
    //
    cout << "Please enter your midterm and final exam grades: ";
    double midterm, final;
    cin >> midterm >> final;

    //ask for homework grades
    //
    cout << "Enter all your homework grades, "
        "followed by end-of-file: ";


    //a variable to read inputs
    //
    double x;
    
    //vector to store all incoming values
    //
    vector<double> homework;

    //invariant
    //we have read count grades so far, 
    //and sum is the sum of the first count grades
    //
    while (cin >> x){
        //appends vector homework
        //
        homework.push_back(x);

    }

    //check that the student entered homework grades
    //
    //typedef creates a synonym for type
    //
    typedef vector<double>::size_type vec_sz;
    vec_sz size = homework.size();
    if (size == 0){
        cout << "You must enter your grades.  "
                "Please try again." << endl;
        return 1;
    }

    //sort grades
    //
    sort(homework.begin(), homework.end());

    //computre median homework grade
    //
    vec_sz mid = size/2;
    double median;

    //? is another way to do if / else
    //
    median = size % 2 == 0  ? (homework[mid] + homework[mid - 1]) / 2
                            : homework[mid];

   
    streamsize prec = cout.precision();


    cout << "Your final grade is " << setprecision(3)
         << 0.2 * midterm + 0.4 * final + 0.4 * median
         << setprecision(prec) << endl;

    return 0;   
}