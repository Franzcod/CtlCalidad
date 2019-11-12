
#CONTROL DE CALIDAD DE PROBUSOL

# a revisar:

#  si es conveniente Sqlite o MysqL
# el uso remoto en una red (usar desde varias pc) PUEDE SER CON DROPBOX
# crear el ejecutable


from tkinter import*
from tkinter import messagebox   #se importa para crear ventanas emergentes
from tkinter import filedialog
import sqlite3
from datetime import *
from tkinter import ttk 
import time



root=Tk()
now=datetime.now()

root.title("Control de Calidad                 -"+(now.strftime("%A %d de %b del %Y -")))
root.geometry("900x785")
root.iconbitmap("hoja.ico")

"""
Scrollbar=Scrollbar(root, command=root.yview)
scroll.grid(row=1, column=2, pady=0, padx=0, sticky="nsew")
root.config(yscrollcommand=scrollVertical.set)
"""


#_________________________________FUNCIONES__________________________________________________________

#-----------------FUNCION DE BOTON CREAR BBDD---------------------

def conexionBBDD():
	miConexion=sqlite3.connect("BBDD_Control_Calidad")
	miCursor=miConexion.cursor()

	try:
		miCursor.execute('''
			CREATE TABLE CONTROL_CALIDAD (
			ID_CONTROL_N° INTEGER PRIMARY KEY AUTOINCREMENT,     
			NOMBRE_PROD VARCHAR(50),
			PRESENTACION INTEGER(50), 
			N°_LOTE VARCHAR (50) UNIQUE,
			CANTIDAD INTEGER (50),   
			COD_PROD INTEGER (50),
			ASPECTO VARCHAR (50),
			COLOR VARCHAR (50),
			FRAGANCIA VARCHAR (50), 
			pH INTEGER (50), 
			DENSIDAD INTEGER (50),
			VISCOSIDAD INTEGER (50), 
			INDICE_RF INTEGER (50), 
			NO_VOLATILES INTEGER (50),
			OBSERVACIONESS VARCHAR (50))
			''')
		messagebox.showinfo("BBDD", "Se ha creado una BBDD con exito")
	except:
		messagebox.showwarning("Atencion!","La base de datos BBDD_Control_Calidad ya existe")

#----------------FUNCION PARA SALIR DE LA APP--------------------------

def salirApp():
	valor=messagebox.askquestion("salir","¿Desea salir de la aplicacion?")
	if valor=="yes":
		root.destroy()

#---------------FUNCION PARA VACIAR CAMPOS-----------------------------

def vaciarCampos():
	valor=messagebox.askquestion("Borrar","¿Desea vaciar todos los campos?")
	if valor=="yes":
		textAspecto.set("")
		textColor.set("")
		textFragancia.set("")
		textPh.set("")
		textDensidad.set("")
		textViscosidad.set("")
		textRf.set("")
		textVolatiles.set("")

		textNControl.set("")
		textProd.set("")
		textPresentacion.set("")
		textLote.set("")
		textCantidad.set("")
		textCod.set("")
		cuadroObservaciones.delete(1.0,END)

		aspecto.set(False)    #esto vacia los CheckButton
		color.set(False)
		fragancia.set(False)
		ph.set(False)	
		densidad.set(False)
		viscosidad.set(False)
		indiceRf.set(False)
		volatiles.set(False)

#------------ FUNCION PARA AGREGAR CONTENIDO A LA BBDD-----------------

