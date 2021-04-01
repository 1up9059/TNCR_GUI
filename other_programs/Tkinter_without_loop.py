import tkinter as tk

ROOT1 = tk.Tk()
ROOT2 = tk.Tk()
LABEL1 = tk.Label(ROOT1, text="Hello, world!")
LABEL2 = tk.Label(ROOT2, text="Hello, world!")

LABEL1.pack()
LABEL2.pack()
LOOP_ACTIVE = True

while LOOP_ACTIVE:
    
    ROOT1.update()
    ROOT2.update()
    USER_INPUT = input("Give me your command! Just type \"exit\" to close: ")
    
    if USER_INPUT == "exit":
        ROOT2.quit()
        ROOT1.quit()
        LOOP_ACTIVE = False
    else:
        LABEL1 = tk.Label(ROOT1, text=USER_INPUT)
        LABEL2 = tk.Label(ROOT2, text=USER_INPUT)
        LABEL1.pack()
        LABEL2.pack()