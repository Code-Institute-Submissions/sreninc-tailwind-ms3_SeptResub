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
    Swal.fire(message);
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