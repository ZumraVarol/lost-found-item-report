import tkinter as tk
def lostButton():
    itemsLost=[]
    def apply():
        i=itemType.get()#belleğe almak için
        d=reportDate.get()
        t=reportTime.get()
        c=communication.get()
        list=[i,d,t,c]
        itemsLost.append(list)#listeye almak için (bu kısım daha sonra MySQL ile ortak dataya atılacak)
        print(list)
    lostWindow=tk.Tk()
    lostWindow.title("Lost Item Report")#arayüz başlığı
    lostWindow.geometry("400x500")
    lostWindow.config(background="black")#arayüz rengi

    text1 = tk.Label(lostWindow,text="--Lost Item Report--", font="Times 20 italic", fg="white", bg="black")#text
    text1.pack()
    # lost item type giriş
    typeText = tk.Label(lostWindow, text="Please enter the type of lost item ", font="Times", fg="white", bg="black")
    typeText.pack()
    itemType = tk.Entry(lostWindow)
    itemType.pack()
    # report date giriş
    dateText = tk.Label(lostWindow, text="Please enter the report date ", font="Times", fg="white", bg="black")
    dateText.pack()
    reportDate = tk.Entry(lostWindow)
    reportDate.pack()
    #report time giriş
    timeText = tk.Label(lostWindow, text="Please enter the report time ", font="Times", fg="white",bg="black")
    timeText.pack()
    reportTime=tk.Entry(lostWindow)
    reportTime.pack()
    # iletişim bilgilerini alma
    communicationText = tk.Label(lostWindow, text="Please enter the contact information", font="Times", fg="white", bg="black")
    communicationText.pack()
    communication = tk.Entry(lostWindow)
    communication.pack()
    # dataya kaydetme butonu
    enter=tk.Button(lostWindow,text="ENTER",command=apply)
    enter.pack()

    lostWindow.mainloop()