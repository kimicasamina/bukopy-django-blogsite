console.log("Hello world")

const burgerMenuBtn = document.querySelector("#burger-menu-btn")
const closeMenuBtn = document.querySelector("#close-menu-btn")
const navMenu = document.querySelector("#nav")


console.log('burgermenu', burgerMenuBtn)
burgerMenuBtn.addEventListener("click", displayMobileMenu);
closeMenuBtn.addEventListener("click", closeMobileMenu);

// display and hide mobile menu
function displayMobileMenu(e) {
    burgerMenuBtn.classList.toggle("visible");
    closeMenuBtn.classList.toggle("visible");
    navMenu.classList.toggle("visible");
    console.log("DISPLAY MENU")
}

function closeMobileMenu(e) {
  burgerMenuBtn.classList.toggle("visible");
  closeMenuBtn.classList.toggle("visible");
  navMenu.classList.toggle("visible");
console.log("CLOSE MENU")
}