# -*- coding: utf-8 -*-

"""
////////////////////////////////////////////////
/coding by MENUT_Nicolas:(technicien stagiaire)/
////////////////////////////////////////////////
"""

from random import *
import os
from PIL import ImageFont
from fonts.ttf import AmaticSC
import sys
import shutil
from PIL import Image
import sys
try:
    from PIL import Image
except ImportError:
    import Image
try:
    from PIL import ImageDraw
except ImportError:
    import ImageDraw
try:
    from PIL import ImageFont
except ImportError:
    import ImageFont

amitie = []
file = open("/home/Nicolas.Menut/Bureau/dossier_stage/Scraping/texte_test.txt",'r')
for i in file:
      amitie.append(i)

for i in amitie :
      print i 

tabl1 = []
tabl2 = []
src1 = "/home/Nicolas.Menut/Bureau/dossier_stage/Scraping/sport"
src2 = "/home/Nicolas.Menut/Bureau/dossier_stage/Scraping/ocean"
for filename in os.listdir(src1):
      tabl1.append(src1 + "/"+filename)

for filename in os.listdir(src2):
      tabl2.append(src2 + "/"+filename)

demande = raw_input("combien d'image voulez-vous générer ? : ")
demande = demande.lstrip().rstrip()
demande = int(demande)
odd = 0
while odd != demande :
      n1 = randint(0 , len(tabl1)-1)
      n2 = randint(0 , len(tabl2)-1)

      # ouverture du fichier image
      ImageFile = tabl1[n1]
      try:
        img = Image.open(ImageFile)
      except IOError:
        print 'Erreur sur ouverture du fichier ' + ImageFile
        sys.exit(1)
      # affichage des caractéristiques de l'image
      print img.format,img.size, img.mode
      """
      # affichage de l'image
      img.show()
      # fermeture du fichier image
      img.close()
      """
      colonne1,ligne1 = img.size
      # ouverture du fichier image
      ImageFile = tabl2[n2]
      try:
        img2 = Image.open(ImageFile)
      except IOError:
        print 'Erreur sur ouverture du fichier ' + ImageFile
        sys.exit(1)
      # affichage des caractéristiques de l'image
      print img2.format,img2.size, img2.mode

      colonne2,ligne2 = img2.size

      colonne = min(colonne1, colonne2)
      ligne = min(ligne1,ligne2)
      imgF = Image.new(img.mode,img.size)
      for i in range(ligne):
            for j in range(colonne):
              p1 = img.getpixel((j,i))
              p2 = img2.getpixel((j,i))
              p = (max(p1[0],p2[0]),max(p1[1],p2[1]),max(p1[2],p2[2]))
              imgF.putpixel((j,i), p)




      """
      for i in range(ligne):
            for j in range(colonne):
                pixel = img.getpixel((j,i))
                # récupération du pixel
                # on calcule le complement à MAX pour chaque composante - effet négatif
                p = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
                # composition de la nouvelle image
                imgF.putpixel((j,i), p)
      """
      draw = ImageDraw.Draw(imgF)
      n3 = randint(0,len(amitie)-1)
      txt = amitie[n3]
      dra = randint(0,255)
      gon = randint(0,255)
      ball = randint(0,255)
      dra = str(dra)
      gon = str(gon)
      ball = str(ball)
      #color = 'rgb('+dra+','+gon+','+ball+')'
      color = 'rgb(0,0,0)'
      longueur = len(txt)
      longu = 1+longueur/2
      check = 4
      ntabl = []
      if longueur > 75 :
          check = 1
          ntabl.append(amitie[n3][:longu])
          ntabl.append(amitie[n3][longu:])
    


      print "LONGUEUR : ",longueur
      if check == 1 :

        a = 1062 - longueur 
        b = randint(0,708)
        c = randint(0,a)
        font = ImageFont.truetype(AmaticSC,50)
        #font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 20)
        draw.text( (c/2,b), unicode(ntabl[0],'UTF-8'),fill = color ,  font=font)
        draw.text( (c/2,b+40), unicode(ntabl[1],'UTF-8'),fill = color ,  font=font)
      else:

        a = 1062 - longueur 
        b = randint(0,708)
        c = randint(0,a)
        font = ImageFont.truetype(AmaticSC,50)
        #font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 20)
        draw.text( (c/4,b), unicode(txt,'UTF-8'),fill = color ,  font=font)

      imgF.show()

      

      de = raw_input("Voulez-vous enregistrer le tout ? (y/n) : ")
      if de == "y":
        alpha = odd
        alpha = str(alpha)
        imgF.save("img/"+alpha+".jpeg")
      

      else :
        print "Annulation"
      imgF.close()
      odd +=1


print "FIN PROGRAMME"

