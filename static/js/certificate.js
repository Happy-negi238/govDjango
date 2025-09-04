let form = document.getElementById("form")
let tag = document.querySelectorAll("#anchor")
let cross = document.getElementById("cross")
let input = document.getElementById("search")
let searchIcon = document.getElementById("search-icon")

tag.forEach((a)=>{
    a.addEventListener("click",()=>{
    document.body.style.backgroundColor="#808080"
    document.body.style.overflow="hidden"
    form.style.left="50%"
    // form.style.transition="0.2s linear"
    form.style.display="block";
    input.setAttribute("disabled" , "")
    input.style.backgroundColor="#808080"
    searchIcon.style.backgroundColor="#808080"
    })
})

cross.addEventListener("click", ()=>{
     document.body.style.backgroundColor="#f6f8fa"
    document.body.style.overflow="visible"
    form.style.left="50%"
    // form.style.transition="0.2s linear"
    form.style.display="none";
    input.removeAttribute("disabled" , "")
    input.style.backgroundColor="#f6f8fa"
    searchIcon.style.backgroundColor="#f6f8fa"
    
    let name = document.getElementById('name');
    let phone = document.getElementById('phone');
    let user_id = document.getElementById('user_id');

    name.value = '';
    phone.value = '';
    user_id.value = '';
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
document.getElementById('checkForm').addEventListener('submit', function(e){
    e.preventDefault();
    let formData = new FormData(this);
    fetch("/check_userId/", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        if(data.status == "success"){
            // console.log(data.message);
            window.open(data.download_url, "_blank");
        }
        else{
            alert(data.message)
        }
    })
})