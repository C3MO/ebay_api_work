from ebaysdk.finding import Connection as finding
from bs4 import BeautifulSoup

makeNum = ['1','2','3','4','5','6','7','8','9','0','.']
Keywords = input('Enter what you would like to search for: ')
maxprice = input('Enter the maximum price you would like to search for: ')

api = finding(appid = 'CoryChes-JustASim-PRD-1c6cc25dc-b7a70e4e', config_file = None)
api_request = {'keywords': Keywords, 'outputSelector': 'SellerInfo'}

response = api.execute('findItemsByKeywords', api_request)
soup = BeautifulSoup(response.content, 'lxml')

totalentries = soup.find('totalentries')
print (totalentries)
items = soup.find_all('item')

print
print

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

    elif float(num) <= float(maxprice):
        print ("___________________")
        print ('Url number: ' + str(urlNumber))
        print ('Category: ' + cat)
        print ('Title: ' + title)
        print ('Price: ' + num)
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