def crear():  # en el video 65 del curso se muestra otra forma mas facil de escribir esto
	try:
		miConexion=sqlite3.connect("BBDD_Control_Calidad")
		miCursor=miConexion.cursor()
		miCursor.execute("INSERT INTO CONTROL_CALIDAD VALUES(NULL, '" +  textProd.get()+
			"','"+ textPresentacion.get()+			
			"','"+ textLote.get()+
			"','"+ textCantidad.get()+
			"','"+ textCod.get()+
			"','"+ textAspecto.get()+
			"','"+ textColor.get()+
			"','"+ textFragancia.get()+
			"','"+ textPh.get()+
			"','"+ textDensidad.get()+
			"','"+ textViscosidad.get()+
			"','"+ textRf.get()+
			"','"+ textVolatiles.get()+
			"','"+ cuadroObservaciones.get("1.0",END)+"')")
		miConexion.commit()
		messagebox.showinfo("BBDD", "Registro creado con exito")
	except sqlite3.IntegrityError:
		messagebox.showwarning("Atencion!","Ya existe un registro con ese Lote")


#-----------------FUNCION DE BOTON "LEER"------------------------------

def leer():
	miConexion=sqlite3.connect("BBDD_Control_Calidad")
	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM CONTROL_CALIDAD WHERE ID_CONTROL_N°=" + textNControl.get())
	#miCursor.execute("SELECT * FROM CONTROL_CALIDAD WHERE N°_LOTE=" + textLote.get())

	elUsuario=miCursor.fetchall()

	for usuario in elUsuario:
		textNControl.set(usuario[0])
		textProd.set(usuario[1])
		textPresentacion.set(usuario[2])
		textLote.set(usuario[3])
		textCantidad.set(usuario[4])
		textCod.set(usuario[5])

		textAspecto.set(usuario[6])
		textColor.set(usuario[7])
		textFragancia.set(usuario[8])
		textPh.set(usuario[9])
		textDensidad.set(usuario[10])
		textViscosidad.set(usuario[11])
		textRf.set(usuario[12])
		textVolatiles.set(usuario[13])


		aspecto.set(True)    #esto vacia los CheckButton
		color.set(True)
		fragancia.set(True)
		ph.set(True)	
		densidad.set(True)
		viscosidad.set(True)
		indiceRf.set(True)
		volatiles.set(True)

		cuadroObservaciones.delete(1.0,END)
		cuadroObservaciones.insert(1.0,usuario[14])
		
	miConexion.commit()

#-------------FUNCION PARA BOTON ACTUALIZAR----------------------------

def actualizar():
	miConexion=sqlite3.connect("BBDD_Control_Calidad")
	miCursor=miConexion.cursor()
	miCursor.execute("UPDATE CONTROL_CALIDAD SET  NOMBRE_PROD='" +  textProd.get()+
		"',PRESENTACION='"+ textPresentacion.get()+
		"',N°_LOTE='"+ textLote.get()+
		"',CANTIDAD='"+ textCantidad.get()+
		"',COD_PROD='"+ textCod.get()+
		"',ASPECTO='"+ textAspecto.get()+
		"',COLOR='"+ textColor.get()+
		"',FRAGANCIA='"+ textFragancia.get()+
		"',pH='"+ textPh.get()+
		"',DENSIDAD='"+ textDensidad.get()+
		"',VISCOSIDAD='"+ textViscosidad.get()+
		"',INDICE_RF='"+ textRf.get()+
		"',NO_VOLATILES='"+ textVolatiles.get()+
		"',OBSERVACIONESS='"+ cuadroObservaciones.get("1.0",END)+
		"' WHERE ID_CONTROL_N°="+ textNControl.get())

	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro actualizado con exito")

#-------------FUNCION PARA ELIMIAR DE BBDD-----------------------------

def eliminar():
	valor=messagebox.askquestion("Borrar","¿Esta seguro de eliminar este control de calidad?")
	if valor=="yes":
		miConexion=sqlite3.connect("BBDD_Control_Calidad")
		miCursor=miConexion.cursor()

		miCursor.execute("DELETE FROM CONTROL_CALIDAD WHERE ID_CONTROL_N°=" + textNControl.get())

		miConexion.commit()
		messagebox.showinfo("Eliminar", "Registro borrado con exito")

#--------FUNCIONES DE BOTON AYUDA DE MENU------------

