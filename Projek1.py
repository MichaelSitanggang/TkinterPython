#Program CONVERSE USD TO IDR
import tkinter as tk
class Converse:
    def __init__(self,root):
        self.root = root
        self.root.title("USD -> IDR Converse")
        self.root.geometry("400x150")

        self.label1 = tk.Label(self.root,text="USD ($)",font=("helvetica",12,'bold'))
        self.label1.pack()

        self.text1 = tk.Entry(self.root,font=("helvetica",15,"bold"),width=30,justify=tk.CENTER)
        # self.text1.insert(tk.END, "$")
        self.text1.pack()

        self.button = tk.Button(self.root,text="TO",command=self.usd_to_idr)
        self.button.pack()

        self.text2 = tk.StringVar()
        self.text2.set("IDR")

        self.label2 = tk.Entry(self.root,font=("helvetica",15,"bold"),width=30,justify=tk.CENTER,textvariable=self.text2)
        self.label2.pack() 

    def usd_to_idr(self):
        try :
            angka = self.text1.get()
            dollar = float(angka) * 14405.5
            self.text2.set("RP. " + str(dollar))
            self.label2.config(font=("helvetica",15,"bold"),fg="green")
        except ZeroDivisionError as error :
            raise Exception("ADA YANG ERROR DI PROGRAM")

def main():
    window = tk.Tk()
    Converse(window)
    window.mainloop()

if __name__ == "__main__":
    main()
