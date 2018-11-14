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
	print (file.read())
	texto=file.read()
	colores={"a":"#ffff00","c":"#00ffff","d":"#ffc90e","m":"#800080","r":"#ff0000","v":"#00bb00"}
	#Codigo ejemplo para crear un rectangulo
	c.create_rectangle(0,0,20,20,fill="#ff0000",outline="")

	c.pack()
	c.mainloop()
	
