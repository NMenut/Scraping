from bs4 import BeautifulSoup
import requests
from urllib.request import Request , urlopen
import time
import os 
import shutil


os.system('clear')
demande = input("Quel theme voulez-vous scraper ? :")
src = "https://negativespace.co/?s=" + demande
result = requests.get(src)
verif = result.status_code
if verif == 200 :
    print("Acces to the target accepeted")
    time.sleep(2)
else :
    print("failed : you can't access to the target")
    time.sleep(2)

src = result.content

src = result.content
soup = BeautifulSoup(src , 'lxml')
print ("\n")



for img in soup.find_all('img'):
    temp = img.get('src')
    if temp[:1]=="/":
        image = "https://negativespace.co/?s=nature"+temp
    
    else :
        image= temp
    

    nametemp = img.get('alt')
    if len(nametemp)==0 :
        filename = str(i)
        i = i+1
    else :
        filename = nametemp
    
    imagefile = open("img/"+filename + ".jpeg","wb")
    req = Request(image,headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    imagefile.write(webpage)
    """
    imagefile.write(urllib.request.urlopen(image,headers={'User-Agent': 'Mozilla/5.0'}).read())
    """

    src = 'img'
    dst = '/home/Nicolas.Menut/Bureau/dossier_stage/Scraping/'+demande
    imagefile.close()
    try:
        shutil.copytree(src, dst)
    except FileExistsError:
        shutil.rmtree(dst)
        shutil.copytree(src, dst)

for i in soup.find_all('img') :
    print(i) 

for filename in os.listdir(src) :
    os.remove(src + "/" + filename)