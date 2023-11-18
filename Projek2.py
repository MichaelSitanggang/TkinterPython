#Converse IMG
import sys
from PIL import ImageTk , Image
from threading import Thread

import tkinter as tk
from tkinter import ttk, filedialog

x = 500
y = 600

class ImageConverter(tk.Frame):
    def __init__(self,window):
        super().__init__(window)
        self.init_ui()
    def init_ui(self):
        self.pack()
        self.label = tk.Label(self,text="IMAGE CONVERTER",font=("Helvetica",20))
        self.label.pack()
        self.btn = tk.Button(self,text="Load Image",command=self.open_image)
        self.btn.pack()
        self.imageFrame = tk.LabelFrame(self,text="Image View")
        self.imageFrame.pack()
        self.labelimage = tk.Label(self.imageFrame,width=100,height=25)
        self.labelimage.pack()
        self.convertbtn = tk.Button(self,text="Convert Button")
        self.convertbtn.pack()
        self.comboBox = ttk.Combobox(self)
        self.comboBox['value'] = ['BMP','GIF','JPEG','PNG','TIFF']
        self.comboBox.pack()
        self.progress = ttk.Progressbar(self)
        self.progress.pack()
        self.convertbtn.bind('<Button-1>',self.run_trading)

    def open_image(self):
        try:
            self.filename = filedialog.askopenfilename()
            if self.filename:
                self.img = Image.open(self.filename)
                self.x = int(self.img.size[0] * 0 + x * .50)
                self.y = int(self.img.size[1] * 0 + y * .60)
                self.img2 = self.img.resize((self.x, self.y))
                self.imgTk = ImageTk.PhotoImage(self.img2)
                self.labelimage.config(image=self.imgTk, width=300, height=400)
            else:
                print("Pemilihan file dibatalkan.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


    def run_trading(self,event):
        t = Thread(target=self.convert_img)
        t.start()

    def convert_img(self):
        self.progress.start()
        self.format = self.comboBox.get()
        self.img.save(f"convertedImage.{self.format}") 

        for i in range(100):
            self.progress['value'] = i  
            self.update_idletasks()  

        self.progress.stop()

        self.top = tk.Toplevel(width=300, height=200)
        self.topLabel = tk.Label(self.top, text="Convert Berhasil silahkan cek di direktori komputer anda !")
        self.topLabel.pack()



window = tk.Tk()
gui = ImageConverter(window)
window.geometry(f"{x}x{y}")
window.mainloop()
