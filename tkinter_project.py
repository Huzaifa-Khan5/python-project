from tkinter import *
import webbrowser

def search():
    taburl="http://google.com/?#q="
    entry_value=entry.get()
    answer_value=webbrowser.open(taburl+entry_value)

def openyoutube():
    youtubelink=webbrowser.open("https://youtube.com/")
    
def openfacebook():
    facebooklink=webbrowser.open("https://www.facebook.com/")
    
def opengmail():
    gmaillink=webbrowser.open("https://accounts.google.com/b/0/AddMailService")

def openstackoverflow():
    stackoverflowlink=webbrowser.open("https://stackoverflow.com/")

#creating a window
root=Tk()
root.title("Drop Fix search page")
root.geometry('650x600+270+50')

#creating a top frame
topframe=Frame(root)

#creating a label
logo=PhotoImage(file="logo2.png")
label=Label(root)
resizelogo=logo.subsample(2,3)
label.config(image=resizelogo)
label.pack()

# creating a entry
entry=Entry(topframe,width=40,font=('BellMT',16))
entry.pack(side=LEFT,pady=40)

iconsearch=PhotoImage(file="icon search.png")
yimage=PhotoImage(file="icon.png")
fimage=PhotoImage(file="icon f.png")
gimage=PhotoImage(file="icon g.png")
simage=PhotoImage(file="icon s.png")

# creating a search button
button=Button(topframe,command=search,width=25,height=25)
resizeImg=iconsearch.subsample(8,8)
button.config(image=resizeImg)
button.pack(side=LEFT,padx=20)
topframe.pack()


#creating a middle frame
middleframe=Frame(root)
middleframe.pack()

#creating youtube button
youtubebutton=Button(middleframe,bg="white",command=openyoutube,width=70,height=45)
yresizeimage=yimage.subsample(4,4)
youtubebutton.config(image=yresizeimage)
youtubebutton.pack(side=LEFT,padx=65)

#creating facebook button 
facebookbutton=Button(middleframe,bg="blue",command=openfacebook,width=70,height=45)
fresizeimage=fimage.subsample(3,4)
facebookbutton.config(image=fresizeimage)
facebookbutton.pack(side=LEFT)

#creating gmail button
gmailbutton=Button(middleframe,bg="white",command=opengmail,width=70,height=45)
gresizeimage=gimage.subsample(4,4)
gmailbutton.config(image=gresizeimage)
gmailbutton.pack(side=LEFT,padx=65)

#creating stack over flow button
stackoverflowbutton=Button(middleframe,bg="white",command=openstackoverflow,width=70,height=45)
sresizeimage=simage.subsample(4,4)
stackoverflowbutton.config(image=sresizeimage)
stackoverflowbutton.pack(side=LEFT)
middleframe=Frame(root)
middleframe.pack()

#creating youtube label
ylabel=Label(middleframe,text="Youtube",font="BellMT,20")
ylabel.pack(side=LEFT,padx=85)

#creating facebook label
flabel=Label(middleframe,text="Facebook",font="BellMT,20")
flabel.pack(side=LEFT)

#creating gmail label
glabel=Label(middleframe,text="Gmail",font="BellMT,")
glabel.pack(side=LEFT,padx=70)

#creating stack overflow label
slabel=Label(middleframe,text="Stack overflow",font="BellMT,20")
slabel.pack(side=LEFT)

root.mainloop()