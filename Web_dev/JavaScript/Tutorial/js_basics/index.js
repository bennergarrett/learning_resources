// First Javascript Code

// Cannot be a reserved keyword
// should be meaningful
// cannots start with a number
//Cannot contain a space or hyphen
//Case-sensitive
let name = 'Garrett'; //String Literal
let age = 23; //Number Literal
let isApproved = true; //Boolean Literal (true/false)
//object literal {}
let person = {
  name:'Garrett',
  age: 23
};

//change object
//Dot notation
person.name = 'John'; //default choice
//bracket notation
person['name'] = 'Mary'; //for variables
console.log(name);
console.log(person);
console.log(person.name);

//camel notation
let firstName = null; //explicitly clear value of variable
let selectColor = null;

//constants
const interestRate = 0.3;
//creates error below
//interestRate = 1;
console.log(interestRate);

//array Literal
let selectedColors = ['red', 'blue'];
selectedColors[2] = 1; //dynamic, also various tyeps

//functions Perfom tasks
function greet(name, lastName){ //name is paramter of function
  console.log('Hello ' + name + ' ' + lastName);
}
//calculating a value
function square(number){
  return number * number;
}

//call functions
greet('John', 'Doe'); //arguement in function
greet('Mary', 'Smith'); //arguement in function
let number = square(2);
console.log(number);
console.log(square(2));
