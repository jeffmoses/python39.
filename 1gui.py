from tkinter import*

window =Tk()
window.geometry("600x270")
window.title("EmployeeDATA App")

empId = Label(window,text = "EmployeeID:",font = ("serif",12))
empId.place(x=20,y=30)

empName = Label(window,text="EmployeeName:",font=("serif",12))
empName.place(x=20,y=60)

empDept = Label(window,text="EmployeeDept:",font=("serif",12))
empDept.place(x=20,y=90)

enterId=Entry(window)
enterId.place(x=170,y=30)

enterName=Entry(window)
enterName.place(x=170,y=60)

enterDept=Entry(window)
enterDept.place(x=170,y=90)

insertBtn = Button(window,text="Insert",font=("sans",12),bg="green",command= "insertData")
insertBtn.place(x=20,y=160)

updateBtn =Button(window,text="update",font=("sans",12),bg="white",command="updateData")
updateBtn.place(x=80,y=160)

getBtn =Button(window,text="Fetch",font=("sans",12),bg="yellow",command="getData")
getBtn.place(x=150,y=160)

deleteBtn =Button(window,text="delete",font=("sans",12),bg="red",command="deleteData")
deleteBtn.place(x=210,y=160)

resetBtn =Button(window,text="reset",font=("sans",12),bg="grey",command="resetData")
resetBtn.place(x=20,y=210)

showData =Listbox(window)
showData.place(x=330,y=30)

window.mainloop()
