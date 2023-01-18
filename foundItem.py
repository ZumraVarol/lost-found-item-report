import tkinter as tk
def foundButton():
    itemFound=[]
    def apply():
        i=itemType.get()#belleğe almak için
        d=reportDate.get()
        t=reportTime.get()
        list=[i,d,t]
        itemFound.append(list)#listeye almak için (bu kısım daha sonra MySQL ile ortak dataya atılacak)
        print(list)
    foundWindow=tk.Tk()
    foundWindow.title("--Found Item Report--")# arayüz başlığı
    foundWindow.geometry("400x500")
    foundWindow.config(background="black")#arayüz rengi

    text1 = tk.Label(foundWindow,text="Found Item Report", font="Times 20 italic", fg="white", bg="black")#text
    text1.pack()
    # found item type giriş
    typeText = tk.Label(foundWindow, text="Please enter the type of lost item ", font="Times", fg="white", bg="black")
    typeText.pack()
    itemType = tk.Entry(foundWindow)
    itemType.pack()
    # report date giriş
    dateText = tk.Label(foundWindow, text="Please enter the report date ", font="Times", fg="white", bg="black")
    dateText.pack()
    reportDate = tk.Entry(foundWindow)
    reportDate.pack()
    # report time girişi
    timeText = tk.Label(foundWindow, text="Please enter the report time ", font="Times", fg="white",bg="black")
    timeText.pack()
    reportTime=tk.Entry(foundWindow)
    reportTime.pack()
    # dataya kaydetme butonu
    enter=tk.Button(foundWindow,text="ENTER",command=apply)
    enter.pack()

    foundWindow.mainloop()