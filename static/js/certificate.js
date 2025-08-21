let form = document.getElementById("form")
let tag = document.querySelectorAll("#anchor")
// console.log(tag);


tag.forEach((a)=>{
a.addEventListener("click",()=>{
    // document.body.style.backgroundColor="red"
    
    form.style.left="50%"
    form.style.transition="5s"
    form.style.display="block";
})

})

// form.style.display="block";