def licencia():
	messagebox.showwarning("Licencia","¿  ?")

def contactos():
	messagebox.showinfo("Contactos: ", "Correo: palacios.francisco@outlook.com \nTel: 11-26579344")

def acercaDe():
	messagebox.showinfo("Acerca de...", "Aplicacion ideada para guardar la informacion resultante de los controles de calidad a los productos elaborados en el laboratorio de Probusol.\n\nTambien se pueden leer, editar y eliminar registros antiguos de una manera mas facil, rapida y con una interfaz grafica mas amigable para el usuario")

#------------------------------------
textNControl=StringVar()
textProd=StringVar()
textPresentacion=StringVar()
textLote=StringVar()
textCantidad=StringVar()
textCod=StringVar()

textAspecto=StringVar()
textColor=StringVar()
textFragancia=StringVar()
textPh=StringVar()
textDensidad=StringVar()
textViscosidad=StringVar()
textRf=StringVar()
textVolatiles=StringVar()

cuadroObservaciones=StringVar()

#-----------------------------------

aspecto=IntVar()
color=IntVar()
fragancia=IntVar()
ph=IntVar()	
densidad=IntVar()
viscosidad=IntVar()
indiceRf=IntVar()
volatiles=IntVar()

#----------------------------------
#FUNCION PARA QUE APARESCAN CUANDO SE TILDA EL CHECKbUTTON
"""
def aprobado():
	analisisAprobado=""

	if (aspecto.get()==1):
		analisisAprobado+=" Aspecto Aprobado : "+textAspecto.get() 
	if (color.get()==1):
		analisisAprobado+=" \nColor Aprobado : "+textColor.get()
	if (fragancia.get()==1):
		analisisAprobado+=" \nFragancia Aprobado : "+textFragancia.get()
	if (ph.get()==1):
		analisisAprobado+=" \npH Aprobado : "+textPh.get()
	if (densidad.get()==1):
		analisisAprobado+=" \nDensidad Aprobado : "+textDensidad.get()
	if (viscosidad.get()==1):
		analisisAprobado+=" \nViscosidad Aprobado : "+textViscosidad.get()
	if (indiceRf.get()==1):
		analisisAprobado+=" \nIndise Rf Aprobado : "+textRf.get()
	if (volatiles.get()==1):
		analisisAprobado+=" \nVolatiles Aprobado : "+textVolatiles.get()

	aprobados.config(text=analisisAprobado)
"""

#------------FUNCION PARA QUE APARESCA palabra "APROBADO" SI ESTAN TODOS OK


def aprobado():
	analisisAprobado=""

	if (aspecto.get()==1) and (color.get()==1) and (fragancia.get()==1) and (ph.get()==1) and (densidad.get()==1) and (viscosidad.get()==1) and (indiceRf.get()==1) and (volatiles.get()==1):
		analisisAprobado+=" APROBADO "
	aprobados.config(text=analisisAprobado) 

def select():
	#cargar un IF por cada producto (si tiene los mismos controles usar OR)
	if cuadroProd.get()=="Limpia Motor Plus":
		
		textAspecto.set("N/A")
		textColor.set("")
		textFragancia.set("N/A")
		textPh.set("")
		textDensidad.set("")
		textViscosidad.set("N/A")
		textRf.set("N/A")
		textVolatiles.set("N/A")

		aspecto.set(True)    
		color.set(False)
		fragancia.set(True)
		ph.set(False)	
		densidad.set(False)
		viscosidad.set(True)
		indiceRf.set(True)
		volatiles.set(True)



# BARRA DE MENU__________________________________________________-

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
#archivoMenu.add_command(label="Nuevo")                       # opciones de pestaña
archivoMenu.add_command(label="Crear BBDD", command=conexionBBDD)
#archivoMenu.add_command(label="Abrir")#, command=abreFichero)                       # opciones de pestaña
#archivoMenu.add_command(label="Guardar")                     # opciones de pestaña
#archivoMenu.add_command(label="Guardar Como...")             # opciones de pestaña
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salirApp)#), command=avisoSalida)                       # opciones de pestaña


