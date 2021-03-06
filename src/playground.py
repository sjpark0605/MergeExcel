import tkinter as tk

app = tk.Tk()
app.title('List box')


def clicked():
    print("clicked")
    selected = box.curselection()  # returns a tuple
    for idx in selected:
        print(box.get(idx))

box = tk.Listbox(app, selectmode=tk.MULTIPLE, height=4)
values =['사업자', '대표자명', '주소', '우편번호']
for val in values:
    box.insert(tk.END, val)
box.pack()

button = tk.Button(app, text='Show', width=25, command=clicked)
button.pack()

exit_button = tk.Button(app, text='Close', width=25, command=app.destroy)
exit_button.pack()

app.mainloop()