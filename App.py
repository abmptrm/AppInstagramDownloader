from tkinter import * 
import tkinter.messagebox 
import webbrowser

class IGDown():
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Downloader")

        canvas = Canvas(root, width=600, height=590)
        canvas.grid(columnspan=5, rowspan=5)

        # logo 
        logo = PhotoImage(file="Logo3.png")
        potoLabel = Label(image=logo)
        potoLabel.image = logo
        potoLabel.grid(row=0 , column=2)

        # var 
        urlIG = StringVar()
        userNameIG = StringVar()
       
        #intruksi
        intruksi = Label(root, text="Url Post", font=("Raleway",10, "bold"))
        intruksi.grid(row=1, column=2)

        # func

        def iReset():
            urlIG.set("")
            return

        def iExit():
            Exit = tkinter.messagebox.askyesno(
                "Instagram Downloader", "Kamu Yakin Mau Keluar ?")
            if Exit > 0:
                root.destroy()
                return

        def Urlink():
            item = urlIG.get()

            if item.istitle:

                #item
                downloadUrl = 'savefrom.net/' + item
                webbrowser.open_new_tab(downloadUrl)
              
                tkinter.messagebox.showinfo(
                "Instagram Downloader", "  Mantap :)  ")
                return True
                
            else:
                tkinter.messagebox.showwarning(
                "Instagram Downloader", "Goblok :v")
                urlIG.set("")
                return False

        #Link Entry
        self.linkUrl = Entry(root,
            textvariable=urlIG, width=25)
        self.linkUrl.grid(row=2, column=2 )

        #Button Sumbit 
        self.btnSumbit = Button(root, text="Sumbit", command=Urlink,
            font=("Raleway", 10))
        self.btnSumbit.place(x=200, y=500)

        #Button exit
        self.btnExit = Button(root, text="Exit", command=iExit,
            font=("Raleway", 10))
        self.btnExit.place(x=350, y=500)

        # Button Reset 
        self.ResetButton = Button(root, text="Reset",
            command=iReset,
            font=("Raleway", 10))
        self.ResetButton.place(x=280, y=500) 




if __name__ == "__main__":
    root = Tk()
    app = IGDown(root)
    root.mainloop()
