import tkinter as tk
import setting.Image_exe as Im
import setting.Color_picker as cp
import sys


import pdb

global filepath, folderpath

class Window_manager():

    def __init__(self):
        pass

    def windows(self, title):
        window = tk.Tk()
        window.title(title) 
        return window

    def button_frame(self, window):
        buttomframe = tk.Frame(window)
        buttomframe.pack()
        return buttomframe
        
    def img_read_buttom(self, window, buttomframe):
        Im_read = Im.Img()
        openimg_buttom = tk.Button(buttomframe, 
                            text='Select an image', fg='blue', 
                            command=lambda : [Im_read.select_image(), self.window_instructor(self.windows('Intruction')) ])
        openimg_buttom.pack(side="left", fill="both", expand="yes", padx="10", pady="10")
        
    def analysis_buttom(self, window, buttomframe):
        Im_read = Im.Img()
        analyse_buttom = tk.Button(buttomframe, 
                            text='Analyze', fg='green', 
                            command=lambda : [Im_read.img_loop()])
        analyse_buttom.pack(side="left", fill="both", expand="yes", padx="10", pady="10")

    def close_buttom(self, window, buttomframe):
        stop_buttom = tk.Button(buttomframe, 
                            text='Close program', fg='red', 
                            command=lambda : [self.destroy_window(window)])
        stop_buttom.pack(side="left", fill="both", expand="yes", padx="10", pady="10")

    def stop_program_buttom(self, window, buttomframe):
        stop_buttom = tk.Button(buttomframe, 
                            text='Close program', fg='red', 
                            command=lambda : [sys.exit()])
        stop_buttom.pack(side="left", fill="both", expand="yes", padx="10", pady="10")

    def window_instructor(self, window):

        tk.Label(window, text='Use the follow command when carry out the analysis of the images:\n').pack()#etiqueta de vetana
        
        tk.Label(window, text='Press and hold "right mouse click" to draw contour\n' 
                             + 'Press "a" to apply a contour\n' 
                             + 'Press "s" to save analysis\n'
                             + 'Press "d" to clean analysis and contour\n'
                             + 'Press "q" to close windows image').pack()
        self.close_buttom(window, self.button_frame(window))

        #window.mainloop()
    def destroy_window(self, window):
        window.destroy()

    def loop(self, window):
        window.mainloop()

    #    return 
        



    



        





        