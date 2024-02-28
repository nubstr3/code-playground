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
      success: function (response) {
          console.log(response, expectedOutput)
      if (response.stdout.slice(0,-1)==expectedOutput) {
          document.getElementById("OutputCode").innerHTML = "&#10004; Correct, well done! Submit code and onto the next one :)";
          document.getElementById("formResult").value = 1;
        /* function to test hidden cases?*/
        /* document.getElementById("OutputCode").innerHTML = "Partially correct, check your code, some hidden test cases failed !!" */
      } else {
          document.getElementById("OutputCode").innerHTML = "&#215; Incorrect, better luck next time!";
          document.getElementById("formResult").value = 9;
          console.log(response);
        }
    },
    error: function(response) {
      console.log(response)
      alert("badrequest")
    }
  });
}

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
    window.open("/question/1", "_self");
}


function updateCode() {
    let e = ace.edit("editor");
    let theCode = e.getValue();
    let formattedCode = JSON.stringify(theCode);
    document.getElementById("formStudentsCode").value = formattedCode;

}