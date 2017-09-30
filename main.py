###########################################################################
# Projet AstroPi 2016 --- Seconde 10 - Lycee Francois Mauriac (Bordeaux)
# 
# Equipe programmation des detections :
#
# Matteo Christophe / Zakariya Bourajaa / Quentin Cologni
# Tom Delmonteil / Martin Genebes / Gaetan Bonneau
# Nicolas Jarrige /Louis Pejoine / Malo Lebreton / Gabin Poncelet
# Josselin Lebas / Leo Lopez-Laiguillon / Audric Nys-Daymard 
# Theo Parrou / Aymerick Samba / Marco Sloim Dafonte 
#
#########################################################################



from sense_hat import SenseHat
import time
import csv
# pour la lecture du fichier csv contenant les heures de lever
# et coucher du soleil a Rome.

import ephem 
# l'idee d'utilisation de la librairie PyEphem pour le calcul
# de la position de l'ISS vient du code "ISS_Tracker" de la Thirsk School
# (www.thirskschool.org), lors de leur contribution au Challenge AstroPi 2015.
# Voir https://github.com/astro-pi/iss-tracker

import animations
# fichier local contenant toutes les animations realisees par
# l'autre partie de la classe


s = SenseHat()
s.low_light = True
s.rotation = 270



f=open('data_FM.csv','a') 
f.write('timestamp,humidite,accX,accY,accZ,latitude,longitude,commentaire \n')	
f.close()

with open('rome.csv') as csvfile:
	liste=csv.DictReader(csvfile)
	for ligne in liste:
		if ligne['date']==time.strftime("%Y-%m-%d"):
			Hlever=ligne['sunrise']
			Hcoucher=ligne['sunset']



def calibrage():
	print("Veuillez patienter pendant le calibrage")
	nbvaleurs=60 #nombre de donnees necessaires
	animations.roueAttente()
	global MoyHum,MaccX,MaccY,MaccZ
	S_Hum=0
	SaccX=0
	SaccY=0
	SaccZ=0
	for k in range(nbvaleurs): 
		if k==0:
			animations.calib0() #afin d'afficher une barre de progression du calibrage
		if k==10:
			animations.calib1()
		if k==20:
			animations.calib2()
		if k==30:
			animations.calib3()
		if k==40:
			animations.calib4()
		if k==50:
			animations.calib5()
		if k==58:
			animations.calib6()
		time.sleep(1)
		h=s.get_humidity()
		S_Hum=S_Hum+h
		accX=s.get_accelerometer_raw()['x']
		accY=s.get_accelerometer_raw()['y']
		accZ=s.get_accelerometer_raw()['z']
		SaccX=SaccX+accX
		SaccY=SaccY+accY
		SaccZ=SaccZ+accZ
	MoyHum=round(S_Hum/nbvaleurs,2)
	MaccX=round(SaccX/nbvaleurs,2)
	MaccY=round(SaccY/nbvaleurs,2)
	MaccZ=round(SaccZ/nbvaleurs,2)
	ecritureCommentairesFichierData("MoyHum : "+str(MoyHum))
	ecritureCommentairesFichierData("MaccX : "+str(MaccX))
	ecritureCommentairesFichierData("MaccY : "+str(MaccY))
	ecritureCommentairesFichierData("MaccZ : "+str(MaccZ))
	print("fin du calibrage")
	animations.finCalibrage()
	

def ecritureMesuresFichierData():
	h=round(s.get_humidity(),2)
	accX=round(s.get_accelerometer_raw()['x'],3)
	accY=round(s.get_accelerometer_raw()['y'],3)
	accZ=round(s.get_accelerometer_raw()['z'],3)
	f=open('data_FM.csv','a') 
	f.write(time.strftime("%d/%m/%y %H:%M:%S")+','+str(h)+','+ str(accX) + ','+ str(accY)+','+ str(accZ)+ ','+str(latitude)+ ','+ str(longitude)+'\n')	
	f.close()

def ecritureCommentairesFichierData(text):
	f=open('data_FM.csv','a') 
	f.write(",,,,,,,"+text+'\n')	
	f.close()


def detectionPresence(): #MISSION 1
	seuilH=4
	h=s.get_humidity()
	if h>MoyHum+seuilH:
		ecritureMesuresFichierData()
		ecritureCommentairesFichierData("presence detectee")
		animations.detectionHumain()

def detectionPoussee(): #MISSION 2
	seuilP=0.01
	accX=s.get_accelerometer_raw()['x']
	accY=s.get_accelerometer_raw()['y']
	accZ=s.get_accelerometer_raw()['z']	
	if abs(accX-MaccX)>seuilP or abs(accY-MaccY)>seuilP or abs(accZ-MaccZ)>seuilP:
		ecritureMesuresFichierData()
		ecritureCommentairesFichierData("poussee detectee")
		animations.detectionPoussee()
		
def testPositionISS(): #EasterEgg 1
	global latitude
	global longitude
	#informations TLE a remettre a jour sur https://www.celestrak.com/NORAD/elements/stations.txt
	name= "ISS (ZARYA)"             
	line1= "1 25544U 98067A   17054.55909344  .00002977  00000-0  51677-4 0  9991"
	line2="2 25544  51.6410 244.7310 0006703 220.6438 244.9238 15.54421533 44082"


	posISS=ephem.readtle(name,line1,line2)
	posISS.compute()
	latitude=str(posISS.sublat).split(':')[0]
	longitude=str(posISS.sublong).split(':')[0]

	if 41<int(latitude)<49 and 0<int(longitude)<9:
		ecritureCommentairesFichierData("survol de la France")
		animations.coqFrance()
	if 39<int(latitude)<47 and 9<int(longitude)<17: 
		ecritureCommentairesFichierData("survol de l'Italie")
		animations.coeurItalie()



def testLeverCoucherSoleil(): #EasterEgg 2
	if time.strftime("%H:%M")==Hlever:
		animations.leverSoleil1()
		animations.leverSoleil2()
		
	if time.strftime("%H:%M")==Hcoucher:
		animations.coucherSoleil()
	



#debut programme

animations.debut()

calibrage()
animations.testAnniversaires()
animations.mouvementISS()
testPositionISS() 
start=time.time()
print("debut de la mission")
print("duree prevue : 2h")
while time.time()-start<7200 : #boucle de 7200 secondes

    	if time.localtime().tm_sec%10==0 : #toutes les 10 sec
    		testPositionISS() 
	        ecritureMesuresFichierData()
		time.sleep(1)
    	if time.localtime().tm_sec==5 : #toutes les minutes
	        testLeverCoucherSoleil()
	        
	if time.localtime().tm_sec%2==0 :	#chaque seconde paire
		animations.attenteBouclePair()
	else:
		animations.attenteBoucleImpair() #chaque seconde impaire
		
	detectionPresence() #Mission 1
	detectionPoussee() #Mission 2

	
print("fin du programme")
animations.fin()
animations.end()
s.clear()



