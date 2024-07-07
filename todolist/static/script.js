let editable = document.querySelectorAll(".editable")

//function to hide the orignal and show the form 
function switcher(cls_name) {
    let c_name = "."+cls_name
    let cls = document.querySelectorAll(c_name)
    cls.forEach((e)=>{
        e.classList.toggle("d-none")
    })
    
}

