from bs4 import BeautifulSoup
import requests
import urllib.request


result = requests.get("https://dicocitations.lemonde.fr/phrases-mot-meilleur-2.php")
print (result.status_code)
amitie = []
src =result.content
soup = BeautifulSoup(src , 'lxml')
for img in soup.find_all('blockquote'):
    temp = img.get('font color="black" size="3"')
    amitie.append(img)




truc = amitie[1]
truc = str(truc)
truc=truc.replace('<blockquote><font color="black" size="3">'," ")


for i in range (len(amitie)):
    amitie[i] = str(amitie[i])
    for j in range (50000):
        j = str(j)
        amitie[i] = amitie[i].replace('<blockquote><font size="3"><a class="lienmot" href="/citation_auteur_ajout/'+j+'.php" title="Lien permanent citation n° : '+j+'">'," ")
        amitie[i] = amitie[i].replace('</a></font></blockquote>'," ")


for i in amitie :
    print(i)

file = open("texte_test.txt","w+")
for i in amitie :
    file.write(i)
    file.write("\n")
file.close()