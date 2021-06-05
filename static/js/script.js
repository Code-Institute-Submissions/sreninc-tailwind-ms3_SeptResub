let mobileNav = document.getElementById("headerMobileNav");
console.log(mobileNav);

function toggleMobileMenu() {
    if (mobileNav.classList.contains("invisible")) {
        mobileNav.classList.remove("invisible");
    } else {
        mobileNav.classList.add("invisible");
    }
}