import tkinter as tk
from tkinter import colorchooser

import pdb

class color_selector():


    def __init__(self):
        pass

    def color_function(self):
        #Devuelve los valores RGB del color picker
        color_picker = colorchooser.askcolor()[0]
        return color_picker

