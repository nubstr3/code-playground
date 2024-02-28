function checkUsername(){
    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    
 

    if(username.length == 0 || email.length == 0){
        alert("Inputs need to be filled");
    } else {
        window.open("../profile/index.html", "_self");
    }
   
}

function escape() {
    window.open("../profile/index.html", "_self");
}