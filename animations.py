###########################################################################
# Projet AstroPi 2017 --- Seconde 10 - Lycee Francois Mauriac (Bordeaux)
# 
# Equipe affichage et animations
#
# Lea Delamour / Lisa Douangphrachanh / Hanae Aliouate
# Marie Girard / Manon Boucheron / Felix Boutet
# Thibault Heytmann / Lael Boco / Lea Megardon
# Guy Bie Endamne / Anna San Millan / Zoe Vimpere / Felix Lamarcade
# Florian Sonnet / Raphael Valiergue / Arthur Laforest
# Matheo Miart / Chadi Mourad
#
######################################################################

import time

from sense_hat import SenseHat

s = SenseHat()
s.rotation=270

#########################################################
def sunset2():

	O=(0, 158, 255)
	O1=(0, 141, 255)
	O2=(0, 128, 255)
	O3=(133, 177, 205)
	O4=(172, 196, 211)
	O5=(189, 118, 55)
	O6=(255, 107, 0)
	O7=(255, 102, 0)



	B1 = (0, 191, 255)
	B2 = (0, 158, 211)
	B3 = (2, 115, 153)
	B4 = (8, 106, 135)
	B5 = (255, 128, 48)
	B6 = (233, 175, 61)
	B7 = (180, 95, 4)
	B8 = (255, 85, 4)
	B9 = (211, 56, 3)

	S1 = (252, 255, 0)
	S2 = (252, 192, 0)
	S3 = (255, 154, 0)
	S4 = (255, 128, 0)
	S5 = (255, 111, 0)
	S6 = (255, 102, 0)
	S7 = (255, 85, 0)

	soleilcouchant=[
	[
	    O, O, S1, S1, S1, S1, O, O,
	    O, O, O, S1, S1, O, O, O,
	    O, O, O, O, O, O, O, O,
	    O, O, O, O, O, O, O, O,
	    O, O, O, O, O, O, O, O,
	    O, O, O, O, O, O, O, O,
	    B1, B1, B1, B1, B1, B1, B1, B1,
	    B1, B1, B1, B1, B1, B1, B1, B1,
	]
	,
	[
	    O1, O1, S2, S2, S2, S2, O1, O1,
	    O1, O1, S2, S2, S2, S2, O1, O1,
	    O1, O1, O1, S2, S2, O1, O1, O1,
	    O1, O1, O1, O1, O1, O1, O1, O1,
	    O1, O1, O1, O1, O1, O1, O1, O1,
	    O1, O1, O1, O1, O1, O1, O1, O1,
	    B2, B2, B2, B2, B2, B2, B2, B2,
	    B2, B2, B2, B2, B2, B2, B2, B2,
	]
	,
	[
	    O2, O2, O2, S3, S3, O2, O2, O2, 
	    O2, O2, S3, S3, S3, S3, O2, O2, 
	    O2, O2, S3, S3, S3, S3, O2, O2, 
	    O2, O2, O2, S3, S3, O2, O2, O2,
	    O2, O2, O2, O2, O2, O2, O2, O2,
	    O2, O2, O2, O2, O2, O2, O2, O2,
	    B3, B3, B3, B3, B3, B3, B3, B3,
	    B3, B3, B3, B3, B3, B3, B3, B3,
	]
	,
	[
	    O4, O4, O4, O4, O4, O4, O4, O4,
	    O4, O4, O4, S4, S4, O4, O4, O4,
	    O4, O4, S4, S4, S4, S4, O4, O4,
	    O4, O4, S4, S4, S4, S4, O4, O4,
	    O4, O4, O4, S4, S4, O4, O4, O4,
	    O4, O4, O4, O4, O4, O4, O4, O4,
	    B4, B4, B4, B4, B4, B4, B4, B4,
	    B4, B4, B4, B4, B4, B4, B4, B4,
	]
	,
	[
	    O5, O5, O5, O5, O5, O5, O5, O5,
	    O5, O5, O5, O5, O5, O5, O5, O5,
	    O5, O5, O5, S5, S5, O5, O5, O5,
	    O5, O5, S5, S5, S5, S5, O5, O5,
	    O5, O5, S5, S5, S5, S5, O5, O5,
	    O5, O5, O5, S5, S5, O5, O5, O5,
	    B5, B5, B5, B5, B5, B5, B5, B5,
	    B5, B5, B5, B5, B5, B5, B5, B5,
	]
	,
	[
	    O6, O6, O6, O6, O6, O6, O6, O6,
	    O6, O6, O6, O6, O6, O6, O6, O6,
	    O6, O6, O6, O6, O6, O6, O6, O6,
	    O6, O6, O6, S6, S6, O6, O6, O6,
	    O6, O6, S6, S6, S6, S6, O6, O6,
	    O6, O6, S6, S6, S6, S6, O6, O6,
	    B6, B6, B6, B6, B6, B6, B6, B6,
	    B6, B6, B6, B6, B6, B6, B6, B6,
	]
	,
	[
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, S7, S7, O7, O7, O7,
	    O7, O7, S7, S7, S7, S7, O7, O7,
	    B7, B7, B7, B7, B7, B7, B7, B7,
	    B7, B7, B7, B7, B7, B7, B7, B7,
	]
	,
	[
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, S7, S7, O7, O7, O7,
	    B8, B8, B8, B8, B8, B8, B8, B8,
	    B8, B8, B8, B8, B8, B8, B8, B8,
	]
	,
	[
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    O7, O7, O7, O7, O7, O7, O7, O7,
	    B9, B9, B9, B9, B9, B9, B9, B9,
	    B9, B9, B9, B9, B9, B9, B9, B9,
	]
	]   
	for i in range(2):
	  for image in soleilcouchant:
	    s.set_pixels(image)
	    time.sleep(0.8)
	    




