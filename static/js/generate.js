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
    let subIDNumber = 1;
    for (let x in cat) {
        //console.log(x); //category
        let catAnchor = document.createElement("a");
        setAttributes(catAnchor, {
                            "onclick":"show(this)",
                            "id":'catAnchor'+String(catIDNumber),
                            "class":"catAnchor"});
        //"href": "function.js",
        let catCollapsible = document.createElement("div");
        setAttributes(catCollapsible, {"class":"collapsible",
                            "name": "category-"+String(x),
                            "id":'catCollapsible'+String(catIDNumber)});

        catCollapsibleHeader = document.createElement("h2");
        catCollapsibleHeader.innerHTML = x;
        catCollapsibleHeader.setAttribute("class","catHeader");
        catCollapsible.appendChild(catCollapsibleHeader);

        catAnchor.appendChild(catCollapsible);
        mainContainer.append(catAnchor);
        let sub = cat[x];
        for (let y in sub) {
            let subAnchor = document.createElement("a");
            setAttributes(subAnchor, {
                            "onclick":"show(this)",
                            "id":'subAnchor'+String(subIDNumber),
                            "class":"subAnchor"});
            //"href":"static/js/functions.js",
            let subCollapsible = document.createElement("div");
            setAttributes(subCollapsible, {"class":"collapsible",
                                "name": "subcategory-"+String(x),
                                "id":'sub'+String(catIDNumber)});
            subCollapsibleHeader = document.createElement("h2")
            subCollapsibleHeader.setAttribute("class","subHeader");
            subCollapsibleHeader.innerHTML = y;
            subCollapsible.appendChild(subCollapsibleHeader);

            subAnchor.appendChild(subCollapsible);
            mainContainer.append(subAnchor);
            let rows = sub[y];
            for (let z = 0; z < rows.length; z++) {
                let w = rows[z];
                let rowcontainer = document.createElement("div");
                setAttributes(rowcontainer, {"class":"row",
                            "class" : "rowsub"+String(subIDNumber),
                            "name": "rowcontainer",
                            "id":String("rowcontainer-"+ w['rownum'])});

                let cb = document.createElement("INPUT");
                setAttributes(cb, {"class":"cb",
                            "name":"checkbox",
                            "type":"checkbox",
                            "id": String(w['rownum'])});
                
                let criteria = document.createElement("p");
                setAttributes(criteria, {"class":"criteria",
                            "name":"criteria",
                            "id": "criteria-"+w['rownum']});
                criteria.innerHTML = w['Problem'];

                let comment = document.createElement("textarea");
                setAttributes(comment, {"class":"comment",
                            "name":"comment",
                            "id": "comment-"+w['rownum']});
                comment.innerHTML = w['Comment'];
                
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
            subIDNumber++;
        }
    catIDNumber++;    
    }
};