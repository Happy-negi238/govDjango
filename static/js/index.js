const accordians = document.querySelectorAll(".accordian");

accordians.forEach(accor => {
    const icon = accor.querySelector('.icon');
    const answer = accor.querySelector('.answer');
    
    accor.addEventListener('click', () => {
        if(icon.classList.contains('active')){
            icon.classList.remove('active');
            answer.style.maxHeight = null;
        } else{
            icon.classList.add('active');
            answer.style.maxHeight = answer.scrollHeight + "px";
        }
    })
});
