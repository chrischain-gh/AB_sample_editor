import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

root = tk.Tk()
root.title('Alpha Base Sample Editor')

# top row dropwdowns
def open_session():
    filepath = filedialog.askopenfilename(
                                #initialdir = "/",
                                initialdir = ".",
                                title = "Open Session File",
                                filetypes = [ (".csv", "*.csv") ] )
    return filepath

menubar = tk.Menu(root) #, bd=1) #, relief = tk.SUNKEN)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open Session...", command = open_session)
filemenu.add_command(label="Exit", command = root.quit)
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)


# Notebook
notebook = ttk.Notebook(root) # required for tabs

tab0 = tk.Frame(notebook, width=800, height=700)
tab1 = tk.Frame(notebook, width=800, height=700)
tab2 = tk.Frame(notebook, width=800, height=700)

notebook.add(tab0, text = '                 Record Single                 ')
notebook.add(tab1, text = '                 Single Edit                  ')
notebook.add(tab2, text = '                 Batch Edit                 ')

notebook.pack()
notebook.enable_traversal() # enables Ctrl+Tab

root.mainloop()