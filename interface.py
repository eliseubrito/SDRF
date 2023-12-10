import customtkinter
import ctypes
import links
from PIL import Image
import cv2


class App(customtkinter.CTk):
    def __init__(self):

        #Deletar pagina
        def delete_page():
            for frame in self.winfo_children():
                frame.destroy()
        

        # def delete_page_side():
        #     for frame in main_frame.winfo_children():
        #         frame.destroy()

        def recog_page():
            print("Recog")
            # delete_page_side()
            # main_frame = customtkinter.CTkFrame(self)
            # recog_frame = customtkinter.CTkFrame(main_frame)
        

            # video = cv2.VideoCapture(0)
            # facedetection = cv2.CascadeClassifier("./classifier/haarcascade_frontalface_default.xml")
            # while True:
            #     ret,frame=video.read()

            #     gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #     faces = facedetection.detectMultiScale(gray, 1.3, 5)

            #     for(x,y,w,h) in faces:
            #         font = cv2.FONT_HERSHEY_SIMPLEX
            #         cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
            #         cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
                
            #     cv2.imshow("SDRF", frame)

            #     k=cv2.waitKey(1)

            #     if k == ord('q'):
            #         break

            # video.release()
            # cv2.destroyAllWindows()

            # # lb = customtkinter.CTkLabel(recog_frame, text="2133")
            # # lb.pack()

            # recog_frame.pack(padx=500, pady=10)
        
        def reg_page():
            print("register")
            # delete_page_side()
            
            # main_frame = customtkinter.CTkFrame(self)
            # regis_frame = customtkinter.CTkFrame(main_frame)

            # name_User = customtkinter.CTkLabel(regis_frame, text="Nome")
            # name_User.pack(padx=10, pady=0)
            # name_ent = customtkinter.CTkEntry(regis_frame, placeholder_text="Seu nome")
            # name_ent.pack(padx=10, pady=0)

            # idade_user = customtkinter.CTkLabel(regis_frame, text="Idade")
            # idade_user.pack(padx=10, pady=0)
            # idade_entr = customtkinter.CTkEntry(regis_frame, placeholder_text="Sua idade")
            # idade_entr.pack(padx=10, pady=0)

            
            # cargo_user = customtkinter.CTkLabel(regis_frame, text="Cargo")
            # cargo_user.pack(padx=10, pady=0)
            # cargo_entr = customtkinter.CTkEntry(regis_frame, placeholder_text="Seu cargo")
            # cargo_entr.pack(padx=10, pady=0)
            
            # regis_btn = customtkinter.CTkButton(regis_frame, text="Tirar Foto e Registrar", font=('Bold',15), fg_color='#158aff', command=reg_page)
            # regis_btn.pack(padx=10, pady=10)

            # regis_frame.pack(padx=200, pady=10)


        def interface_login():
            delete_page()

            main_frame = customtkinter.CTkFrame(self)

            frame_Title = customtkinter.CTkFrame(main_frame)
            frame_Main = customtkinter.CTkFrame(main_frame)
            frame_Cop = customtkinter.CTkFrame(main_frame)

            text_Title = customtkinter.CTkLabel(frame_Title, text="SDRF", font=("Arial",30))
            text_Title.pack(padx=0, pady=0)
            text_Desc = customtkinter.CTkLabel(frame_Title, text="Software de Reconhecimento Facial")
            text_Desc.pack(padx=10, pady=0)

            text_User = customtkinter.CTkLabel(frame_Main, text="Usuário")
            text_User.pack(padx=10, pady=0)
            user_database = customtkinter.CTkEntry(frame_Main, placeholder_text="Usuário BD")
            user_database.pack(padx=10, pady=0)

            text_Pass = customtkinter.CTkLabel(frame_Main, text="Senha")
            text_Pass.pack(padx=10, pady=0)
            pass_database = customtkinter.CTkEntry(frame_Main, placeholder_text="Senha Database", show="*")
            pass_database.pack(padx=10, pady=0)

            text_Option = customtkinter.CTkLabel(frame_Main, text="Opções BD",)
            text_Option.pack(padx=10, pady=0)

            combobox = customtkinter.CTkComboBox(frame_Main,values=["PostgreSQL", "MariaDB", "MySQL", "SQLite"])
            combobox.pack(padx=20, pady=0)
            combobox.set("PostgreSQL")

            button = customtkinter.CTkButton(frame_Main, text="Login", command=interface_main)
            button.pack(padx=10, pady=10)

            button_Doc = customtkinter.CTkButton(frame_Main, text="Documentação", command=links.documentation)
            button_Doc.pack(padx=10, pady=15)

            dev_Cop = customtkinter.CTkButton(frame_Cop, text="Desenvolvido por @EliseuBrito", fg_color="black", command=links.developer)
            dev_Cop.pack(padx=0, pady=0)


            frame_Title.pack(padx=20,pady=10)
            frame_Main.pack(padx=20,pady=0)
            frame_Cop.pack(padx=20,pady=20)

            main_frame.pack(padx=100,pady=15)

        def interface_main():
            delete_page()

            self._set_appearance_mode("Light")
            self.geometry("1000x500")
            self.title("SDRF")
            self.iconbitmap("assets\logo.ico")
            self.minsize(300,450)
            self.maxsize(1000,1000)
        
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

            main_framer = customtkinter.CTkFrame(self, border_color="black", border_width=1)
            main_framer.pack(side=customtkinter.LEFT)
            main_framer.pack_propagate(False)
            main_framer.configure(width=850,height=600)




        super().__init__()
        self._set_appearance_mode("Light")
        self.geometry("500x500")
        self.title("SDRF")
        self.iconbitmap("assets\logo.ico")
        self.minsize(300,450)
        self.maxsize(500,500)

        
        myappid = 'mycompany.myproduct.subproduct.version'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


        #Pagina Inicial
        main_frame = customtkinter.CTkFrame(self)
        frame_Logo = customtkinter.CTkFrame(main_frame)
        frame_Title = customtkinter.CTkFrame(main_frame)
        frame_Init = customtkinter.CTkFrame(main_frame)
        frame_Cop = customtkinter.CTkFrame(main_frame)

        my_image = customtkinter.CTkImage(light_image=Image.open("assets\Logo.png"), dark_image=Image.open("assets\Logo.png"), size=(120, 120))
        image_label = customtkinter.CTkLabel(frame_Logo, image=my_image, text="")
        image_label.pack()

        text_Title = customtkinter.CTkLabel(frame_Title, text="SDRF", font=("Arial",30))
        text_Title.pack(padx=0, pady=0)
        text_Desc = customtkinter.CTkLabel(frame_Title, text="Software de Reconhecimento Facial")
        text_Desc.pack(padx=10, pady=0)

        init = customtkinter.CTkButton(frame_Init, text="Iniciar", fg_color="black", font=("Arial",18), command=interface_login)
        init.pack(padx=0, pady=0)

        dev_Cop = customtkinter.CTkButton(frame_Cop, text="Desenvolvido por @EliseuBrito", fg_color="#696969", command=links.developer)
        dev_Cop.pack(padx=0, pady=0)


        frame_Logo.pack(padx=20,pady=30)
        frame_Title.pack(padx=20,pady=0)
        frame_Init.pack(padx=20,pady=30)
        frame_Cop.pack(padx=20,pady=10)

        main_frame.pack(padx=15,pady=45)




app = App()
app.mainloop()
