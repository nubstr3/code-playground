let editor = document.querySelector("#editor");
const UploadBtn = document.querySelector("#uploadBtn");


ace.edit(editor,  {
    theme: 'ace/theme/textmate',
    mode: 'ace/mode/python',
});

let popup = document.getElementById("popup");

function openPopup() {
    popup.classList.add("open-popup");
}

function closePopup() {
    popup.classList.remove("open-popup");
    window.open("/question/1", "_self");
}

function closePopup2() {
    popup.classList.remove("open-popup");
    window.open("/discussion/1", "_self");
}

const expectedOutput = document.getElementById('expected').innerHTML;

// run test code with main function
function runTestCode() {
  var editor = ace.edit("editor");
  var myCode = editor.getValue();
  var completeCode = myCode;

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
      let outputCode = response.stdout;
      document.getElementById("OutputCode").innerHTML = outputCode;
      
    },
    error: function(response) {
      console.log(response)
      alert("badrequest")

    }
  });
}


function updateTitleValue() {
  document.getElementById("formTitle").value = document.getElementById("input").value;

}

function updateTopicValue(var1) {
  document.getElementById("formTopic").value = var1;
}

function updateDescriptionValue() {
  document.getElementById("formDescription").value = document.getElementById("description").value;

}

function updateFunctionValue() {
  document.getElementById("formFunctionName").value = document.getElementById("functionName").value;

}

function updateCode() {
  let e = ace.edit("editor");
  let theCode = e.getValue();
  let formattedCode = JSON.stringify(theCode);
  document.getElementById("formMainCode").value = formattedCode;
}

function updateExpectedValue() {
  document.getElementById("formExpectedOutput").value = document.getElementById("expected").value;

}

function updateDiffValue(var2) {
  document.getElementById("formDifficulty").value = var2;
}

function updateHintValue() {
  document.getElementById("formHint").value = document.getElementById("hint").value;

}









