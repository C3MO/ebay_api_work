from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import *

if __name__ == "__main__":
    m = tk.Tk()
    m.title('Produktsuche')
    back = tk.Frame(master=m, width=800, height=500, bg='black')
    Label(m, text='Geben sie ihr gewünschtes Produkt ein!').grid(row=0)
    e1 = tk.Entry(m)
    e1 = tk.Entry(row=0, column=1)
    #button = tk.Button(m, text='Suchen', width=25, command=m.destroy)
    #button.pack()
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

while True:
    inpu = input('Enter a URL Number to get the items URL: ')
    try:
        inpu = int(inpu)
        print (items[inpu]).viewitemurl
    except:
        if inpu.lower() == 'exit':
            break
        else:
            print ('Please enter a URL number or enter exit if you would like to exit')