archivoEdicion=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
#archivoEdicion.add_command(label="Cortar")                       # opciones de pestaña
#archivoEdicion.add_command(label="Copiar")                     # opciones de pestaña
#archivoEdicion.add_command(label="Pegar")             # opciones de pestaña
#archivoEdicion.add_separator()
archivoEdicion.add_command(label="Vaciar Campos",command=vaciarCampos)
#archivoEdicion.add_command(label="Eliminar")                       # opciones de pestaña


archivoHerramientas=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="CRUD", menu=archivoHerramientas)
archivoHerramientas.add_command(label="Crear", command=crear)
archivoHerramientas.add_command(label="Leer", command=leer)
archivoHerramientas.add_command(label="Actualizar",command=actualizar)
archivoHerramientas.add_separator()
archivoHerramientas.add_command(label="Borrar Registro", command=eliminar )

archivoAyuda=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)#, menu=archivoAyuda)
archivoAyuda.add_command(label="Licencia" , command=licencia)#, command=avisoLicencia)                       # opciones de pestaña
archivoAyuda.add_command(label="Contactos", command=contactos)#), command=infoAdiciona)                     # opciones de pestaña
archivoAyuda.add_command(label="Acerca de...", command=acercaDe)


#  IMAGEN____________________________________________________

foto=PhotoImage(file="probusol2.png")
#Label(root, text="").pack()               #Espacio en blanco
Label(root, image=foto).pack()

# FRAME 1_____________________________________________________

frame1=Frame(root,pady=20)
frame1.pack()

#labelVacio4=Label(frame1, text= "", width=50)
#labelVacio4.grid(row=0, column=1,columnspan=4)      #campo vacio

labelNroControl=Label(frame1, text="Control n°: ",fg="black",font=("Arial Black",8))
labelNroControl.grid(row=1,column=1, sticky="e", pady=6, padx=3)

cuadroNroControl=Entry(frame1,textvariable=textNControl)
cuadroNroControl.grid(row=1,column=2, sticky="e", pady=6, padx=3) 

labelProd=Label(frame1, text="Nombre del Producto: ",fg="black",font=("Arial Black",8))
labelProd.grid(row=2,column=1, sticky="e", pady=6, padx=3) 

#-------------------------------------------------------------------------------------
cuadroProd=ttk.Combobox(frame1,textvariable=textProd)#,values=["Limpia Motor Plus", "Repollo"]
								#	"Limpia Motor Super",
								#	"Lava Autos Siliconado", 
								#	"Lava Autos (Rojo)", 
								#	"Silicona Aero Vainilla", 
								#	"Silicona Aero Frances",
								#	"Silicona Aero Pino"])

cuadroProd["values"]=["Limpia Motor Plus",
						"Lava Autos Siliconado", 
						"Lava Autos (Rojo)", 
						"Silicona Aero Vainilla", 
						"Silicona Aero Frances",
						"Silicona Aero Pino"]

cuadroProd.current(1)
cuadroProd.grid(row=2,column=2, sticky="e", pady=6, padx=3)
#-------------------------------------------------------------------------------------
botonOk=Button(frame1, text="»", width=3, command=select)#, command=lambda:numeroPulsado("7"))
botonOk.grid(row=2, column=3, pady=1, padx=1)

#  cuadroProd=Entry(frame1,textvariable=textProd)
#  cuadroProd.grid(row=2,column=2, sticky="e", pady=6, padx=3)

labelPresentacion=Label(frame1, text="Presentacion: ",fg="black",font=("Arial Black",8))
labelPresentacion.grid(row=3,column=1, sticky="e", pady=6, padx=3) 

