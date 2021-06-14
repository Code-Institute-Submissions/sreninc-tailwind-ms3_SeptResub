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

let userMenu = document.getElementById("toggleUserMenu");

function toggleUserMenu() {
    if (userMenu.classList.contains("invisible")) {
        userMenu.classList.remove("invisible");
    } else {
        userMenu.classList.add("invisible");
    }
}

function filterBookings() {
    date = document.getElementById("filterDate");
    date ? date = date.value : date = "";
    if (document.getElementById("filterStatus")) {
        status = document.getElementById("filterStatus").value;
    } else {
        status= "all";
    }
    window.open('/bookings/date/' + date + '/status/' + status, '_self');
}

// To show popups
function generateFlashMessage(message) {
    if(message.includes("already")) {
        Swal.fire({
            title: 'Action Failed',
            text: message,
            icon: 'warning',
            confirmButtonColor: '#3085d6',
            confirmButtonText: 'Okay'
        }).then((result) => {
        })
    } else {
        Swal.fire({
        title: 'Success',
        html: message,
        timer: 1000,
        timerProgressBar: true,
        didOpen: () => {
            Swal.showLoading()
            timerInterval = setInterval(() => {
            const content = Swal.getHtmlContainer()
            if (content) {
                const b = content.querySelector('b')
                if (b) {
                b.textContent = Swal.getTimerLeft()
                }
            }
            }, 100)
        },
        willClose: () => {
            clearInterval(timerInterval)
        }
        }).then((result) => {
        /* Read more about handling dismissals below */
        if (result.dismiss === Swal.DismissReason.timer) {
            console.log('I was closed by the timer')
        }
        })
    }

}

function confirmDeleteBooking(id) {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href="/delete_booking/" + id;
        }
    })
}

function confirmDeleteGuest(id) {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href="/delete_guest/" + id;
        }
    })
}

function confirmDeleteUser(id) {
    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href="/delete_user/" + id;
        }
    })
}

function starRating(number) {
    container = document.getElementById("starRating");
    document.getElementById("rating").value = parseInt(number) + 1;
    container.innerHTML = "";
    let x = 0;
    for (let i = 0; i < 5; i++) {
        x = i;
        if (i <= number) {
            let full = `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 inline text-yellow-400" viewBox="0 0 20 20" fill="currentColor" onclick="starRating('${x}')">
                            <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                        </svg>`;
            container.insertAdjacentHTML(
                'beforeend',
                full
            )
        } else {
            let empty = `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 inline text-yellow-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" onclick="starRating('${x}')">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                        </svg>`;
            container.insertAdjacentHTML(
                'beforeend',
                empty
            )
        }
    }
}

function tooltip(type) {
    if (type == "guest") {
        tippy('.bookler-system-set', {
            content: 'This is set by the system',
        });
    };

    if (type == "booking") {
        tippy('.bookler-booking', {
            content: 'Edit this field on the guests profile page',
        });      
    }
}

// https://stackoverflow.com/questions/454202/creating-a-textarea-with-auto-resize

const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
}

function OnInput() {
  this.style.height = "auto";
  this.style.height = (this.scrollHeight) + "px";
}