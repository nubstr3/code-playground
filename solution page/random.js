fetch("143.110.155.198/jobe/index.php/restapi/runs", {
    method: "POST",
    headers: { "Content-Type": "application/json; charset-utf-8" },
    body: {"run_spec": {"language_id":"python3", "sourcefilename": "test.py", "sourcecode": myCodeJson}}
})

  .then((response) => {
    if (response.status===200) {
      return response.json();
    } else {
      console.log("Status: " + response.status);
      return Promise.reject("server");
    }
  })

  .then((dataJson) => {
    dataReceived = JSON.parse(dataJson);
    //output = dataReceived.stdout;
    output = dataJson.stdout;
    document.getElementById("OutputCode").innerHTML = output;
  })

  .catch((err) => {
    if (err === "server") {
      return;
    };
    console.log(err)
    document.getElementById("OutputCode").innerHTML = "There was an error, try again!";

  })

  console.log(`Received: ${dataReceived}`)
