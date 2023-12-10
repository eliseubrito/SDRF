import customtkinter
from CTkMessagebox import CTkMessagebox
import cv2
from PIL import Image, ImageTk


class WebcamAPP:
    def __init__(self, window):
        def register():
            msg = CTkMessagebox(title="Concluído", message="Cadastro realizado",
                            icon="check", option_1="Ok")
            response = msg.get()
            
            if response =="OK":
                WebcamAPP.destroy() 
                
            else:
                root.destroy() 
                print("Click 'Yes' to exit!")
        
        self.window = window
        self.window.title("SDRF")

        self.video_capture = cv2.VideoCapture(0)
        self.current_image = None

        self.canvas = customtkinter.CTkCanvas(window, width=640, height=480)
        self.canvas.pack()

        self.register_button = customtkinter.CTkButton(window, text="Registrar", command=register)
        self.register_button.pack()

        self.update_webcam()
    
    def update_webcam(self):
        ret, frame = self.video_capture.read()
        if ret:
            self.current_image = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
            self.photo = ImageTk.PhotoImage(image=self.current_image)
            self.canvas.create_image(0,0, image=self.photo, anchor=customtkinter.NW)
            self.window.after(15, self.update_webcam)

root = customtkinter.CTk()
app = WebcamAPP(root)
root.mainloop()