#############################################################
def debut():

	White = (255, 255,255)
	Black = (0, 0, 0)

	W = White
	B = Black

	Start = [
	[ 
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  B, B, B, W, W, W, B, B,
	  B, B, B, B, B, W, B, B,
	  B, B, B, W, W, W, B, B,
	  B, B, B, B, B, W, B, B,
	  B, B, B, W, W, W, B, B,
	  B, B, B, B, B, B, B, B,
	  ]
	,

	[ 
	  B, B, B, B, B, B, B, B, 
	  B, B, B, B, B, B, B, B,
	  B, B, B, W, W, W, B, B,
	  B, B, B, B, B, W, B, B,
	  B, B, B, W, W, W, B, B,
	  B, B, B, W, B, B, B, B,
	  B, B, B, W, W, W, B, B, 
	  B, B, B, B, B, B, B, B,
	  ]
	,

	[ 
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, W, B, B, B,
	  B, B, B, W, W, B, B, B,
	  B, B, W, B, W, B, B, B,
	  B, B, B, B, W, B, B, B,
	  B, B, B, B, W, B, B, B,
	  B, B, W, W, W, W, B, B,
	  B, B, B, B, B, B, B, B,
	  ]
	]  

	for i in Start:
	  s.set_pixels(i)
	  time.sleep(1)

#############################################################
def fin():

	F = (133, 76, 6)
	Y = (195, 195, 12)
	S = (255, 255, 0)
	R = (242, 7, 34)
	W = (255,255,255)
	O = (0,0,0)
	G = (8,182, 8)
	B = (0,51,204)

	dessins1=[
	    O, O, B, B, B, B, O, O,
	    O, O, B, B, B, B, O, O,
	    O, O, B, B, O, O, O, O,
	    O, O, B, B, B, B, O, O,
	    O, O, B, B, B, B, O, O,
	    O, O, B, B, O, O, O, O,
	    O, O, B, B, O, O, O, O,
	    O, O, B, B, O, O, O, O,
	    ]

	dessins2=[
	    O, O, O, B, B, O, O, O,
	    O, O, O, B, B, O, O, O,
	    O, O, O, O, O, O, O, O,
	    O, O, O, B, B, O, O, O,
	    O, O, O, B, B, O, O, O,
	    O, O, O, B, B, O, O, O,
	    O, O, O, B, B, O, O, O,
	    O, O, O, B, B, O, O, O,
	    ]

	dessins3=[
	    B, B, O, O, O, O, B, B,
	    B, B, B, O, O, O, B, B,
	    B, B, B, B, O, O, B, B,
	    B, B, B, B, B, O, B, B,
	    B, B, O, B, B, B, B, B,
	    B, B, O, O, B, B, B, B,
	    B, B, O, O, O, B, B, B,
	    B, B, O, O, O, O, B, B,
	    ]

	delai=1 
	s.set_pixels(dessins1)
	time.sleep(delai)
	s.set_pixels(dessins2)
	time.sleep(delai)
	s.set_pixels(dessins3)
	time.sleep(delai)













#####################################################################
def end():

	nothing = (0,0,0)
	white = (255,255,255)
	green = (0,255,0)
	orange = (255,100,0)
	blue = (0,100,255)
	grey = (55,55,55)
	blue2 = (0,0,25)
	b2 = blue2
	g2 = grey
	b = blue
	w = white
	o2 = orange
	o = nothing
	g = green

	zz = [
	  b, b, b, b, b, b2, o, o,
	  b2, b2, b2, b, b2, o, o, o,
	  o, o, b, b2, o, o, o, o,
	  o, b, b2, o, o, b, b, b,
	  b, b, b, b, b2, o, b, b2,
	  b2, b2, b2, b2, b2, b, b2, o,
	  o, o, o, o, b, b, b, b,
	  o, o, b, o, b2, b2, b2, b2,
	  ]
	  

	fin = [ 
	  [
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	  ]
	,
	 [
	   o, w, w, w, w, w, w, o,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   o, w, w, w, w, w, w, o,
	  ]
	  ,
	 [
	   o, o, w, w, w, w, o, o,
	   o, w, w, w, w, w, w, o,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   o, w, w, w, w, w, w, o,
	   o, o, w, w, w, w, o, o,
	  ]
	  ,
	 [
	   o, o, o, w, w, o, o, o,
	   o, o, w, w, w, w, o, o,
	   o, w, w, w, w, w, w, o,
	   w, w, w, w, w, w, w, w,
	   w, w, w, w, w, w, w, w,
	   o, w, w, w, w, w, w, o,
	   o, o, w, w, w, w, o, o,
	   o, o, o, w, w, o, o, o,
	  ]
	  ,
	 [
	   o, o, o, o, o, o, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, w, w, w, w, o, o,
	   o, w, w, w, w, w, w, o,
	   o, w, w, w, w, w, w, o,
	   o, o, w, w, w, w, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	  ]
	  ,
	  [
	   o, o, o, o, o, o, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, w, w, o, o, o,
	   o, w, w, w, w, w, w, o,
	   o, w, w, w, w, w, w, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	  ]
	  ,
	  [
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, w, w, w, w, w, w, o,
	   o, o, o, o, w, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	  ]
	  ,
	  [
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, w, w, w, w, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	  ]
	  ,
	  [
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, o, w, w, w, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	  ]
	  ,
	  [
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	  ]
	  ,
	  [
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	  ]
	]
	  
	 

	s.set_pixels(zz)
	time.sleep(3)
	  
	for i in fin :
	  s.set_pixels(i)
	  time.sleep(0.001)











#################################################################
def attenteBouclePair():
	green = (0, 255, 0)
	yellow = (255, 255, 0)
	blue = (0, 0, 255)
	red = (255, 0, 0)
	white = (255,255,255)
	nothing = (0,0,0)
	W = white
	G = green
	B = yellow
	Y = blue
	N = nothing

	iss_logo = [
	 Y , Y , N , N , N , N , Y , Y,
	 Y , Y , N , N , N , N , Y , Y,
	 Y , Y , N , W , W , N , Y , Y,
	 W , W , W , W , W , W , W , W,
	 Y , Y , N , W , W , N , Y , Y,
	 Y , Y , N , N , N , N , Y , Y,
	 Y , Y , N , G , N , N , Y , Y,
	 N , N , N , N , N , N , N , N
	]
	s.set_pixels(iss_logo)

