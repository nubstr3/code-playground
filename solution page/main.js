const submitAnswer = document.querySelector('#SubmitButton');


let editor = document.querySelector("#editor");

ace.edit(editor,  {
    theme: 'ace/theme/textmate',
    mode: 'ace/mode/python',
});

// run test code function
const mainCode = document.getElementById('mainCode').innerHTML;
const expectedOutput = document.getElementById('expectedOutput').innerHTML;


function runTestCode() {
    var editor = ace.edit("editor");
    var myCode = editor.getValue();
    var completeCode = myCode + "\n" + JSON.parse(mainCode);

    var myCodeJson = completeCode.trim();

    $.ajax({
      url:"http://143.110.155.198/jobe/index.php/restapi/runs",
      dataType:"json",
      data: {
        "run_spec": {"language_id":"python3", "sourcefilename": "test.py", "sourcecode": myCodeJson}
      },
      type: "post",
      headers: {
        Accept: "application/json; charset=utf-8"
      },
      success: function(response) {
        if (response.stdout.slice(0,-1)==expectedOutput) {
          document.getElementById("OutputCode").innerHTML = "&#10004; Correct, well done! Submit code and onto the next one :)";
          document.getElementById("formUsersOutput").value = response.stdout;
      
          /* function to test hidden cases?*/
          /* document.getElementById("OutputCode").innerHTML = "Partially correct, check your code, some hidden test cases failed !!" */
        } else {
           document.getElementById("OutputCode").innerHTML = "&#215; Incorrect, better luck next time!";
           console.log(response);
        }
      },
      error: function(response) {
        console.log(response)
        alert("badrequest")
  
      }
    });
  }


function updateCode() {
    let e = ace.edit("editor");
    let theCode = e.getValue();
    let formattedCode = JSON.stringify(theCode);
    document.getElementById("formStudentsCode").value = formattedCode;
  }
/* fetch("http://143.110.155.198/jobe/index.php/restapi/runs", {
  method: "POST",
  headers: { "Content-Type" : "application/json; charset-utf-8" },
  body: 
})
.then(res => {
  if (res.status >= 200 && res.status <= 299) { return res.json()}
  else {throw new Error('Something went wrong.');}
})
.then(data => {
  let resData = JSON.stringify(data);
  let resOutput = resData.stdout
  if (resOutput.slice(0,-2)==expectedOutput) {
    document.getElementById("OutputCode").innerHTML = "Correct, well done! Submit code and onto the next one :)";
  } else {
     document.getElementById("OutputCode").innerHTML = "Incorrect, better luck next time!";
  }
})
.catch(err => {
  document.getElementById("OutputCode").innerHTML = "Something went wrong, make sure you're using the correct function name.";
  console.log('Something went wrong');
})
}
// save code to db function at ip/api/student_submission/answers
const submitCode = function() {
  openPopup();
  var editor = ace.edit("editor");
  var myCode = editor.getValue();
  var completeCode = myCode + "\n" + mainCode;
  var myCodeJson = JSON.stringify(completeCode);

  let studentId = 123;
  let questionId = 123;


  fetch("codeplayground.club/api/student_submissions/answers", {
    method: "post",
    headers: { "Content-Type": "application/json; charset-utf-8" },
    body: {"student_id": 123, "question_id":123, "source_code": myCodeJson}
  })
  .then(res => {
    if (res.status===200) { return res.json()}
    else {throw new Error('Something went wrong.');}
  })
  .catch(err => {
    
  })
} */

// click to call functions
/* runTestCode.addEventListener('click', runCode); */
/* submitAnswer.addEventListener('click', submitCode); */


/* .then(responseJson => {
  dataReceived = JSON.parse(responseJson);
  output = dataReceived.stdout;
  if (output.slice(0, -2) == expectedOutput) {
    document.getElementById("OutputCode").innerHTML = "Correct, well done! Submit code and onto the next one :)";
  } else {
    document.getElementById("OutputCode").innerHTML = "Incorrect, better luck next time!";
  }
})
.catch(error => {
  document.getElementById("OutputCode").innerHTML = "Something went wrong, try again!";
  console.log('Something went wrong');
}) */

// test upload code to change context



  
 




     




var modal = document.getElementById("myModal");
var text = document.getElementById("HintButton");
text.onclick = function(){
  modal.style.display = "block";
}

var span = document.getElementsByClassName("close")[0];
span.onclick = function() {
  modal.style.display = "none";
}



let popup = document.getElementById("popup");

function openPopup(){
  popup.classList.add("open-popup");
}

function closePopup(){
  popup.classList.remove("open-popup");
}