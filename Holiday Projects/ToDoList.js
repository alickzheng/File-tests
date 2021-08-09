const TASKS = "task";
const LIST = "list";

if (localStorage.getItem(TASKS) !== null) {
    toDoList = JSON.parse(localStorage.getItem(TASKS));
}
else{
    toDoList = [];
}

class ToDoTask {
    constructor(task, dueDate){
        this._task = task;
        this._dueDate = dueDate;
        this._outPut = this._task + " " + this._dueDate
    }
    get task(){
        return this._task;
    }

    get dueDate(){
        return this._dueDate;
    }

    get outPut(){
        return this._outPut
    }
}

function retrieveItem(key){
    return retrieved = JSON.parse(localStorage.getItem(key));
}

function updateDisplay(){
    let listElement = document.getElementById("toDoList");
    listElement.innerHTML += `
    <li onclick="removeTask(this)"> ${toDoList.pop().outPut}</li>
    `
}

function addTask(){
    let tasks = document.getElementById("task").value;
    let dueDates = document.getElementById("dueDate").value;
    toDoList.push(new ToDoTask(tasks, dueDates));
    window.localStorage.setItem(TASKS, JSON.stringify(toDoList))
    updateDisplay()
}

function removeTask(selected_item) {
    confirm("Is this task complete?")
    selected_item.parentNode.removeChild(selected_item);
}

function moveUp(index){
    if (index == 0){
        return console.log("This task is already the highest priority")
    }
    else{
        let b = toDoList[index-1];
        toDoList[index-1] = toDoList[index];
        toDoList[index] = b;
    }
}

function moveDown(index){
    if (index == toDoList.length){
        return console.log("This task is already the lowest priority")
    }
    else{
        let b = toDoList[index+1];
        toDoList[index+1] = toDoList[index];
        toDoList[index] = b;
    }
}