def attenteBoucleImpair():
	green = (0, 255, 0)
	yellow = (255, 255, 0)
	blue = (0, 0, 255)
	red = (255, 0, 0)
	white = (255,255,255)
	nothing = (0,0,0)
	W = white
	G = green
	B = yellow
	Y = blue
	N = nothing

	iss_logo = [
	 Y , Y , N , N , N , N , Y , Y,
	 Y , Y , N , N , N , N , Y , Y,
	 Y , Y , N , W , W , N , Y , Y,
	 W , W , W , W , W , W , W , W,
	 Y , Y , N , W , W , N , Y , Y,
	 Y , Y , N , N , N , N , Y , Y,
	 Y , Y , N , N , G , N , Y , Y,
	 N , N , N , N , N , N , N , N
	]
	s.set_pixels(iss_logo)


##################################################################
# anim lever du soleil
def leverSoleil1():

	O = (254, 174, 107)
	Y = (248, 230, 122)
	B = (34, 37, 64)
	W = (251, 251, 253)
	M = (229,128, 116)
	N = (252,225, 242)
	P = (235,127, 105)
	V = (252,213, 17)
	Bl = (14,20, 208)
	b = (26,149, 230)


	lever=[
	[
	M, M, M, M, M, M, M, M,
	M, M, O, O, O, O, M, M,
	O, O, O, O, O, O, O, Y,
	O, O, O, P, P, O, O, O,
	P, P, P, N, W, P, P, P,
	P, P, P, W, N, P, P, P,
	B, Bl, B, P, P, B, Bl, B,
	B, Bl, B, B, B, Bl, B, Bl,
	]
	,
	[
	M, M, M, M, M, M, M, M,
	O, O, O, O, O, O, O, O,
	Y, O, O, P, P, M, O, O,
	O, O, P, W, N, P, M, M,
	P, P, N, N, W, W, P, P,
	P, P, N, W, N, N, P, P,
	B, Bl, P, P, P, P, B, Bl,
	Bl, Bl, B, Bl, B, B, Bl, Bl,
	]
	,
	[
	M, M, M, M, M, M, M, M,
	O, O, P, P, P, P, O, O,
	O, P, P, N, N, P, P, O,
	P, P, N, W, W, N, P, P,
	P, P, N, W, W, N, P, P,
	P, P, P, N, N, P, P, P,
	Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
	Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
	]
	,
	[
	b, b, b, b, b, b, b, b,
	b, b, b, W, W, b, b, b,
	b, b, W, N, N, W, b, b,
	b, b, N, W, W, N, b, b,
	b, b, b, W, W, b, b, b,
	b, b, b, b, b, b, b, b,
	Bl, Bl, Bl, Y, Y, Bl, Bl, Bl,
	Bl, Bl, Y, Y, Y, Y, Bl, Bl,
	]
	,
	[
	b, b, b, W, W, b, b, b,
	b, b, W, W, W, W, b, b,
	b, b, W, N, N, W, b, b,
	b, b, b, W, W, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	Bl, Bl, Bl, Y, Y, Bl, Bl, Bl,
	Bl, Bl, Y, Y, Y, Y, Bl, Bl,
	]
	,
	[
	b, b, W, W, W, W, b, b,
	b, b, W, W, W, W, b, b,
	b, b, b, N, N, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	Bl, Bl, Bl, Y, Y, Bl, Bl, Bl,
	Bl, Bl, Y, Y, Y, Y, Bl, Bl,
	]
	,
	[
	b, b, W, W, W, W, b, b,
	b, b, b, W, W, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	Bl, Bl, Bl, Y, Y, Bl, Bl, Bl,
	Bl, Bl, Y, Y, Y, Y, Bl, Bl,
	]
	,
	[
	b, b, b, W, W, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
	Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
	]
	,
	[
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
	Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
	]
	,
	[
	N, N, N, b, b, b, b, b,
	N, N, b, b, b, N, N, b,
	N, b, b, b, N, N, N, N,
	b, b, b, b, b, N, N, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
	Bl, Bl, Bl, Bl, Bl, Bl, Bl, Bl,
	]

	]

	for i in range(2):
		for image in lever:
	  		s.set_pixels(image)
	  		time.sleep(0.7)
  	time.sleep(1)
  	s.clear()
##########################################################
# anim coq

def coqFrance():
	white = (255,255,255)
	nothing = (0,0,0)
	red = (255,0,0)
	blue = (0,0,255)
	brown2 = (120,65,0)
	b2 = brown2
	b = blue
	w = white
	o = nothing
	r = red

	coqFR = [
	 o, r, r, o, o, o, o, o, 
	 o, o, r, r, o, o, o, o,
	 b, b, b, r, o, o, r, r,
	 o, b, b, w, w, w, r, r,
	 o, o, b, w, w, w, r, o,
	 o, o, o, w, w, w, o, o,
	 o, o, o, o, b2, o, o, o,
	 o, o, o, b2, b2, o, o, o,
	]
	  
	for i  in range(3):
		s.set_pixels(coqFR)
		time.sleep(1)
		s.clear()
		time.sleep(0.4)
############################################################
# anim coeur

