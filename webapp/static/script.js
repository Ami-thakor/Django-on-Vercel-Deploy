// Get the modal and buttons
const modal = document.getElementById("deleteModal");
const formControll = document.getElementById("formControll");
const openModalBtn = document.getElementById("delete");
const openEditBtn = document.getElementById("edit");
const closeModalBtn = document.getElementById("closeModal");
const cross = document.getElementById("cross");
const cancelBtn = document.getElementById("cancel");

// Open modal on button click
openModalBtn.onclick = function () {
  modal.style.display = "flex";
};

// Close modal on close button click or cancel button
closeModalBtn.onclick = function () {
  modal.style.display = "none";
};

cancelBtn.onclick = function () {
  modal.style.display = "none";
};


const myfuntion = ()=>{

}

// Open edit on button click
const openEditor = (data) => {
  formControll.style.display = "flex";
  const title =  document.getElementById("action-title");
  title.innerText = data + " Monitor"
};

cross.onclick = function () {
  formControll.style.display = "none";
};

// Close modal when clicking outside the modal
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
    formControll.style.display = "none";
  } else if (event.target == formControll) {
    formControll.style.display = "none";
  }
};
