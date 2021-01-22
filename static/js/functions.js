document.getElementById('submit').onclick = function() {
    var checkboxes = document.getElementsByName('cb');
    for (var checkbox of checkboxes) {
      if (checkbox.checked) {
        let cIndex = "c"+String(checkbox.id);
        let rIndex = "r"+String(checkbox.id);
        let comment = document.getElementById(cIndex);
        let reference = document.getElementById(rIndex);
        checkbox.value = comment.value + " (" + reference.innerHTML + ".)";
        console.log(checkbox.value);
  }}
};

let coll = document.getElementsByClassName("collapsible");
let i;

function show(obj) {
  let index = obj.id.slice(-1);
  let row = document.getElementById("row"+index);
  if(row.style.display === 'none') {
    row.style.display = 'flex';
  }
  else {
    row.style.display = 'none';
  }
}