def coeurItalie():

	green = (0,255,0)
	white = (255,255,255)
	red = (255,0,0)
	nothing = (0,0,0)
	g = green
	w = white
	r = red
	o = nothing 

	italy = [
	o, o, o, o, o, o, o, o,
	g, g, w, w, w, w, r, r,
	g, g, w, w, w, w, r, r,
	g, g, w, w, w, w, r, r,
	g, g, w, w, w, w, r, r,
	g, g, w, w, w, w, r, r,
	g, g, w, w, w, w, r, r,
	o, o, o, o, o, o, o, o,
	]


	s.set_pixels(italy)
	time.sleep(2)





	rose = (255,0,205)
	rose2 = (175,30,145)
	white = (255,255,255)
	nothing = (0,0,0)
	r = rose
	r2 = rose2
	w = white
	o = nothing

	heart = [
	  [
	  o, o, o, o, o, o, o, o,
	  o, o, r, o, r, o, o, o,
	  o, r, w, r, r, r, o, o,
	  o, r, r, r, r, r2, o, o,
	  o, o, r, r, r2, o, o, o,
	  o, o, o, r2, o, o, o, o,
	  o, o, o, o, o, o, o, o,
	  o, o, o, o, o, o, o, o,
	  ]
	,
	[
	  o, o, o, o, o, o, o, o,
	  o, r, r, o, r, r, o, o,
	  r, r, w, r, r, r, r, o,
	  r, w, r, r, r, r, r2, o,
	  o, r, r, r, r, r2, o, o,
	  o, o, r, r, r2, o, o, o,
	  o, o, o, r2, o, o, o, o,
	  o, o, o, o, o, o, o, o,
	  ]
	]
	  
	for i in range(3):
		for k in heart:
			s.set_pixels(k)
			time.sleep(0.5)
 	time.sleep(1)
 	s.clear()

#######################################################
# check de fin de calibrage

def finCalibrage():

	nothing = (0,0,0)
	green = (0,255,0)
	orange = (255,100,0)
	o2 = orange
	o = nothing
	g = green

	check = [ 
	  [
	   o2, o2, o2, o2, o2, o2, o2, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o2, o2, o2, o2, o2, o2, o2,
	  ]
	,
	 [
	   o2, o2, o2, o2, o2, o2, o2, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, g, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o2, o2, o2, o2, o2, o2, o2,
	  ]
	  ,
	 [
	   o2, o2, o2, o2, o2, o2, o2, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, g, o, o, o, o, o2,
	   o2, o, o, g, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o2, o2, o2, o2, o2, o2, o2,
	  ]
	  ,
	 [
	   o2, o2, o2, o2, o2, o2, o2, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, g, o, g, o, o, o2,
	   o2, o, o, g, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o2, o2, o2, o2, o2, o2, o2,
	  ]
	  ,
	 [
	   o2, o2, o2, o2, o2, o2, o2, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, g, o, o2,
	   o2, o, g, o, g, o, o, o2,
	   o2, o, o, g, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o2, o2, o2, o2, o2, o2, o2,
	  ]
	  ,
	 [
	   o2, o2, o2, o2, o2, o2, o2, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o, o, o, o, o, g, o2,
	   o2, o, o, o, o, g, o, o2,
	   o2, o, g, o, g, o, o, o2,
	   o2, o, o, g, o, o, o, o2,
	   o2, o, o, o, o, o, o, o2,
	   o2, o2, o2, o2, o2, o2, o2, o2,
	  ]
	  
	]

	  
	for i in check : 
		s.set_pixels(i)
	 	time.sleep(0.3)
 	time.sleep(1)
 	s.clear()

##########################################################
# fusee detection poussee

def detectionPoussee():

	F = (133, 76, 6)
	Y = (195, 195, 12)
	S = (255, 255, 0)
	R = (242, 7, 34)
	W = (255,255,255)
	O = (0,0,0)
	G = (8,182, 8)
	B = (0,51,204)

	dessins=[
	[
	    R, R, R, R, R, R, R, R,
	    R, O, O, W ,W, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, R, R, R, R, R, R, R,
	    ]
	,
	[
	    R, R, R, R, R, R, R, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, R, R, R, R, R, R, R,
	    ]
	,
	[
	    R, R, R, R, R, R, R, R,
	    R, O, O, W ,W, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, R, R, R, R, R, R, R,
	    ]
	,
	[
	    R, R, R, R, R, R, R, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, R, R, R, R, R, R, R,
	    ]
	,
	[
	    R, R, R, R, R, R, R, R,
	    R, O, O, W ,W, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, O, O, O, O, O, O, R,
	    R, O, O, W, W, O, O, R,
	    R, R, R, R, R, R, R, R,
	    ]
	,
	[
	    O, O, O, R, R, O, O, O,
	    S, O, R, W, R, W, O, O,
	    O, O, W, R, W, R, O, S,
	    O, O, R, W, R, W, O, O,
	    O, O, W, R, W, R, O, S,
	    O, O, R, W, R, W, O, O,
	    O, R, Y, Y, Y, Y, R, O,
	    O, R, Y, Y, Y, Y, R, O,
	    ]
	,
	[
	    O, O, O, R, R, O, O, O,
	    O, O, R, W, R, W, O, O,
	    S, O, W, R, W, R, O, O,
	    O, O, R, W, R, W, O, S,
	    O, O, W, R, W, R, O, O,
	    O, O, R, W, R, W, O, S,
	    O, R, Y, Y, Y, Y, R, O,
	    O, R, W, W, W, W, R, O,
	    ]
	,
	[
	    S, O, R, W, R, W, O, O,
	    O, O, W, R, W, R, O, S,
	    O, O, R, W, R, W, O, O,
	    O, O, W, R, W, R, O, S,
	    O, O, R, W, R, W, O, O,
	    O, R, Y, Y, Y, Y, R, O,
	    O, R, Y, Y, Y, Y, R, O,
	    O, O, O, O, O, O, O, Y,
	    ]
	,
	[
	    O, O, R, W, R, W, O, O,
	    O, O, W, R, W, R, O, S,
	    O, O, R, W, R, W, O, O,
	    O, R, Y, Y, Y, Y, R, O,
	    O, R, Y, Y, Y, Y, R, O,
	    O, O, O, O, O, O, O, Y,
	    O, O, Y, O, O, Y, O, O,
	    Y, O, O, O, O, O, Y, O,
	    ]
	,
	[
	    O, O, R, W, R, W, O, O,
	    O, R, Y, Y, Y, Y, R, O,
	    O, R, Y, Y, Y, Y, R, O,
	    O, O, O, O, O, O, O, Y,
	    O, Y, O, O, O, B, B, B,
	    O, O, O, O, G, G, B, B,
	    O, Y, O, O, B, B, G, B,
	    O, O, O, Y, B, B, B, B,
	    ]
	,
	[
	    O, R, Y, Y, Y, Y, R, O,
	    O, O, O, O, O, O, O, O,
	    O, O, O, O, O, O, O, O,
	    O, Y, O, Y, O, B, B, B,
	    O, O, O, O, G, G, B, B,
	    O, Y, O, O, B, B, G, B,
	    O, O, O, Y, B, B, B, B,
	    O, Y, O, O, O, G, B, B,
	    ]
	,
	[
	    O, O, W, W, W, W, O, O,
	    O, O, O, W, W, O, O, Y,
	    O, O, O, O, O, O, O, O,
	    O, Y, O, Y, O, B, B, B,
	    O, O, O, O, G, G, B, B,
	    O, Y, O, O, B, B, G, B,
	    O, O, O, O, B, B, B, B,
	    O, Y, O, O, O, B, G, B,
	    ]
	  ]

	for i in range(1):
		for image in dessins:
	 		s.set_pixels(image)
	    		time.sleep(0.7)
	time.sleep(1)
	s.clear()
	
