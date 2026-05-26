import tkinter as tk

main = tk.Tk()
main.geometry("1000x750")

label = tk.Label(main, text='todo list', font=('Arial', 40))
label.pack()
insert = tk.Toplevel()
insert.title('add to list')
insert.geometry('300x200')
insert.withdraw()
entry = tk.Entry(insert, width=20)
entry.pack(padx=15, pady=15)

def addnew():
    new = entry.get()
    
    if new:
        num = list.size() + 1
        list.insert('end', f"{num}. {new}")
    
button = tk.Button(insert, text='add', width=20, background='blue', fg='white', command=lambda: addnew())
button = tk.Button(main, text='add to list', width=20, background='blue', fg='white', command=lambda: insert.deiconify())
button.pack(padx=15, pady=15)
container = tk.Frame(main, background='white', width=500, height=500)
container.pack(fill='both', expand=True)
list = tk.Listbox(container, width=30, height=10, font=('Arial', 24))
list.pack(padx=15, pady=15)



tk.mainloop()



    

