import numpy as np
import os
import os.path
from tkinter import messagebox

import pdb

#Hacer el os.uname, para obtener info del systema operativo y decidir como guardar las cosas

class file_manager():

    def Folder_changer(self, path):
        try:
            os.chdir('./save_files')
        except OSError:
            messagebox.showwarning(title='Warning', 
                                   message='Select image first')
    
    def obtain_path_and_file_name(self, path):
        
        file_path = os.path.dirname(path)
        file_name = os.path.basename(path)
        
        return [file_path, file_name] 
    
#    def file_writer(self, file_name, data):
#            
#        file = open(str(file_name) + '_Histogram_data.csv', 'a')
#        file.write('# ' + str(file_name) + '_Counts_vs_intensity'+  '\n')
#        #file.write('# counts max value: ' + str(data[1]) +  '\n')
#        #file.write('# intensity max value: ' + str(data[2]) +  '\n')
#        file.write('# intensity     counts \n')
#
#        for h in range(len(data[0])):
#            file.write(str(h) + '	' + str(data[0][h]) + '\n')
#        file.close()
