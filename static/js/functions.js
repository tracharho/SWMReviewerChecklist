

/*
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
        console.log(letterComment);
        console.log(checkbox.value);
        checkbox.value = letterComment;
      }
    }
};

function show(obj) {
  console.log(obj.attributes.class);
  let children = obj.children;
  let l = children.length;
  let rows = document.getElementsByClassName("row"+children[0].id);
  for (row of rows) {
    console.log(row.style.display);
    if (row.style.display === '') {
      row.style.display = 'none';
    }
    else if (row.style.display === 'none') {
      row.style.display = 'flex';
    }
    else {
      row.style.display = 'none';
    }
  }  
};