##################################################
# logo ISS

def logoISS():
	green = (0, 255, 0)
	yellow = (255, 255, 0)
	blue = (0, 0, 255)
	red = (255, 0, 0)
	white = (255,255,255)
	nothing = (0,0,0)
	W = white
	G = green
	B = yellow
	Y = blue
	N = nothing

	iss_logo = [
	 Y , Y , N , N , N , N , Y , Y,
	 Y , Y , N , N , N , N , Y , Y,
	 Y , Y , N , W , W , N , Y , Y,
	 W , W , W , W , W , W , W , W,
	 Y , Y , N , W , W , N , Y , Y,
	 Y , Y , N , N , N , N , Y , Y,
	 Y , Y , N , N , N , N , Y , Y,
	 N , N , N , N , N , N , N , N
	]
	s.set_pixels(iss_logo)
	time.sleep(1)
	s.clear()

#################################################
# detectionHumain()

def detectionHumain():

	Q = (0,0,255)
	F = (255,132,23)
	R = (255,1,1)
	B = (0, 50, 255)
	W = (210,210,210)
	O = (0,0,0)

	dessins=[
	[ 
	   O, O, O, O, O, W, O, O,
	    O, O, O, O, W, O, O, O,
	    O, O, O, W, W, O, O, O,
	    O, Q, Q, W, W, W, W, O,
	    O, Q, Q, W, W, W, W, O,
	    O, Q, Q, W, W, W, W, O,
	    O, Q, Q, W, W, W, W, O,
	    O, O, O, O, O, O, O, O,
	    ]
	,
	[ 
	    O, O, O, O, O, O, O, O,
	    B, O, B, O, B, O, B, O,
	    B, O, B, O, O, O, B, O,
	    B, B, B, O, B, O, B, O,
	    B, B, B, O, B, O, B, O,
	    B, O, B, O, B, O, O, O,
	    B, O, B, O, B, O, B, O,
	    O, O, O, O, O, O, O, O,
	    ]
	  ] 
	for i in range(2):
		for image in dessins:
	    		s.set_pixels(image)
	    		time.sleep(1)
	s.clear()
	
########################################################
# animISS

def mouvementISS():

	F = (133, 76, 6)
	Y = (178, 119, 0)
	B = (4, 188, 197)
	R = (62, 49, 43)
	W = (97,106,107)
	O = (0,0,0)
	G = (8,182, 8)

	dessins=[
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, B, W, B, F, F,
	    B, B, G, W, G, B, B, B,
	    ]
	,
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, W, B, B, F, F,
	    B, G, W, G, B, B, B, B,
	    ]
	,
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, W, B, B, B, F, F,
	    G, W, G, B, B, B, B, B,
	    ]
	,
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, B, B, B, F, F,
	    W, G, B, B, B, B, B, B,
	    ]
	,
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, B, B, B, F, F,
	    G, B, B, B, B, B, B, B,
	    ]
	,
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, B, B, B, F, F,
	    B, B, B, B, B, B, B, G,
	    ]
	,
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, B, B, B, F, F,
	    B, B, B, B, B, B, G, W,
	    ]
	,
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, B, B, B, F, F,
	    B, B, B, B, B, G, W, G,
	    ]
	,
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, B, B, B, F, F,
	    B, B, B, B, G, W, G, B,
	    ]
	,
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, B, B, W, F, F,
	    B, B, B, G, W, G, B, B,
	    ]
	,
	[
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, B, W, B, F, F,
	    B, B, G, W, G, B, B, B,
	    ]
	  ,
	  [
	    R, R, O, O, O, O, R, R,
	    R, R, O, W, W, O, R, R,
	    R, R, O, W, W, O, R, R,
	    W, W, W, W, W, W, W, W,
	    Y, Y, O, W, W, O, Y, Y,
	    Y, Y, O, O, O, O, Y, Y,
	    F, F, B, B, W, B, F, F,
	    B, B, G, W, G, B, B, B,
	    ]
	  ]

	for i in range(2):
		for image in dessins:
			s.set_pixels(image)
	    		time.sleep(0.2)
	s.clear()

#################################################
# roueAttente

