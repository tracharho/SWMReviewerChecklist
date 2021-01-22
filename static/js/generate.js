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
};
    for (var i = 0; i < (data.length); i++) {
        for (var j = 0; j < (data[i].length); j++) {
            for (var k = 0; k < (data[i][j].length); k++) {
                var div = document.createElement("div");
                div.innerHTML = data[i][j][k];
                div.setAttribute("id", ("row" + i));
                div.setAttribute("class", ("row"));
                mainContainer.appendChild(div);
        }
    }
};