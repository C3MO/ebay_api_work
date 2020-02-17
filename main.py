from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *

if __name__ == "__main__":
    m = Tk(className="Produktsuche - Händler")
    m.geometry("800x500")
    labMain = tk.Label(m,text = 'Reparatur/Produkt Preise')
    labMain.pack(side = 'top')
    l1 = tk.Label(m, text ='Geben sie ihr gesuchtes Produkt ein: ')
    l1.pack(side = LEFT, anchor ='n')
    e1 =tk.Entry(m, width = 55)
    #e1.insert()
    e1.pack(side = 'left', anchor= 'n')
    button1 = tk.Button(m, text='Suchen', command=m.destroy)
    button1.pack(side= 'right', anchor = 'n')
    m.mainloop()

makeNum = ['1','2','3','4','5','6','7','8','9','0','.']
Keywords = input('Enter what you would like to search for: ')
api = finding(appid = 'CemSaygi-PythonSe-PRD-9b44724db-b657c8b2', config_file = 'ebay.yml')
api_request = {'keywords': Keywords, 'outputSelector': 'SellerInfo'}

response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content, 'lxml')

totalentries = soup.find('totalentries')
print (totalentries)
items = soup.find_all('item')


urlNumber = 0
for item in items:
    num = ''
    cat = item.categoryname.string.lower()
    title = item.title.string.lower()
    price = str(item.currentprice)
    for i in price:
        if i in makeNum:
            num += i
    url = item.viewitemurl.string.lower()
    if 'delid' in title:
        pass

    elif float(num):
        print ("___________________")
        print ('Url number: ' + str(urlNumber))
        print ('Category: ' + cat)
        print ('Title: ' + title)
        print ('Price: ' + num +'€' )
        print ("___________________")
        print ("*~*~*~*~*~*~*~*~*~*")
    urlNumber += 1





