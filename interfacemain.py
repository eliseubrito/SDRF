import customtkinter
import ctypes
from PIL import Image
import cv2


class App(customtkinter.CTk):

    def __init__(self):
        def delete_page():
            for frame in main_frame.winfo_children():
                frame.destroy()

        def recog_page():
            delete_page()
            recog_frame = customtkinter.CTkFrame(main_frame)

            video = cv2.VideoCapture(0)
            facedetection = cv2.CascadeClassifier("./classifier/haarcascade_frontalface_default.xml")
            while True:
                ret,frame=video.read()

                gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = facedetection.detectMultiScale(gray, 1.3, 5)

                for(x,y,w,h) in faces:
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
                
                cv2.imshow("SDRF", frame)

                k=cv2.waitKey(1)

                if k == ord('q'):
                    break

            video.release()
            cv2.destroyAllWindows()

            # lb = customtkinter.CTkLabel(recog_frame, text="2133")
            # lb.pack()

            recog_frame.pack(padx=500, pady=10)
        
        def reg_page():
            delete_page()
            regis_frame = customtkinter.CTkFrame(main_frame)

            name_User = customtkinter.CTkLabel(regis_frame, text="Nome")
            name_User.pack(padx=10, pady=0)
            name_ent = customtkinter.CTkEntry(regis_frame, placeholder_text="Seu nome")
            name_ent.pack(padx=10, pady=0)

            idade_user = customtkinter.CTkLabel(regis_frame, text="Idade")
            idade_user.pack(padx=10, pady=0)
            idade_entr = customtkinter.CTkEntry(regis_frame, placeholder_text="Sua idade")
            idade_entr.pack(padx=10, pady=0)

            
            cargo_user = customtkinter.CTkLabel(regis_frame, text="Cargo")
            cargo_user.pack(padx=10, pady=0)
            cargo_entr = customtkinter.CTkEntry(regis_frame, placeholder_text="Seu cargo")
            cargo_entr.pack(padx=10, pady=0)
            
            regis_btn = customtkinter.CTkButton(regis_frame, text="Tirar Foto e Registrar", font=('Bold',15), fg_color='#158aff', command=reg_page)
            regis_btn.pack(padx=10, pady=10)

            regis_frame.pack(padx=200, pady=10)


        super().__init__()
        self._set_appearance_mode("Light")
        self.geometry("1000x600")
        self.title("SDRF")
        self.iconbitmap("assets\logo.ico")

        
        myappid = 'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


        options_frame = customtkinter.CTkFrame(self)

        home_btn = customtkinter.CTkButton(options_frame, text="Reconhecimento", font=('Bold',15), fg_color='#158aff', command=recog_page)
        home_btn.place(x=5, y=50)

        registrar_btn = customtkinter.CTkButton(options_frame, text="Registrar", font=('Bold',15), fg_color='#158aff', command=reg_page)
        registrar_btn.place(x=5, y=100)
       
        options_frame.pack(side=customtkinter.LEFT)
        options_frame.pack_propagate(False)
        options_frame.configure(width=150, height=600)

        main_frame = customtkinter.CTkFrame(self, border_color="black", border_width=1)
        main_frame.pack(side=customtkinter.LEFT)
        main_frame.pack_propagate(False)
        main_frame.configure(width=850,height=600)


app = App()
app.mainloop()
