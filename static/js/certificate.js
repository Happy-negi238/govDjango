let form = document.getElementById("form")
let tag = document.querySelectorAll("#anchor")

tag.forEach((a)=>{
    a.addEventListener("click",()=>{
    // document.body.style.backgroundColor="red"
    form.style.left="50%"
    form.style.transition="5s"
    form.style.display="block";
    })
})

const validation = (input) => {
    // console.log(input.value);  
    let sibling = input.nextElementSibling;
    
    if(input.value.trim().length === 0){
        input.style.borderBottomColor = "red";
        input.style.setProperty("--bkl", "red");
        sibling.style.visibility = "visible";
        sibling.style.marginTop = "2px";
        sibling.style.color = "red";
        sibling.style.paddingLeft = "8px";
        
    }else{
        input.style.borderBottomColor = "black";
        input.style.setProperty("--bkl", "black");
        sibling.style.visibility = "hidden";
        sibling.style.marginTop = "0px";    
        
    }
}

