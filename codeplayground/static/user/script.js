function editProfile() {
    window.open("/user/info", "_self");

}

function editPassword() {
    window.open("/user/pass", "_self");

}

function backToHome() {
    window.open("/home", "_self");

}

function escape() {
    window.open("/user", "_self");
}

function delay(time) {
    return new Promise(resolve => setTimeout(resolve, time));
}

function onDelete() {
    let confirmation = document.getElementById("confirmation");
    if (!confirmation.classList.contains("modal-open")) {
        confirmation.classList.add("modal-open");
    }
}

function onCancel() {
    let confirmation = document.getElementById("confirmation");
    confirmation.classList.remove("modal-open");
}

function onConfirm() {
    window.open("/user/dele", "_self");
}

document.addEventListener("DOMContentLoaded", () => {
    document
        .getElementById("confirmation")
        .addEventListener("click", onCancel);
    document
        .querySelector(".modal")
        .addEventListener("click", (e) => e.stopPropagation());
});