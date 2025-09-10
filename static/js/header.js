let menu = document.getElementById("menu");
let popup = document.getElementById("popup");
// let off = document.querySelector(".popup ul")

// off.style.display="none"

menu.addEventListener("click", function () {
    
  if (popup.style.display === "none") {
    popup.style.display = "block";
    document.body.style.overflow="hidden"
  } else {
    popup.style.display = "none";
    document.body.style.overflow="visible"

  }
});