cuadroPresentacion=Entry(frame1,textvariable=textPresentacion)
cuadroPresentacion.grid(row=3,column=2)

labelLote=Label(frame1, text="Numero de Lote: ",fg="black",font=("Arial Black",8))
labelLote.grid(row=1,column=4, sticky="e", pady=6, padx=3) 

cuadroLote=Entry(frame1,textvariable=textLote)
cuadroLote.grid(row=1,column=5, sticky="e", pady=6, padx=3)

labelCantidad=Label(frame1, text="Cantidad: ",fg="black",font=("Arial Black",8))
labelCantidad.grid(row=2,column=4, sticky="e", pady=6, padx=3)

cuadroCantidad=Entry(frame1,textvariable=textCantidad)
cuadroCantidad.grid(row=2,column=5, sticky="e", pady=6, padx=3)

labelCod=Label(frame1, text="Codigo del Producto: ",fg="black",font=("Arial Black",8))
labelCod.grid(row=3,column=4, sticky="e", pady=6, padx=3) 

cuadroCod=Entry(frame1,textvariable=textCod)
cuadroCod.grid(row=3,column=5)



# FRAME 2_____________

frame2=LabelFrame(root,text="Regitro de controles")#,width=400, height=300)
frame2.pack()
#frame2.config(bg="blue")


#labelVacio1=Label(frame2, text= "", width=50)
#labelVacio1.grid(row=1, column=1,columnspan=3)                    #Espacio en blanco


#titulo "controles"

#labelTitulo1=Label(frame2, text= "Controles:",fg="black",font=("Arial Black",8), width=50)
#labelTitulo1.grid(row=2, column=1, columnspan=3)
"""
labelVacio2=Label(frame2, text= "", width=50)
labelVacio2.grid(row=3, column=1,columnspan=3)                   #Espacio en blanco
"""
labelAspecto=Label(frame2, text="Aspecto: ")
labelAspecto.grid(row=4 ,column=1 )
cuadroAspecto=Entry(frame2, textvariable=textAspecto)
cuadroAspecto.grid(row=4, column=2)#, sticky="w", pady=3, padx=0)
check5=Checkbutton(frame2, text="Analisis de Aspecto", variable=aspecto, onvalue=1, offvalue=0, command=aprobado)
check5.grid(row=4, column=3,  pady=0, padx=0)

labelColor=Label(frame2, text="Color: ")
labelColor.grid(row=5 ,column=1 )
cuadroColor=Entry(frame2, textvariable=textColor)
cuadroColor.grid(row=5, column=2)
check3=Checkbutton(frame2, text="Analisis de Color ", variable=color, onvalue=1, offvalue=0, command=aprobado)
check3.grid(row=5, column=3)

labelFragancia=Label(frame2, text="Fragancia: ")
labelFragancia.grid(row=6 ,column=1 )
cuadroFragancia=Entry(frame2, textvariable=textFragancia)
cuadroFragancia.grid(row=6, column=2)
check6=Checkbutton(frame2, text="Analisis de Fragancia ", variable=fragancia, onvalue=1, offvalue=0, command=aprobado)
check6.grid(row=6, column=3)

labelPh=Label(frame2, text="pH: ")
labelPh.grid(row=7 ,column=1 )
cuadroPh=Entry(frame2, textvariable=textPh)
cuadroPh.grid(row=7, column=2)#, sticky="w", pady=3, padx=0)
check1=Checkbutton(frame2, text="Analisis de pH", variable=ph, onvalue=1, offvalue=0, command=aprobado)
check1.grid(row=7, column=3,  pady=0, padx=0)


labelDensidad=Label(frame2, text="Densidad: ")
labelDensidad.grid(row=8 ,column=1 )
cuadroDensidad=Entry(frame2, textvariable=textDensidad)
cuadroDensidad.grid(row=8, column=2)#
check2=Checkbutton(frame2, text="Analisis de Densidad", variable=densidad, onvalue=1, offvalue=0, command=aprobado)
check2.grid(row=8, column=3)

