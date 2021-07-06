//Global to app functions
// auto search function for nav
let typingTimer;                //timer identifier
let doneTypingInterval = 1000;  //time in ms (1 second)
let myInput = document.getElementById("search");

//on keyup, start the countdown
myInput.addEventListener("keyup", () => {
    clearTimeout(typingTimer);
    if (myInput.value) {
        typingTimer = setTimeout(doneTyping, doneTypingInterval);
    }
});

//user is "finished typing," do something
function doneTyping () {
    window.location.href="/guests/" + myInput.value;
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
    if (document.getElementById("filterDate")) {
        let date = date.value;
    } else {
        date = "";
    }
    if (document.getElementById("filterStatus")) {
        status = document.getElementById("filterStatus").value;
    } else {
        status= "all";
    }
    window.open("/bookings/date/" + date + "/status/" + status, "_self");
}

function confirmDeleteBooking(id) {
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href="/delete_booking/" + id;
        }
    })
}

function confirmDeleteGuest(id) {
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href="/delete_guest/" + id;
        }
    })
}

function confirmDeleteUser(id) {
    Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href="/delete_user/" + id;
        }
    });
}

function starRating(number) {
    container = document.getElementById("starRating");
    document.getElementById("rating").value = parseInt(number) + 1;
    container.innerHTML = "";
    let x = 0;
    for (let i = 0; i < 5; i++) {
        x = i;
        if (i <= number) {
            let full = `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 inline text-yellow-400" viewBox="0 0 20 20" fill="currentColor" stroke="currentColor" onclick="starRating('{{ x }}')">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                        </svg>`;
            container.insertAdjacentHTML(
                "beforeend",
                full
            )
        } else {
            let empty = `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 inline text-yellow-400" fill="none" viewBox="0 0 24 24" stroke="currentColor" onclick="starRating('${x}')">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
                        </svg>`;
            container.insertAdjacentHTML(
                "beforeend",
                empty
            )
        }
    }
}

function tooltip(type) {
    if (type == "guest") {
        tippy(".bookler-system-set", {
            content: "This is set by the system",
        });
    };

    if (type == "booking") {
        tippy(".bookler-booking", {
            content: "Edit this field on the guests profile page",
        });
    }
}

//auto resize textareas
const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
}

function OnInput() {
  this.style.height = "auto";
  this.style.height = (this.scrollHeight) + "px";
}

function  stylePagination() {
    let pagination = document.querySelector(".pagination").getElementsByTagName("LI");
    let newPagination = document.createElement("nav");
    newPagination.classList.add("border-t", "border-gray-200", "px-4", "flex", "items-center", "justify-between", "sm:px-0", "mt-12");

    let firstDiv = document.createElement("div");
    firstDiv.classList.add("firstPaginationDiv", "-mt-px", "w-0", "flex-1", "flex");
    newPagination.appendChild(firstDiv);

    let middleDiv = document.createElement("div");
    middleDiv.classList.add("middlePaginationDiv", "hidden", "md:-mt-px", "md:flex");
    newPagination.appendChild(middleDiv);

    let lastDiv = document.createElement("div");
    lastDiv.classList.add("lastPaginationDiv", "-mt-px", "w-0", "flex-1", "flex", "justify-end");
    newPagination.appendChild(lastDiv);

    for (let element of pagination) {
        let anchor = element.firstChild;
        if(element.classList[0] && element.classList[0] == "previous") {
            anchor.classList.add(element.classList[0], "border-t-2", "border-transparent", "pt-4", "pr-1", "inline-flex", "items-center", "text-sm", "font-medium", "text-gray-500", "hover:text-gray-700", "hover:border-gray-300");
            anchor.innerHTML = `<svg class="mr-3 h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
        <path fill-rule="evenodd" d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z" clip-rule="evenodd" />
      </svg>`;
            newPagination.getElementsByClassName("firstPaginationDiv")[0].appendChild(anchor);
        } else if (element.classList[0] && element.classList[0] == "next") {
            anchor.classList.add(element.classList[0], "border-t-2", "border-transparent", "pt-4", "pl-1", "inline-flex", "items-center", "text-sm", "font-medium", "text-gray-500", "hover:text-gray-700", "hover:border-gray-300");
            anchor.innerHTML = `<svg class="ml-3 h-5 w-5 text-gray-400" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
        <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd" />
      </svg>`;
            newPagination.getElementsByClassName("lastPaginationDiv")[0].appendChild(anchor);
        } else if (element.classList[0] &&  element.classList[0] == "active") {
            anchor.classList.add(element.classList[0], "border-indigo-500", "text-indigo-600", "border-t-2", "pt-4", "px-4", "inline-flex", "items-center", "text-sm", "font-medium");
            newPagination.getElementsByClassName("middlePaginationDiv")[0].appendChild(anchor);
        } else if (element.classList[0] && element.classList[0] == "disabled") {
            anchor.classList.add(element.classList[0], "border-transparent", "text-gray-500", "border-t-2", "pt-4", "px-4", "inline-flex", "items-center", "text-sm", "font-medium");
            newPagination.getElementsByClassName("middlePaginationDiv")[0].appendChild(anchor);
        } else {
            anchor.classList.add(element.classList[0], "border-transparent", "text-gray-500", "hover:text-gray-700", "hover:border-gray-300", "border-t-2", "pt-4", "px-4", "inline-flex", "items-center", "text-sm", "font-medium");
            newPagination.getElementsByClassName("middlePaginationDiv")[0].appendChild(anchor);
        }

        if(anchor.href) {
            anchor.setAttribute("href", anchor.getAttribute("href") + "#pagePagination");
        }
    }
    document.getElementById("pagePagination").appendChild(newPagination);
}