def roueAttente():
	
	grey5 = (200,200,200)
	grey4 = (150,150,150)
	grey3 = (100,100,100)
	grey2 = (50,50,50)
	white = (255,255,255)
	grey = (10,10,10)
	nothing = (0,0,0)
	w = white
	g = grey
	o = nothing
	g5 = grey5
	g4 = grey4
	g3 = grey3
	g2 = grey2


	loading_screen = [
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, w, o, o, w, o, o,
	   o, o, w, o, o, w, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, w, o, o, w, o, o,
	   o, o, w, o, o, w, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	   ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g, o, o, o, o,
	   o, o, w, o, o, w, o, o,
	   o, o, w, o, o, w, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	   ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g2, g, o, o, o,
	   o, o, w, o, o, o, o, o,
	   o, o, w, o, o, w, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	   ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g3, g2, o, o, o,
	   o, o, w, o, o, g, o, o,
	   o, o, w, o, o, o, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	   ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g4, g3, o, o, o,
	   o, o, w, o, o, g2, o, o,
	   o, o, w, o, o, g, o, o,
	   o, o, o, w, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	   ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g5, g4, o, o, o,
	   o, o, w, o, o, g3, o, o,
	   o, o, w, o, o, g2, o, o,
	   o, o, o, o, g, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	   ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, w, g5, o, o, o,
	   o, o, w, o, o, g4, o, o,
	   o, o, o, o, o, g3, o, o,
	   o, o, o, g, g2, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	   ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, o, o, g5, o, o,
	   o, o, g, o, o, g4, o, o,
	   o, o, o, g2, g3, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	    ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, w, o, o, o,
	   o, o, g, o, o, w, o, o,
	   o, o, g2, o, o, g5, o, o,
	   o, o, o, g3, g4, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	    ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g, o, o, o, o,
	   o, o, g2, o, o, w, o, o,
	   o, o, g3, o, o, w, o, o,
	   o, o, o, g4, g5, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	    ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g2, g, o, o, o,
	   o, o, g3, o, o, o, o, o,
	   o, o, g4, o, o, w, o, o,
	   o, o, o, g5, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	    ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g3, g2, o, o, o,
	   o, o, g4, o, o, g, o, o,
	   o, o, g5, o, o, o, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	    ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g4, g3, o, o, o,
	   o, o, g5, o, o, g2, o, o,
	   o, o, w, o, o, g, o, o,
	   o, o, o, w, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	    ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g5, g4, o, o, o,
	   o, o, w, o, o, g3, o, o,
	   o, o, w, o, o, g2, o, o,
	   o, o, o, o, g, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	    ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, w, g5, o, o, o,
	   o, o, w, o, o, g4, o, o,
	   o, o, o, o, o, g3, o, o,
	   o, o, o, g, g2, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	    ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, w, o, o, o, o,
	   o, o, o, o, o, g5, o, o,
	   o, o, g, o, o, g4, o, o,
	   o, o, o, g2, g3, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	    ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, g, o, o, o, o, o,
	   o, o, g2, o, o, g5, o, o,
	   o, o, o, g3, g4, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	   ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g, o, o, o, o,
	   o, o, g2, o, o, o, o, o,
	   o, o, g3, o, o, o, o, o,
	   o, o, o, g4, g5, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	      ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g2, o, o, o, o,
	   o, o, g3, o, o, o, o, o,
	   o, o, g4, o, o, o, o, o,
	   o, o, o, g5, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	      ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g3, o, o, o, o,
	   o, o, g4, o, o, o, o, o,
	   o, o, g5, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	      ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g4, o, o, o, o,
	   o, o, g5, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	      ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, g5, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	   ,
	[
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	   ,
	   [
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, w, o, o, w, o, o,
	   o, o, w, o, o, w, o, o,
	   o, o, o, w, w, o, o, o,
	   o, o, o, o, o, o, o, o,
	   o, o, o, o, o, o, o, o,
	   ]
	]

	for k in loading_screen:
	  s.set_pixels(k)
	  time.sleep(0.1)

##############################################################
# CoucherSoleil

def coucherSoleil():

	orange = (252, 167, 41)
	orangee = (241, 119, 26)
	yellow = (237, 241, 26)
	yelloww = (229, 232, 66)
	purple = (182, 40, 213)
	blue = (58, 172, 248)
	sun = (255, 255, 0)

	O = orange 
	R = orangee 
	J = yellow 
	A = yelloww
	V = purple
	B = blue
	S = sun

	Sunset = [
	[
	  B, B, B, S, S, B, B, B,
	  B, B, S, S, S, S, B, B,
	  V, V, S, S, S, S, V, V,
	  A, A, A, S, S, A, A, A,
	  A, A, A, A, A, A, A, A,
	  J, J, J, J, J, J, J, J,
	  R, R, R, R, R, R, R, R,
	  O, O, O, O, O, O, O, O,
	  ]
	,

	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, S, S, B, B, B,
	  V, V, S, S, S, S, V, V,
	  A, A, S, S, S, S, A, A,
	  A, A, A, S, S, A, A, A,
	  J, J, J, J, J, J, J, J,
	  R, R, R, R, R, R, R, R,
	  O, O, O, O, O, O, O, O,
	  ]
	,

	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  V, V, V, S, S, V, V, V,
	  A, A, S, S, S, S, A, A,
	  A, A, S, S, S, S, A, A,
	  J, J, J, S, S, J, J, J,
	  R, R, R, R, R, R, R, R,
	  O, O, O, O, O, O, O, O,
	  ]
	,

	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  V, V, V, V, V, V, V, V,
	  A, A, S, S, S, S, A, A,
	  A, S, S, S, S, S, S, A,
	  J, S, S, S, S, S, S, J,
	  R, S, S, S, S, S, S, R,
	  O, O, S, S, S, S, O, O,
	  ]
	,

	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  V, V, V, V, V, V, V, V,
	  A, A, A, A, A, A, A, A,
	  A, A, S, S, S, S, A, A,
	  J, S, S, S, S, S, S, J,
	  R, S, S, S, S, S, S, R,
	  O, S, S, S, S, S, S, O,
	  ]
	,

	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  V, V, V, V, V, V, V, V,
	  A, A, A, A, A, A, A, A,
	  A, A, A, A, A, A, A, A,
	  J, J, S, S, S, S, J, J,
	  R, S, S, S, S, S, S, R,
	  O, S, S, S, S, S, S, O,
	  ]
	]  


	for i in Sunset:
		s.set_pixels(i)
	 	time.sleep(1)
	s.clear()
	
#############################################################
# leverSoleil2

