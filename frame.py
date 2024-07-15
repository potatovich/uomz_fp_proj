from tkinter import *
from tkinter import ttk
from graph_constructor import show_graph
from other_methods import get_paths, get_sym_labels_and_descriptions
 
root = Tk()
root.title("Параметры графика")
root.geometry("600x250")
root.attributes("-toolwindow", True)

files_list = ttk.Combobox(values=get_paths(), width=60)
files_list.set('Выберите файл')
files_list.pack()
 
root.mainloop()