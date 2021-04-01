import setting.Window_comander as Wc
import setting.Image_exe as Im
import pdb

global img_bool, close_bool
close_bool = True


def main():
    

    main_obj = Wc.Window_manager()#inicialización de main    
    main_win = main_obj.windows('Control window')#creo la ventana de menu
    framebuttom1 = main_obj.button_frame(main_win)
    main_obj.img_read_buttom(main_win, framebuttom1)
    main_obj.analysis_buttom(main_win, framebuttom1)
    main_obj.stop_program_buttom(main_win, framebuttom1)

    main_obj.loop(main_win)



#pdb.set_trace()

if __name__ == '__main__':
    main()

