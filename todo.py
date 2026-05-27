import tkinter as tk
import json

main = tk.Tk()
main.geometry("1000x750")
main.title("Todo List")

title = tk.Label(main, text='Todo List', font=('Arial', 36, 'bold'))
title.pack(pady=10)

insert = tk.Toplevel()
insert.title('Add Item')
insert.geometry('350x200')
insert.withdraw()

entry = tk.Entry(insert, width=30, font=('Arial', 14))
entry.pack(padx=15, pady=15)

container = tk.Frame(main)
container.pack(fill='both', expand=True, padx=20, pady=20)

left = tk.Frame(container)
left.pack(side='left', fill='both', expand=True, padx=10)
right = tk.Frame(container)
right.pack(side='right', fill='both', expand=True, padx=10)

label1 = tk.Label(left, text="Focus", font=('Arial', 20, 'bold'))
label1.pack(pady=5)
label2 = tk.Label(right, text="Backburner", font=('Arial', 20, 'bold'))
label2.pack(pady=5)

focus = tk.Listbox(left, font=('Arial', 16), height=20)
focus.pack(fill='both', expand=True)
backburner = tk.Listbox(right, font=('Arial', 16), height=20)
backburner.pack(fill='both', expand=True)


focus_data = []
backburner_data = []


def refresh():
    focus.delete(0, tk.END)
    backburner.delete(0, tk.END)

    for i, item in enumerate(focus_data, start=1):
        focus.insert(tk.END, f"{i}. {item}")

    for i, item in enumerate(backburner_data, start=1):
        backburner.insert(tk.END, f"{i}. {item}")


def add_item(target):
    new = entry.get().strip()
    entry.delete(0, tk.END)

    if new:
        if target == focus:
            focus_data.append(new)
        else:
            backburner_data.append(new)

        refresh()


def delete_item(listbox):
    selected = listbox.curselection()

    if selected:
        index = selected[0]

        if listbox == focus:
            focus_data.pop(index)
        else:
            backburner_data.pop(index)

        refresh()

drag_data = {"index": None}

def letdrag(listbox):

    def click(event):
        drag_data["index"] = listbox.nearest(event.y)

    def move(event):
        new_index = listbox.nearest(event.y)
        old_index = drag_data["index"]

        if new_index != old_index:
            if listbox == focus:
                item = focus_data.pop(old_index)
                focus_data.insert(new_index, item)

            else:
                item = backburner_data.pop(old_index)
                backburner_data.insert(new_index, item)

            drag_data["index"] = new_index
            refresh()

    listbox.bind("<Button-1>", click)
    listbox.bind("<B1-Motion>", move)

letdrag(focus)
letdrag(backburner)


bframe = tk.Frame(main)
bframe.pack(pady=10)


def open_add():
    insert.deiconify()
    insert.lift()
    entry.focus_set()


add_main = tk.Button(bframe, text='Add to Main', width=15, bg='blue', fg='white', command=lambda: add_item(focus))
add_back = tk.Button(bframe, text='Add to Backburner', width=18, bg='blue', fg='white', command=lambda: add_item(backburner))
delete_main = tk.Button(bframe, text='Delete Main', width=15, bg='red', fg='white', command=lambda: delete_item(focus))
delete_back = tk.Button(bframe, text='Delete Back', width=15, bg='red', fg='white', command=lambda: delete_item(backburner))
open_add_btn = tk.Button(bframe, text='Open Add', width=15, bg='green', fg='white', command=open_add)

add_main.grid(row=0, column=0, padx=5, pady=5)
add_back.grid(row=0, column=1, padx=5, pady=5)
delete_main.grid(row=0, column=2, padx=5, pady=5)
delete_back.grid(row=0, column=3, padx=5, pady=5)
open_add_btn.grid(row=0, column=4, padx=5, pady=5)

def load():

    global focus_data
    global backburner_data

    try:
        with open("todo_data.json", "r") as f:
            data = json.load(f)

        focus_data = data["focus"]
        backburner_data = data["backburner"]

        refresh()

    except FileNotFoundError:
        pass

def save():
    data = {
        "focus": focus_data,
        "backburner": backburner_data
    }

    with open("todo_data.json", "w") as f:
        json.dump(data, f)


def close():
    save()
    main.destroy()


main.protocol("WM_DELETE_WINDOW", close)

load()
tk.mainloop()