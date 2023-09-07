const bars = document.querySelector(".bars");
const navbar = document.querySelector(".nav-bar");

bars.addEventListener("click", () =>{
  bars.classList.toggle("active");
  navbar.classList.toggle("active");
})