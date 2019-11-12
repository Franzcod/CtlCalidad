from tkinter import *
from tkinter.ttk import *


scr = Tk()
scr.title("Cuadro txt desplegable")
scr.geometry('500x500')



def select():
	value = "Producto: " + combo.get()
	label.config(text = value)
	texto1=""


	if combo.get()=="Limpia Motor Super":
		
		texto1+="Prod 1"

		check5=Checkbutton(scr, text="Analisis de Aspecto")
		check5.grid(row=4, column=2,  pady=0, padx=0)

		check5=Checkbutton(scr, text="Analisis de Color")
		check5.grid(row=5, column=2,  pady=0, padx=0)

		check5=Checkbutton(scr, text="Analisis de Fragancia")
		check5.grid(row=6
			, column=2,  pady=0, padx=0)


	if combo.get()=="Limpia Motor Plus":
		texto1+="Prod 1"

	if combo.get()=="Lava Autos Siliconado":
		texto1+="Prod 2"


	#label2.config(text=texto1)     #Texto: Prod1
	

combo = Combobox(scr, values=[ "Limpia Motor Plus", 
								"Limpia Motor Super",
								"Lava Autos Siliconado", 
								"Lava Autos (Rojo)", 
								"Silicona Aero Vainilla", 
								"Silicona Aero Frances",
								"Silicona Aero Pino"])
combo.current(0)
combo.grid(row=1,column=2)



labeltitulo = Label(scr,text="Productos")
labeltitulo.grid(row=0,column=1)

button = Button(scr, text=",/", command=select,width=3)
button.grid(row=1,column=4)


label = Label(scr)
label.grid(row=2,column=2)


label2=Label(scr)
label2.grid(row=3,column=2)


scr.mainloop()