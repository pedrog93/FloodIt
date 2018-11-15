import tkinter as tk
import sys

root=tk.Tk()
c=tk.Canvas(root,width=280,height=280)

fname =sys.argv[1]
file = open(fname,"r")

#CODIFICA AQUI
if len(sys.argv)==1 :
	print("Favor de proporcionar el txt con codigo de colores")

else:
	#print (file.read())
	texto=file.read()
	colores={"a":"#ffff00","c":"#00ffff","d":"#ffc90e","m":"#800080","r":"#ff0000","v":"#00bb00"}
	dic='acdmrv'
	x0=0
	x1=20
	y0=0
	y1=20
	for i in texto:
		if i in colores.keys():
			#print(colores[i])
			c.create_rectangle(x0,y0,x1,y1,fill=colores[i],outline="")
			x0+=20
			x1+=20
			#print(x0,x1)
		else:
		 	if "\n" in texto:
		 		x0=0
		 		x1=20
		 		y0+=20
		 		y1+=20
	#Codigo ejemplo para crear un rectangulo
	
c.pack(side= 'left')
c.mainloop()
	
