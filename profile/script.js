function editProfile() {
    window.open("../profile form/index.html", "_self");

}

function editPassword() {
    window.open("../password form/index.html", "_self");

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
    onCancel();
  }
  
  document.addEventListener("DOMContentLoaded", () => {
    document
      .getElementById("confirmation")
      .addEventListener("click", onCancel);
    document
      .querySelector(".modal")
      .addEventListener("click", (e) => e.stopPropagation());
  });