def leverSoleil2():

	orange = (255, 103, 37)
	orangee = (255, 90, 40)
	yellow = (255, 164, 58)
	yelloww = (255, 169, 82)
	purple = (170, 134, 255)
	blue = (100, 102, 255)
	sun = (255, 195, 0)

	O = orange 
	R = orangee 
	J = yellow 
	A = yelloww
	V = purple
	B = blue
	S = sun


	Sunrise = [
	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  V, V, V, V, V, V, V, V,
	  A, A, A, A, A, A, A, A,
	  A, A, A, A, A, A, A, A,
	  J, J, S, S, S, S, J, J,
	  R, S, S, S, S, S, S, R,
	  O, S, S, S, S, S, S, O,
	  ]
	,

	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  V, V, V, V, V, V, V, V,
	  A, A, A, A, A, A, A, A,
	  A, A, S, S, S, S, A, A,
	  J, S, S, S, S, S, S, J,
	  R, S, S, S, S, S, S, R,
	  O, S, S, S, S, S, S, O,
	  ]
	,

	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  V, V, V, V, V, V, V, V,
	  A, A, S, S, S, S, A, A,
	  A, S, S, S, S, S, S, A,
	  J, S, S, S, S, S, S, J,
	  R, S, S, S, S, S, S, R,
	  O, O, S, S, S, S, O, O,
	  ]
	,

	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  V, V, V, S, S, V, V, V,
	  A, A, S, S, S, S, A, A,
	  A, A, S, S, S, S, A, A,
	  J, J, J, S, S, J, J, J,
	  R, R, R, R, R, R, R, R,
	  O, O, O, O, O, O, O, O,
	  ]
	,

	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, S, S, B, B, B,
	  V, V, S, S, S, S, V, V,
	  A, A, S, S, S, S, A, A,
	  A, A, A, S, S, A, A, A,
	  J, J, J, J, J, J, J, J,
	  R, R, R, R, R, R, R, R,
	  O, O, O, O, O, O, O, O,
	  ]
	,

	[
	  B, B, B, S, S, B, B, B,
	  B, B, S, S, S, S, B, B,
	  V, V, S, S, S, S, V, V,
	  A, A, A, S, S, A, A, A,
	  A, A, A, A, A, A, A, A,
	  J, J, J, J, J, J, J, J,
	  R, R, R, R, R, R, R, R,
	  O, O, O, O, O, O, O, O,
	  ] 
	,

	[
	  B, B, S, S, S, S, B, B,
	  B, B, S, S, S, S, B, B,
	  V, V, V, S, S, V, V, V,
	  A, A, A, A, A, A, A, A,
	  A, A, A, A, A, A, A, A,
	  J, J, J, J, J, J, J, J,
	  R, R, R, R, R, R, R, R,
	  O, O, O, O, O, O, O, O,
	  ]

	,

	[
	  B, B, S, S, S, S, B, B,
	  B, B, B, S, S, B, B, B,
	  V, V, V, V, V, V, V, V,
	  A, A, A, A, A, A, A, A,
	  A, A, A, A, A, A, A, A,
	  J, J, J, J, J, J, J, J,
	  R, R, R, R, R, R, R, R,
	  O, O, O, O, O, O, O, O,
	  ]
	,

	[
	  B, B, B, S, S, B, B, B,
	  B, B, B, B, B, B, B, B,
	  V, V, V, V, V, V, V, V,
	  A, A, A, A, A, A, A, A,
	  A, A, A, A, A, A, A, A,
	  J, J, J, J, J, J, J, J,
	  R, R, R, R, R, R, R, R,
	  O, O, O, O, O, O, O, O,
	  ]
	,

	[
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  V, V, V, V, V, V, V, V,
	  A, A, A, A, A, A, A, A,
	  A, A, A, A, A, A, A, A,
	  J, J, J, J, J, J, J, J,
	  R, R, R, R, R, R, R, R,
	  O, O, O, O, O, O, O, O,
	  ]
	]
	for i in Sunrise:
	  s.set_pixels(i)
	  time.sleep(1)
	  
#####################################################
# code de test des anniversaires de l'equipage

def testAnniversaires():
	
	W = (255,255,255)
	B = (0,0,255)
	R = (255,0,0)
	N = (0,0,0)

	russia = [
	  N, N, N, N, N, N, N, N,
	  W, W, W, W, W, W, W, W,
	  W, W, W, W, W, W, W, W,
	  B, B, B, B, B, B, B, B,
	  B, B, B, B, B, B, B, B,
	  R, R, R, R, R, R, R, R,
	  R, R, R, R, R, R, R, R,
	  N, N, N, N, N, N, N, N,
	  ]

	blue = (0,0,255)
	white = (255,255,255)
	red = (255,0,0)
	nothing = (0,0,0)
	b = blue
	w = white
	r = red
	o = nothing 

	french = [
	o, o, o, o, o, o, o, o,
	b, b, w, w, w, w, r, r,
	b, b, w, w, w, w, r, r,
	b, b, w, w, w, w, r, r,
	b, b, w, w, w, w, r, r,
	b, b, w, w, w, w, r, r,
	b, b, w, w, w, w, r, r, 
	o, o, o, o, o, o, o, o,
	]

	blue = (0,0,255)
	white = (255,255,255) 
	red = (255,0,0)
	nothing = (0,0,0)
	b = blue
	w = white 
	r = red 
	o = nothing 


	us = [
	o, o, o, o, o, o, o, o,
	o, o, o, o, o, o, o, o,
	b, b, b, r, r, r, r, r,
	b, b, b, w, w, w, w, w, 
	b, b, b, r, r, r, r, r, 
	w, w, w, w, w, w, w, w,
	r, r, r, r, r, r, r, r, 
	o, o, o, o, o, o, o, o,
	]


	date_anniv_Thomas="27/02"
	date_anniv_Peggy="09/02"
	date_anniv_Oleg="12/10"
	date_anniv_Robert="04/06"
	date_anniv_Serguei="19/08"
	date_anniv_Andrei="17/04"
	date_du_jour=time.strftime("%d/%m")




	if date_du_jour==date_anniv_Thomas :
	  s.show_message("Happy", text_colour=[0, 0, 255])
	  s.show_message("Birthday", text_colour=[255, 0, 0])
	  s.show_message("Thomas !", text_colour=[255, 255, 255])
	  s.set_pixels(french)
	  
	if date_du_jour==date_anniv_Peggy :
	  s.show_message("Happy", text_colour=[0, 0, 255])
	  s.show_message("Birthday", text_colour=[255, 0, 0])
	  s.show_message("Peggy !", text_colour=[255, 255, 255])
	  s.set_pixels(us)
	  
	if date_du_jour==date_anniv_Oleg :
	  s.show_message("Happy", text_colour=[0, 0, 255])
	  s.show_message("Birthday", text_colour=[255, 0, 0])
	  s.show_message("Oleg !", text_colour=[255, 255, 255])
	  s.set_pixels(russia)
	  
	if date_du_jour==date_anniv_Robert :
	  s.show_message("Happy", text_colour=[0, 0, 255])
	  s.show_message("Birthday", text_colour=[255, 0, 0])
	  s.show_message("Robert !", text_colour=[255, 255, 255])
	  s.set_pixels(us)
	  
	if date_du_jour==date_anniv_Serguei  :
	  s.show_message("Happy", text_colour=[0, 0, 255])
	  s.show_message("Birthday", text_colour=[255, 0, 0])
	  s.show_message("Serguei !", text_colour=[255, 255, 255])
	  s.set_pixels(russia)
	   
	if date_du_jour==date_anniv_Andrei  :
	  s.show_message("Happy", text_colour=[0, 0, 255])
	  s.show_message("Birthday", text_colour=[255, 0, 0])
	  s.show_message("Andrei !", text_colour=[255, 255, 255])
	  s.set_pixels(russia)
	 
	time.sleep(3)
	s.clear()
	
