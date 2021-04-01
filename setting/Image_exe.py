import cv2
import numpy as np
from matplotlib import pyplot as plt
import setting.Image_analytic_func as Iaf
from tkinter import filedialog
from tkinter import messagebox
import os

import pdb


class Img():
    
    def __init__(self):
        pass

    
    def select_image(self):

        global img_BGR, img_BGR_name, open_file_path
        
        ftypes = [
            ("JPG", "*.jpg;*.JPG;*.jpeg;*.JPEG"), 
            ("PNG", "*.png;*.PNG"),
            ("GIF", "*.gif;*.GIF"),
            ("TIF", "*.tif;*.TIF"),
            ("All files", "*.*")
            ]

        open_file_path = filedialog.askopenfilename(filetypes = ftypes)
        
        #pdb.set_trace()
        
        if len(open_file_path) > 0:
            
            img_BGR = cv2.imread(open_file_path)
            img_BGR_name = 'img_BGR'
    
    def img_loop(self):

        try:
                  
            cv2.namedWindow(img_BGR_name, cv2.WINDOW_NORMAL)
            img_ob = Iaf.img_analisys(img_BGR_name, img_BGR)
            cv2.setMouseCallback(img_BGR_name, img_ob.draw_dots)

            while(1):
            
                #cv2.imshow(img_BGR_name,img_BGR)
                img_ob.show_image()
                k = cv2.waitKey(10) & 0xFF
                
                if k == ord('a') or k == ord('A'):
                    #dotslist = np.asarray(dotslist)
                    cuted_sect = img_ob.Croped()[0]
                    mask_cuted_sect = img_ob.Croped()[1]
                    rec_cuted_sect = img_ob.Croped()[2]
                    
                if k == ord('s') or k == ord('S'):
                    
                    save_img_path = self.img_analysis_path()
                
                if k == ord('q') or k == ord('Q'):#esc
                    
                    cv2.destroyAllWindows()#Destruimos todas las ventanas
                    break


        except NameError:
            messagebox.showwarning(title='Warning', 
                                   message='Select image first')

    def img_analysis_path(self):
        
        save_path = filedialog.askdirectory()
        if len(save_path) > 0:
            os.chdir(save_path)
            save_img_path = os.getcwd()
            #pdb.set_trace()
            
            return save_img_path
        
        elif len(save_path) == 0:
            default_save_dir = os.path.isdir('.\save_files')
            
            if default_save_dir == True:
                
                os.chdir('.\save_files')
                save_img_path = os.getcwd()
                #pdb.set_trace()
                return save_img_path
            
            elif default_save_dir == False:
                
                os.mkdir('save_files')
                os.chdir('.\save_files')
                save_img_path = os.getcwd()
                #pdb.set_trace()
                return save_img_path
            
            
            


    






   
    