labelViscosidad=Label(frame2, text="Viscosidad: ")
labelViscosidad.grid(row=9 ,column=1 )
cuadroViscosidad=Entry(frame2, textvariable=textViscosidad)
cuadroViscosidad.grid(row=9, column=2)
check7=Checkbutton(frame2, text="Analisis de Viscosidad ", variable=viscosidad, onvalue=1, offvalue=0, command=aprobado)
check7.grid(row=9, column=3)


labelRf=Label(frame2, text="Indice Rf: ")
labelRf.grid(row=10 ,column=1 )
cuadroAnalisisRf=Entry(frame2, textvariable=textRf)
cuadroAnalisisRf.grid(row=10, column=2)
check3=Checkbutton(frame2, text="Analisis de Indice Rf ", variable=indiceRf, onvalue=1, offvalue=0, command=aprobado)
check3.grid(row=10, column=3)

labelVolatiles=Label(frame2, text="No Volatiles: ")
labelVolatiles.grid(row=11 ,column=1 )
cuadroVolatiles=Entry(frame2, textvariable=textVolatiles)
cuadroVolatiles.grid(row=11, column=2)
check8=Checkbutton(frame2, text="Analisis de No Volatiles ", variable=volatiles, onvalue=1, offvalue=0, command=aprobado)
check8.grid(row=11, column=3)




# FRAME 3_____________

frame3=Frame(root,width=400, height=500)
#frame3.pack(fill='x', expand=1)
frame3.pack()

linea=Label(frame3, text= "_______________________________________________________________________", width=50)
linea.grid(row=0, column=1, columnspan=3)



aprobados=Label(frame3, fg="green",font=("Arial Black",20))
aprobados.grid(row=1,column=1, columnspan=3)



linea=Label(frame3, text= "_______________________________________________________________________", width=50)
linea.grid(row=2, column=1, columnspan=3)


labelObservaciones=Label(frame3, text="Observaciones: ",fg="black",font=("Arial Black",8))
labelObservaciones.grid(row=4,column=1, sticky="e", pady=3, padx=3)
#labelComentario.config(bg="black")

cuadroObservaciones=Text(frame3, width=35, height=5)# ,textvariable=textObservaciones)
cuadroObservaciones.grid(row=4, column=2,pady=0, padx=0)
cuadroObservaciones.insert(INSERT, "Elaborador:  \nContenedor: \n\n"+ now.strftime("%d de %b del %Y -") )
cuadroObservaciones.config(fg="Black")

scrollVertical=Scrollbar(frame3, command=cuadroObservaciones.yview)   #barra de desplazamiento
scrollVertical.grid(row=4, column=3, pady=0, padx=0, sticky="nsew")
cuadroObservaciones.config(yscrollcommand=scrollVertical.set)



#frame 4____________

frame4=Frame(root)
frame4.pack()

labelVacio1=Label(frame4, text= "", width=50)      #espacio vacio
labelVacio1.grid(row=1, column=1,columnspan=5)

botonCrear=Button(frame4, text="Crear", width=9, command=crear)#, command=lambda:numeroPulsado("7"))
botonCrear.grid(row=2, column=2, pady=1, padx=1)

botonLeer=Button(frame4, text="Leer", width=9, command=leer)#, command=lambda:numeroPulsado("7"))
botonLeer.grid(row=2, column=3, pady=1, padx=1)

botonActualizar=Button(frame4, text="Actualizar", width=9, command=actualizar)#, command=lambda:numeroPulsado("7"))
botonActualizar.grid(row=2, column=4, pady=1, padx=1)

botonEliminar=Button(frame4, text="Eliminar", width=9, command=eliminar)#, command=lambda:numeroPulsado("7"))
botonEliminar.bind("Control-a")
botonEliminar.grid(row=2, column=5, pady=1, padx=1)













root.mainloop()
