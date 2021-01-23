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
function appendData(data) {
    var mainContainer = document.getElementById("myData");
    let cat = data[0];
    //checks out - console.log(cat);
    for (let x in cat) {
        //checks out console.log(x);
        let catAnchor = document.createElement("a");
        catAnchor.setAttribute("href","javascript:;");
        catAnchor.setAttribute("onclick","show(this)");
        catAnchor.setAttribute("id", ('a-'+String(x)));
        
        let catCollapsible = document.createElement("div");
        catCollapsible.innerHTML = x;
        catCollapsible.setAttribute("class","collapsible");
        catCollapsible.setAttribute("name", "c-"+String(x));
        
        let category = document.createElement("div");
        category.setAttribute("class","Category");
        category.setAttribute("id",x);
        
        let sub = cat[x];
        //console.log(sub);
        for (let y in sub) {
            console.log(y);
            let subAnchor = document.createElement("a");
            subAnchor.setAttribute("href","javascript:;");
            subAnchor.setAttribute("onclick","show(this)");
            subAnchor.setAttribute("id", ('a-'+String(y)));
            
            let subCollapsible = document.createElement("div");
            subCollapsible.innerHTML = y;
            subCollapsible.setAttribute("class","collapsible");
            subCollapsible.setAttribute("name", String("c-"+String(y)));
            
            let subcategory = document.createElement("div");
            subcategory.setAttribute("class","Category");
            subcategory.setAttribute("id",y);

            let rows = sub[y]
            for (let z in rows) {
                
                for (let row in rows) {
                    //console.log(rows[row]);                    
                    // commentObject[x][y][z][rows] is the lowest level value
                }
            }
        }
        
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