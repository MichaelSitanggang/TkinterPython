import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x150")

        self.label = tk.Label(self.root,text="KALKULATOR SEDERHANA",font=("helvetica",12,"bold"))
        self.label.pack()
        
        self.angka1 = tk.Entry(self.root, justify=tk.CENTER)
        self.angka1.pack()

        self.operator_frame = tk.Frame(self.root)
        self.operator_frame.pack()

        self.tambah = tk.Button(self.operator_frame, text="+", width=1,command=lambda: self.calculator("+"), bg="red")
        self.tambah.pack(side=tk.LEFT)

        self.kurang = tk.Button(self.operator_frame, text="-", width=1, command=lambda: self.calculator("-"))
        self.kurang.pack(side=tk.LEFT)

        self.kali = tk.Button(self.operator_frame, text="X",width=1,command=lambda: self.calculator("x"))
        self.kali.pack(side=tk.LEFT)

        self.bagi= tk.Button(self.operator_frame, text="/",width=1,command=lambda: self.calculator("/"))
        self.bagi.pack(side=tk.LEFT)

        self.pangkat = tk.Button(self.operator_frame,text="^",width=1,command=lambda: self.calculator("^"))
        self.pangkat.pack(side=tk.LEFT)

        self.angka2 = tk.Entry(self.root,justify=tk.CENTER)
        self.angka2.pack()

        self.text2 = tk.StringVar()
        self.text2.set("Hasil")

        self.label2 = tk.Entry(self.root,font=("helvetica",15,"bold"),width=12,justify=tk.CENTER,textvariable=self.text2,fg="white")
        self.label2.pack() 

    def calculator(self,operator):
        try :
            num1 = float(self.angka1.get())
            num2 = float(self.angka2.get())
            result = 0
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "x":
                result = int(num1) * int(num2)
            elif operator == "/":
                if num2 != 0 :
                    result = num1 / num2
                else :
                    self.text2.set("tidak dapat membagi dengan nol")
                    return
            elif operator == "^":
                result = int(num1) ** int(num2)
            self.text2.set(result)
        except ValueError:
            self.text2.set("Masukkan angka yang valid")



def main():
    window = tk.Tk()
    Calculator(window)
    window.mainloop()

if __name__ == "__main__":
    main()
