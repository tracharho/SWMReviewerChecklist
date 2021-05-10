
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
            console.log(checkbox.id);
            console.log('hit');
      let comment = document.getElementById(commentIDPrefix+rowNumValue);
      let reference = document.getElementById(referenceIDPrefix+rowNumValue);
      let letterComment;
      if (comment.value) {
      letterComment = comment.value + " (" + reference.innerHTML + ".)";
      }
      else {
      letterComment = comment.placeholder + " (" + reference.innerHTML + ".)";
      }
      checkbox.value = letterComment;
  }
}
};
let save_button = document.getElementById("save");
save_button.addEventListener("click", function(){
  let checkboxes = document.getElementsByName('checkbox');
  let commentIDPrefix = "comment-";
  for (let checkbox of checkboxes) {
    if (checkbox.checked) {
      let rowNumValue = checkbox.id;
      let comment = document.getElementById(commentIDPrefix+rowNumValue);
      let rowComment;
      if (comment.value) {
      rowComment = comment.value;
      }
      else {
      rowComment = comment.placeholder;
      }
      checkbox.value = checkbox.id + "|" + rowComment;
            console.log(checkbox.id);
  }
}
});

//used to loop through a subcategory's rows and shows or hides them. 
function collapseChildren(obj) {
let children = obj.children;
let rows = document.getElementsByName("row"+children[0].id);
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
  let catName = obj.attributes.name.value; //names like Stormwater or General Requirements
  let subs = document.getElementsByClassName("sub-of-"+String(catName)); //children Names are in this format
  for (sub of subs) {
    showOrHide(sub);
    let subName = sub.attributes.name.value;
    let rows = document.getElementsByClassName("row-of-"+String(subName)); //find each subcategories rows by id in "row{id}" format
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
      let subName = obj.attributes.name.value; //names like Stormwater or General Requirement
      let rows = document.getElementsByClassName("row-of-"+String(subName)); //find each subcategories rows by id in "row{id}" format
      for (row of rows) {
              showOrHide(row);
              }
        
      }  
};