###################################################	
def nyancat():

	orange = (255, 102, 0)
	galaxie = (0, 38, 77)
	rouge = (255, 0, 0)
	jaune = (255, 255, 0)
	vert = (0, 255, 0)
	bleu = (0, 51, 204)
	violet = (153, 51, 255)
	chat = (171, 178, 185)
	toast = (234, 231, 145)
	yeux = (28, 40, 51)
	etoile = (191, 191, 191)
	rose = (241, 148, 138)

	O = orange
	G = galaxie
	R = rouge
	J = jaune
	V = vert
	B = bleu
	Z = violet
	C = chat
	T = toast
	Y = yeux
	E = etoile
	P = rose

	cat= [
	[
	  G, G, G, G, G, G, G, G,
	  G, R, R, G, R, R, G, R,
	  R, O, O, R, O, O, R, O,
	  O, J, J, O, J, J, O, J,
	  J, V, V, J, V, V, J, V,
	  V, B, B, V, B, B, V, B,
	  B, Z, Z, B, Z, Z, B, Z,
	  Z, G, G, Z, G, G, Z, G,
	  ]
	,

	[
	  G, G, G, G, G, G, G, G,
	  R, R, G, R, R, G, R, R,
	  O, O, R, O, O, R, O, O,
	  J, J, O, J, J, O, J, J,
	  V, V, J, V, V, J, V, V,
	  B, B, V, B, B, V, B, B,
	  Z, Z, B, Z, Z, B, Z, Z,
	  G, G, Z, G, G, Z, G, G,
	  ]
	,

	[
	  R, G, G, G, G, G, G, G,
	  O, R, G, G, G, G, G, G,
	  C, O, P, T, P, C, G, C,
	  C, C, T, P, T, Y, C, Y,
	  J, V, P, T, P, C, Y, C,
	  V, B, C, C, G, C, G, C,
	  B, Z, G, G, G, G, G, G,
	  Z, G, G, G, G, G, G, G,
	  ]
	]
	for i in cat:
	  s.set_pixels(i)
	  time.sleep(1)	
#################################################################
#anims calibrage	  
def calib0():
	N=(0,0,0)
	O=(10,10,200)
	dessin=[
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  O, O, O, O, O, O, O, O,
	  O, N, N, N, N, N, N, O,
	  O, O, O, O, O, O, O, O,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  ]
	s.set_pixels(dessin)	

def calib1():
	N=(0,0,0)
	O=(10,10,200)
	G=(210,180,10)
	dessin=[
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  O, O, O, O, O, O, O, O,
	  O, G, N, N, N, N, N, O,
	  O, O, O, O, O, O, O, O,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  ]
	s.set_pixels(dessin)	
	

def calib2():
	N=(0,0,0)
	O=(10,10,200)
	G=(210,180,10)
	dessin=[
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  O, O, O, O, O, O, O, O,
	  O, G, G, N, N, N, N, O,
	  O, O, O, O, O, O, O, O,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  ]
	s.set_pixels(dessin)	  

def calib3():
	N=(0,0,0)
	O=(10,10,200)
	G=(210,180,10)
	dessin=[
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  O, O, O, O, O, O, O, O,
	  O, G, G, G, N, N, N, O,
	  O, O, O, O, O, O, O, O,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  ]
	s.set_pixels(dessin)	
	

def calib4():
	N=(0,0,0)
	O=(10,10,200)
	G=(210,180,10)
	dessin=[
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  O, O, O, O, O, O, O, O,
	  O, G, G, G, G, N, N, O,
	  O, O, O, O, O, O, O, O,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  ]
	s.set_pixels(dessin)
	
def calib5():
	N=(0,0,0)
	O=(10,10,200)
	G=(210,180,10)
	dessin=[
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  O, O, O, O, O, O, O, O,
	  O, G, G, G, G, G, N, O,
	  O, O, O, O, O, O, O, O,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  ]
	s.set_pixels(dessin)

def calib6():
	N=(0,0,0)
	O=(10,10,200)
	G=(210,180,10)
	dessin=[
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  O, O, O, O, O, O, O, O,
	  O, G, G, G, G, G, G, O,
	  O, O, O, O, O, O, O, O,
	  N, N, N, N, N, N, N, N,
	  N, N, N, N, N, N, N, N,
	  ]
	s.set_pixels(dessin)
