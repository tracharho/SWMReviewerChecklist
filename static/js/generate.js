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

//x = Category
//y = Subcategory
//z = row#

//TODO
//Make function to create html tags with 
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
    let cat = data;
    let catIDNumber = 1;
    let subIDNumber = 1;
    for (let x in cat) {
        //console.log(x); //category
        let catAnchor = document.createElement("a");
        setAttributes(catAnchor, {"href":"javascript",
                            "onclick":"show(this)",
                            "id":'catAnchor'+String(catIDNumber),
                            "class":"catAnchor"});
        
        let catCollapsible = document.createElement("div");
        catCollapsible.innerHTML = x;
        setAttributes(catCollapsible, {"class":"collapsible",
                            "name": "c-"+String(x),
                            "id":'catCollapsible'+String(catIDNumber)});
        
        let sub = cat[x];
        //console.log(sub);
        for (let y in sub) {
            let subAnchor = document.createElement("a");
            setAttributes(subAnchor, {"href":"javascript",
                            "onclick":"show(this)",
                            "id":'subAnchor'+String(subIDNumber),
                            "class":"subAnchor"});
            
            let subCollapsible = document.createElement("div");
            subCollapsible.innerHTML = y;
            setAttributes(subCollapsible, {"class":"collapsible",
                                "name": "s-"+String(x),
                                "id":'subCollapsible'+String(catIDNumber)});
            
            //let subcategory = document.createElement("div");
            //subcategory.setAttribute("class","Category");
            //subcategory.setAttribute("id",y);

            let rows = sub[y];
            console.log(rows);
            for (let z in rows) {
                
                for (let row in rows) {
                    for (let item in rows) {
                        console.log(items);
                    }                    
                    // commentObject[x][y][z][rows] is the lowest level value
                }
            }
        }
    catAnchor++;    
    }
    
    
    
    // mainContainer.appendChild(catAnchor);
    // catAnchor.appendChild(collapsible);
};
// for (var i = 0; i < (data.length); i++) {
//     for (var j = 0; j < (data[i].length); j++) {
//         for (var k = 0; k < (data[i][j].length); k++) {
//             var div = document.createElement("div");
//             div.innerHTML = data[i][j][k];
//             div.setAttribute("id", ("row" + i));
//             div.setAttribute("class", ("row"));
//             mainContainer.appendChild(div);
//         }
//     }
// };