//get element

let image = document.querySelector(".image");
let gallery = document.querySelector(".gallery");
let items = document.querySelectorAll(".gallery > a > img");
let left = document.querySelector(".left");
let right = document.querySelector(".right");

//inital varible
let curr = 0;

console.log(items.length);

//next
right.onclick = function(){
    curr++;
    gallery.style.left = -curr * 980 + "px";
    if(curr >= items.length){
        curr = 0;
        gallery.style.left = "0px";
    }
}

//pervious
left.onclick = function(){
    curr--;
    gallery.style.left = -curr * 980 + "px";
    if(curr < 0){
        curr = items.length-1;
        gallery.style.left = "-3920px";
    }
}

//auto carousel
let time = setInterval(() => {
    right.onclick();
},5000);

//when mouse in
image.onmouseleave = function(){
    clearInterval(time);
}


//when mouse leave
image.onmouseleave = function(){
    let time = setInterval(() => {
        right.onclick();
    },5000);
}
