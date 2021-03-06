fetch('static/csv.json')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        appendData(data);
    })
    .catch(function (err) {
        console.log('error: ' + err);
    });

function setAttributes(el, attrs) {
    for(var key in attrs) {
      el.setAttribute(key, attrs[key]);
    }
  }
/*
cat: category object
sub: subcategory
x: string of the category object
y: string of subcategory object
*/ 
function appendData(data) {
    var mainContainer = document.getElementById("myData");
    let cat = data[0];
    let catIDNumber = 1;
    let subIDNumber = 0;
    for (let x in cat) {
        //console.log(x); //category
        let catAnchor = document.createElement("a");
        setAttributes(catAnchor, {
                            "onclick":"show(this)",
                            "id":String(catIDNumber),
                            "name":String(x),
                            "class":"catAnchor"});
        catAnchor.style.display = "flex";
        //"href": "function.js",
        let catCollapsible = document.createElement("div");
        setAttributes(catCollapsible, {"class":"catCollapsible",
                            "name":String(x),
                            "id":'catCollapsible'+String(catIDNumber)});

        catCollapsibleHeader = document.createElement("h2");
        catCollapsibleHeader.innerHTML = x;
        catCollapsibleHeader.setAttribute("class","catHeader");
        catCollapsible.appendChild(catCollapsibleHeader);

        catAnchor.appendChild(catCollapsible);
        mainContainer.append(catAnchor);
        if (cat[x].length === 1) {
            let sub = cat[x][0];
            for (let y in sub) {
                subIDNumber++;
                let subAnchor = document.createElement("a");
                setAttributes(subAnchor, {
                                "onclick":"show(this)",
                                "id":'subcategory-'+String(subIDNumber),
                                "class":"subAnchor"});
                //"href":"static/js/functions.js",
                let subCollapsible = document.createElement("div");
                setAttributes(subCollapsible, {"class":"subCollapsible",
                                    "name": "subcategory-"+String(x),
                                    "id":'sub'+String(subIDNumber)});
                subCollapsibleHeader = document.createElement("h2")
                subCollapsibleHeader.setAttribute("class","subHeader");
                subCollapsibleHeader.innerHTML = y;
                subCollapsible.style.display = "none";
                subCollapsible.appendChild(subCollapsibleHeader);
    
                subAnchor.appendChild(subCollapsible);
                mainContainer.append(subAnchor);
                let rows = sub[y];
                for (let z = 0; z < rows.length; z++) {
                    let w = rows[z];
                    let rowcontainer = document.createElement("div");
                    setAttributes(rowcontainer, {"class":"row",
                                "name" : "rowsub"+String(subIDNumber),
                                "class": "rowcontainer",
                                "id":String("rowcontainer-"+ w['rownum'])});
                    rowcontainer.style.display = "none";
                    
                    let cb = document.createElement("INPUT");
                    setAttributes(cb, {"class":"cb",
                                "name":"checkbox",
                                "type":"checkbox",
                                "id": String(w['rownum'])});
                    
                    let criteria = document.createElement("p");
                    setAttributes(criteria, {"class":"criteria",
                                "name":"criteria",
                                "id": "criteria-"+w['rownum']});
                    criteria.innerHTML = w['Criteria'];

                    let comment = document.createElement("input");
                    setAttributes(comment, {"class":"comment",
                                "name":"comment",
                                "id": "comment-"+w['rownum'],
                                "type":"text",
                                "placeholder":w['Comment']
                            });
                    
                    let reference = document.createElement("p");
                    setAttributes(reference, {"class":"reference",
                                "name":"reference",
                                "id": "reference-"+w['rownum']});
                    reference.innerHTML = w['Reference'];

                    rowcontainer.appendChild(cb);
                    rowcontainer.appendChild(criteria);
                    rowcontainer.appendChild(comment);
                    rowcontainer.appendChild(reference);
                    mainContainer.appendChild(rowcontainer);
                }
                
            }
                
        }
        else {
            for (let a = 0; a < cat[x].length; a++) {
                let sub = cat[x][a];
            for (let y in sub) {
                subIDNumber++;
                let subAnchor = document.createElement("a");
                setAttributes(subAnchor, {
                                "onclick":"show(this)",
                                "id":'subAnchor'+String(subIDNumber),
                                "class":"subcategory-"+String(catIDNumber)});
    
                let subCollapsible = document.createElement("div");
                setAttributes(subCollapsible, {"class":"subCollapsible",
                                    "name": "subcategory-"+String(x),
                                    "id":'sub'+String(subIDNumber)});
                subCollapsibleHeader = document.createElement("h2")
                subCollapsibleHeader.setAttribute("class","subHeader");
                subCollapsibleHeader.innerHTML = y;
                subCollapsible.appendChild(subCollapsibleHeader);
                subCollapsible.style.display = "none";

                subAnchor.appendChild(subCollapsible);
                mainContainer.append(subAnchor);
                let rows = sub[y];
                for (let z = 0; z < rows.length; z++) {
                    let w = rows[z];
                    let rowcontainer = document.createElement("div");
                    setAttributes(rowcontainer, {"class":"row",
                                "name" : "rowsub"+String(subIDNumber),
                                "class": "rowcontainer",
                                "id":String("rowcontainer-"+ w['rownum'])});
                    rowcontainer.style.display = "none";

                    let cb = document.createElement("INPUT");
                    setAttributes(cb, {"class":"cb",
                                "name":"checkbox",
                                "type":"checkbox",
                                "id": String(w['rownum'])});
                    
                    let criteria = document.createElement("p");
                    setAttributes(criteria, {"class":"criteria",
                                "name":"criteria",
                                "id": "criteria-"+w['rownum']});
                    criteria.innerHTML = w['Criteria'];

                    let comment = document.createElement("input");
                    setAttributes(comment, {"class":"comment",
                                "name":"comment",
                                "id": "comment-"+w['rownum'],
                                "type":"text",
                                "placeholder":w['Comment']
                            });
                    
                    let reference = document.createElement("p");
                    setAttributes(reference, {"class":"reference",
                                "name":"reference",
                                "id": "reference-"+w['rownum']});
                    reference.innerHTML = w['Reference'];

                    rowcontainer.appendChild(cb);
                    rowcontainer.appendChild(criteria);
                    rowcontainer.appendChild(comment);
                    rowcontainer.appendChild(reference);
                    mainContainer.appendChild(rowcontainer);
                    }
                } 
            }
        
        }
    }
    catIDNumber++;    
};