//gives array
//
var box = document.querySelectorAll('.col')
var i = 0;
var state;


//functions
//

//reset game
//
function reset(){
  for(let i=0; i < box.length; i++){
    box[i].textContent = '';

  }
}
//generic solution
//
function changeMarker(){
  if(this.textContent ===''){
    this.textContent = 'X';

  }else if (this.textContent ==='X'){
    this.textContent = 'O';

  }else {
    this.textContent='';
  }

}




for(let i= 0; i < box.length;i++){
  box[i].addEventListener('click', function(){
    //box[i].textContent = 'clicked';
    console.log(box[i].innerHTML)
    if (box[i].innerHTML == 0 || box[i].textContent === ''){
      box[i].textContent = 'X';
    }
    else if (box[i].textContent === 'X'){
      box[i].textContent = 'O'
    }
    else if (box[i].textContent === 'O'){
      box[i].textContent = ''
    }

  })

};

// box.addEventListener('mouseover', function(){
//   box.textContent = "mouse currently over";
//
//
// })
