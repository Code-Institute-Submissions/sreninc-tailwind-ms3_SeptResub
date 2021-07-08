let mobileNav = document.getElementById("headerMobileNav");

// Toggles mobile nav menu on website pages
function toggleMobileMenu() {
    if (mobileNav.classList.contains("invisible")) {
        mobileNav.classList.remove("invisible");
    } else {
        mobileNav.classList.add("invisible");
    }
}

// Toggles mobile nav menu on app pages
function hideMobileMenu() {
    if (mobileNav.classList.contains("hidden")) {
        mobileNav.classList.remove("hidden");
    } else {
        mobileNav.classList.add("hidden");
    }
}

// Shows sweetalert2 popup alerts
function generateFlashMessage(message) {
    if(message.includes("already")) { 
        Swal.fire({ // Failed Message
            title: "Action Failed",
            text: message,
            icon: "warning",
            confirmButtonColor: "#064e3b",
            confirmButtonText: "Okay"
        }).then((result) => {
        })
    } else {
        Swal.fire({ // Success Message
        title: "Success",
        html: message,
        confirmButtonColor: "#064e3b",
        confirmButtonText: "Okay",
        timer: 1500,
        icon: "success",
        didOpen: () => {
            timerInterval = setInterval(() => {
            const content = Swal.getHtmlContainer()
            if (content) {
                const b = content.querySelector("b")
                if (b) {
                b.textContent = Swal.getTimerLeft()
                }
            }
            }, 250)
        },
        willClose: () => {
            clearInterval(timerInterval)
        }
        })
    }
}

// Shows login modal
function loginModal() {
    let modal = document.getElementById("loginModal");
    if (modal.classList.contains("hidden")) {
        modal.classList.remove("hidden");
    } else {
        modal.classList.add("hidden");
    }
}

// Shows signup modal 
function signupModal() {
    let modal = document.getElementById("signupModal");
    if (modal.classList.contains("hidden")) {
        modal.classList.remove("hidden");
    } else {
        modal.classList.add("hidden");
    }
}

// Toggles login error modal 
function loginErrorModal() {
    let modal = document.getElementById("loginErrorModal");
    modal.classList.add("hidden");
}