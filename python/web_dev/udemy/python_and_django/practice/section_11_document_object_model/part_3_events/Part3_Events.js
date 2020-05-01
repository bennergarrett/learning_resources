// defining headers by // ID
//
var headOne = document.querySelector('#one')
var headTwo = document.querySelector('#two')
var headThree = document.querySelector('#three')

// testing if variables above worked
//
console.log("connected")

//there is list of event names | check google
//
//adding event listener can change page, takes command and function
//
headOne.addEventListener('mouseover', function(){
  headOne.textContent = "Mouse Currently Over";
  headOne.style.color = "red";
})

headOne.addEventListener('mouseout', function(){
  headOne.textContent = "Hover Over Me!"
  headOne.style.color = 'black';

})

headTwo.addEventListener("click", function(){
  headTwo.textContent = 'CLICKED ON';
  headTwo.style.color = 'blue';

})

headThree.addEventListener("dblclick",function(){
  headThree.textContent = "Double Clicked!";
  headThree.style.color = 'red';
})
