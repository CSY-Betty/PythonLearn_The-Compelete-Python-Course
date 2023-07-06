import tkinter as tk
from  tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side='left', fill='both', expand=True)

tk.Label(main, text='Label1', bg='green').pack(side='left', fill='y', expand=False)
tk.Label(main, text='Label2', bg='red').pack(side='right', fill='x', expand=False)

tk.Label(root, text='Label3', bg='red').pack(side='top', fill='both', expand=True)



root.mainloop()