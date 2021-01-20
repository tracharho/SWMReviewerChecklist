let comments = [];

fetch('static/checklist.json')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        appendData(data);
    })
    .catch(function (err) {
        console.log('error: ' + err);
    });
    
function appendData(data) {
    var mainContainer = document.getElementById("myData");
    for (var i = 0; i < data.length; i++) {
        var div = document.createElement("div");
        div.innerHTML = data[i].checkbox + ' ' + data[i].problem + data[i].comment + data[i].reference;
        div.setAttribute("id", ("row" + i));
        div.setAttribute("class", ("row"));
        mainContainer.appendChild(div);
    }
};

document.getElementById('submit').onclick = function() {
    var checkboxes = document.getElementsByName('cb');
    for (var checkbox of checkboxes) {
      if (checkbox.checked) {
        let cIndex = "c"+String(checkbox.id);
        let rIndex = "r"+String(checkbox.id);
        let comment = document.getElementById(cIndex);
        let reference = document.getElementById(rIndex);
        checkbox.value = comment.innerHTML + " (" + reference.innerHTML + ").";
        console.log(checkbox.value));
  }}
};