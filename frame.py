from tkinter import *
from tkinter import ttk, messagebox, font
from graph_constructor import show_graph
from other_methods import get_paths, get_syms_and_descriptions, get_annotation, get_sig_len


def launch():

    file_name = files_list.get()

    s_from_txt = samp_from.get()
    s_to_txt = samp_to.get()

    s_from = int(s_from_txt) if s_from_txt != '' else 0
    s_to = int(s_to_txt) if s_to_txt != '' else 0

    syms = [sym[0] for sym in [syms_and_descriptions.get(el) for el in syms_and_descriptions.curselection()]]
    if file_name != 'Выберите файл' and s_from < s_to and s_from >= 0 and s_to >= 2:
        show_graph(file_name, syms, s_from, s_to)
    else:
        messagebox.showwarning(title="Проблема с параметрами", message="Выберите файл, промежуток записи и необходимые аннотации!")

def select_file(event):

    selection = files_list.get()
    sig_len = get_sig_len(selection)
    anno_labels = list(dict.fromkeys(get_annotation(selection, 0, sig_len).symbol))

    samp_from_v.set('')
    samp_to_v.set('')
    ex_annos.set([])
    
    samp_from['state'] = 'disabled'
    samp_to['state'] = 'disabled'
    confirm_button['state'] = 'disabled'

    samp_from_v.set('0')
    samp_to_v.set(f'{sig_len}')
    ex_annos.set(get_syms_and_descriptions(anno_labels))

    samp_from['state'] = 'enable'
    samp_to['state'] = 'enable'
    confirm_button['state'] = 'enable'

root = Tk()
root.title("Параметры графика")
root.geometry("840x570")
root.resizable(False, False)

for c in range(4): root.columnconfigure(index=c, weight=1)
for r in range(5): root.rowconfigure(index=r, weight=1)

local_font = font.Font(size=20)

files_list = ttk.Combobox(
    values=get_paths(), 
    width=60, 
    state='readonly',
    font=local_font
)

files_list.bind('<<ComboboxSelected>>', select_file)
files_list.set('Выберите файл')
files_list.grid(row=0, column=0, columnspan=4, ipadx=70, ipady=6, padx=5)

samp_from_v = StringVar()
samp_from = ttk.Entry(
    textvariable=samp_from_v,
    font=local_font,
    width=15
)
samp_from.grid(row=1, column=1)

samp_to_v = StringVar()
samp_to = ttk.Entry(
    textvariable=samp_to_v,
    font=local_font,
    width=15
)
samp_to.grid(row=1, column=3)

samp_from_l = ttk.Label(
    text='Промежуток от:', 
    font=local_font,
    width=13
)
samp_from_l.grid(row=1, column=0)

samp_to_l = ttk.Label(
    text='до:', 
    font=local_font
)
samp_to_l.grid(row=1, column=2)

mini_title = ttk.Label(
    text='Доступные аннотации:',
    font=local_font
)
mini_title.grid(row=2, column=0)

ex_annos = Variable()

syms_and_descriptions = Listbox(
    listvariable=ex_annos, 
    selectmode=MULTIPLE,
    font=local_font,
    width=60
)

syms_and_descriptions.grid(row=3, column=0, columnspan=4, ipady=6, padx=5)

confirm_button = ttk.Button(
    root, 
    text='Применить', 
    command=launch, 
    width=38
)
confirm_button.grid(row=4, column=3, ipady=5)

root.mainloop()