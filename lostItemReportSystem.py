#kayıp eşya bölümüne girince önce kayıp bildirimi mi yoksa bulunma bildirimi mi yapacağımızı seçtirecek ekran
#kayıp bildirimi için: eşyanın türü, kayıt saati tarihi, iletişim bilgileri
#bulma bildirimi için: eşyanın türü kayıt saati tarihi
#ikisinden biri diğeriyle uyuyorsa ekrana yazdır
#uymuyorsa:kayıt tamamlandı yazdır
import tkinter as tk
import foundItem
import lostItem

window = tk.Tk()
window.title("Lost & Found Item Report")#arayüz başlığı
window.geometry("400x500")#arayüz boyutu
window.configure(background="black") #arayüz rengi

text1=tk.Label(text="Lost Item Reporting System",font="Times 23 italic",fg="white",bg="black")#text özellikleri
text1.pack()

lostButton=tk.Button(text="Lost Item Report",font="Times 15 bold",bg="black",fg="white",command=lostItem.lostButton)#lost item buton lostItem.py ile bağlantılı
lostButton.place(x=120,y=190)#lost item buton yeri
lostButton.pack()

foundButton=tk.Button(text="Found Item Report",font="Times 15 bold",bg="black",fg="white",command=foundItem.foundButton)#found item buton foundItem.py ile bağlantılı
foundButton.place(x=113,y=260)#found item buton yeri
foundButton.pack()

# cikis=tk.Button(text="çıkış",command=window.quit)
# cikis.pack()
window.mainloop()



