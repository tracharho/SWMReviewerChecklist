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

//TO DO
//Set up higher layer looping to set the subcategories (i.e. put e&sc items in E&SC section)
function appendData(data) {
    var mainContainer = document.getElementById("myData");
    let collapsible = document.createElement("div");
    let anchor = document.createElement("a");
    anchor.setAttribute("href","javascript:;");
    anchor.setAttribute("onclick","show(this)");
    anchor.setAttribute("id", ("a1"));
    collapsible.innerHTML = "COLLAPSIBLE";
    collapsible.setAttribute("class","collapsible");
    collapsible.setAttribute("name", String("collapsible1"));
    mainContainer.appendChild(anchor);
    anchor.appendChild(collapsible);

    for (var i = 1; i < (1+data.length); i++) {
        let j = i-1;
        var div = document.createElement("div");
        div.innerHTML = data[j].checkbox + ' ' + data[j].problem + data[j].comment + data[j].reference;
        div.setAttribute("id", ("row" + i));
        div.setAttribute("class", ("row"));
        mainContainer.appendChild(div);
    }
};