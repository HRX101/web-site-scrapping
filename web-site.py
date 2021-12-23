import requests
from bs4 import BeautifulSoup, builder
from tkinter import *
root=Tk()
root.title("Web-check")
root.geometry('400x500')
label=Label(text="Enter your site")
label.pack(padx=1,pady=10)
entry=Entry()
entry.pack()
label=Label(text="Enter what you wanna do scapping")
label.pack(padx=1,pady=10)
entry2=Entry()
entry2.pack()
def take_site():
    pes=entry.get()
    pes2=entry2.get()
    ret= "https://www."+pes+".ac.in"
    print(ret)
    res=requests.get(ret)
    soup=BeautifulSoup(res.content,"html.parser")
    result=soup.find(pes2)
    print(result)
    entry1=Entry()
    
    entry1.pack()
    button1=Button(text="export",command=lambda:export(result,entry1))
    button1.pack()
button=Button(text="submit",command= take_site)
button.pack()

def export(result,entry1):
    es=entry1.get()
    es=es+"."+"txt"
    result=(str(result))
    result=result.split()
    file=open(es,"w")
    file.writelines(result)
    file.close()

root.mainloop()