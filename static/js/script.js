let mobileNav = document.getElementById("headerMobileNav");

function toggleMobileMenu() {
    if (mobileNav.classList.contains("invisible")) {
        mobileNav.classList.remove("invisible");
    } else {
        mobileNav.classList.add("invisible");
    }
}

function hideMobileMenu() {
    if (mobileNav.classList.contains("hidden")) {
        mobileNav.classList.remove("hidden");
    } else {
        mobileNav.classList.add("hidden");
    }
}

// To show popups
function generateFlashMessage(message) {
    if(message.includes("already")) {
        Swal.fire({
            title: "Action Failed",
            text: message,
            icon: "warning",
            confirmButtonColor: "#064e3b",
            confirmButtonText: "Okay"
        }).then((result) => {
        })
    } else {
        Swal.fire({
        title: "Success",
        html: message,
        confirmButtonColor: "#064e3b",
        confirmButtonText: "Okay",
        timer: 1000,
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

function loginModal() {
    let modal = document.getElementById("loginModal");
    if (modal.classList.contains("hidden")) {
        modal.classList.remove("hidden");
    } else {
        modal.classList.add("hidden");
    }
}

function signupModal() {
    let modal = document.getElementById("signupModal");
    if (modal.classList.contains("hidden")) {
        modal.classList.remove("hidden");
    } else {
        modal.classList.add("hidden");
    }
}