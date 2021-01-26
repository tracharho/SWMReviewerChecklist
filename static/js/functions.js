

/*
onclick function that gets all checkboxes that are checked 
and appends the comment and reference to the value.

cIndex: comment index used to find the associated comment
rIndex: reference index used to find the associated comment
*/
document.getElementById('submit').onclick = function() {
    let checkboxes = document.getElementsByName('checkbox');
    let commentIDPrefix = "comment-";
    let referenceIDPrefix = "reference-";
    for (let checkbox of checkboxes) {
      if (checkbox.checked) {
        let rowNumValue = checkbox.id;
        let comment = document.getElementById(commentIDPrefix+rowNumValue);
        let reference = document.getElementById(referenceIDPrefix+rowNumValue);
        let letterComment = comment.value + " (" + reference.innerHTML + ".)";
        checkbox.value = letterComment;
      }
    }
};

//used to loop through a subcategory's rows and shows or hides them. 
//the row is the 0th index of the 
function collapseChildren(obj) {
  let children = obj.children;
  let rows = document.getElementsByClassName("row"+children[0].id);
  for (row of rows) {
    showOrHide(row);
  }
};

//hides the obj
function hide(obj) {
  obj.style.display = "none";
}

//shows or hides the object.
//some objects are initializaed with a display value of ""
function showOrHide(obj) {
  if (obj.style.display === '') {
    obj.style.display = 'none';
  }
  else if (obj.style.display === 'none') {
    obj.style.display = 'flex';
  }
  else {
    obj.style.display = 'none';
  }
};

/*
This is the onclick function of categories and subcategories
catAnchor : Category Anchor element
subAnchor : Subcategory Anchor element
Element heirachy : catAnchor < catCollapsible < subAnchor < subCollapsible < rows
*/
function show(obj) {
  let thisClass = obj.attributes.class.value;
  if (thisClass == "catAnchor") {
    let catName = obj.attributes.name.value;
    let subs = document.getElementsByName("subcategory-"+String(catName)); //children Names are in this format
    for (sub of subs) {
      showOrHide(sub);
      let rows = document.getElementsByClassName("row"+sub.id); //find each subcategories rows by id in "row{id}" format
      for (row of rows) {
        //checks if all rows are hidden are showing.
        //The category closes all opened children (subcategories) and "grandchildren" (rows)
        if (row.style.display == "flex" && sub.style.display == "flex") {
          hide(row);
        }
        if (row.style.display == "flex" && sub.style.display == "none") {
          hide(row);
        }
      }
    } 
  }
  //This is called just the subcategory is clicked
  else {
    collapseChildren(obj);
  }
};
