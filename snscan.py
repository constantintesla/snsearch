from bs4 import BeautifulSoup
from urllib.request import urlopen
f = open("ciscoips.txt",'r')
ips = f.readlines() 
with open("sn.txt", "w") as text_file:
    for i in ips:
        url = "http://"+ i 
        soup = BeautifulSoup(urlopen(url).read())
        LL = soup.get_text()
        lst = []
        lst = LL.split()
        m=lst.index('Phone')
        model = lst[m+1]
        snn=lst.index('Серийный')
        serial = lst[snn+1]
        text_file.write(model+" "+ serial+" "+url+ '\n')
        print(model+" "+ serial+" "+url+ '\n')