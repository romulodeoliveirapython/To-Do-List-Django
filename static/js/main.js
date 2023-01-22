const allTasks = document.querySelector(".allTasks");
const caixasInput1 = document.querySelectorAll(".check-item input");
const completedTasks = document.querySelector(".completedTasks");
function initTasks() {
  function addListCompleted() {
    const elementPai = this.parentElement;
    elementPai.classList.toggle("checked");
    completedTasks.appendChild(elementPai);
    if (!elementPai.classList.contains("checked")) {
      allTasks.appendChild(elementPai);
    }
  }

  caixasInput1.forEach((item) => {
    item.addEventListener("click", addListCompleted);
  });
}
initTasks();
/* Modal adcionar */
function initModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add("modal-ativo");
    modal.addEventListener("click", (event) => {
      if (event.target.id == modalId || event.target.id == "fechar-modal") {
        modal.classList.remove("modal-ativo");
      }
    });
  }
}

const btnModal = document.querySelector(".add-task");
btnModal.addEventListener("click", () => initModal("modalAdd"));

// Função construtora
function geradorNum(a, b) {
  return Math.floor(Math.random() * (b - a + 1)) + a;
}

function SaveTodo(text) {
  // Criando a div principal
  const todoItem = document.createElement("div");
  todoItem.classList.add("check-item");

  //Criando a label
  const todoItemLabel = document.createElement("label");
  todoItemLabel.getAttribute("for");
  const valorLabel = geradorNum(10, 1000);
  todoItemLabel.setAttribute("for", valorLabel);
  todoItemLabel.innerText = text;

  // Criando o input
  const todoItemInput = document.createElement("input");
  todoItemInput.getAttribute("type");
  todoItemInput.setAttribute("type", "checkbox");
  todoItemInput.getAttribute("name");
  todoItemInput.setAttribute("name", "radio");
  todoItemInput.getAttribute("id");
  todoItemInput.setAttribute("id", valorLabel);

  //Moovendo os elementos
  todoItem.appendChild(todoItemLabel);
  todoItem.appendChild(todoItemInput);
  allTasks.appendChild(todoItem);

  todoInput.value = "";
}

// add task

const btnAddModal = document.querySelector("#addBtnModal");
const todoInput = document.querySelector("#todoInput");

function clickAddTodo(event) {
  event.preventDefault(); // fazer com que o fonrmulário não seja enviado
  const inputValue = todoInput.value; // Pegando o valor digitado
  if (inputValue) {
    SaveTodo(inputValue); // Ativando a função construtora
  }
}

btnAddModal.addEventListener("click", clickAddTodo);
