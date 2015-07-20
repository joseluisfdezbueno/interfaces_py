#!/usr/python
# -*- coding: utf-8 -*-

import MySQLdb
from gi.repository import Gtk

class interfaz():
	def __init__(self):
		# Iniciamos GTK
		self.builder = Gtk.Builder()
		# Leemos nuestro diseño hecho en glade
		self.builder.add_from_file("diseño.glade")
		# Asociamos eventos a señales
		
		self.handlers = {"onDeleteWindow": self.onDeleteWindow,
						"on_btn_clicked": self.on_btn_clicked,
						"onCloseAbout": self.onCloseAbout,
						"on_acercaDe_clicked": self.on_acercaDe_clicked,
						}
        
        # Conectamos las señales
		self.builder.connect_signals(self)
		# Obtenemos los objetos de la interfaz
		self.window = self.builder.get_object("window")
		self.button = self.builder.get_object("button")
		self.about = self.builder.get_object("aboutdialog")
		self.combo = self.builder.get_object("combobox")
		self.entry1 = self.builder.get_object("entry1")
		self.entry2 = self.builder.get_object("entry2")
		self.entry3 = self.builder.get_object("entry3")
		self.entry4 = self.builder.get_object("entry4")
		self.entry5 = self.builder.get_object("entry5")
		self.entry6 = self.builder.get_object("entry6")
		
		# Mostramos los objetos de la interfaz
		self.window.show_all()
		# Redimensionamos la pantalla
		self.window.resize(500,500)	

	# Definimos las funciones de los manejadores	
	def onDeleteWindow(self, *args):
		# Cerramos las conexiones
		micursor.close()
		Conexion.close()
		Gtk.main_quit(*args)
		
	def on_acercaDe_clicked(self, window):
		self.about.show()
		
	def onCloseAbout(self,window,data=None):
		self.about.hide()
	
	'''			
	def limpiar_entradas(self, *args):
		self.entry1.set_text('')
		self.entry2.set_text('')
		self.entry3.set_text('')
		self.entry4.set_text('')
		self.entry5.set_text('')
		self.entry6.set_text('')						
	'''
	
	def on_btn_clicked(self, window):
		self.entry7 = self.builder.get_object("entry7")
		entrada = self.entry7.get_text()
		print entrada
		model = self.combo.get_model()
		activo = self.combo.get_active()
		if activo == 0: #crear
			# insertamos un nuevo elemento
			query= "INSERT INTO planetas (nombre, superficie, gravedad, temperatura_media, lunas, anillos) VALUES ('%s', %d, %d, %d, %i, %i);"\
			 % (self.entry1.get_text(), float(self.entry2.get_text()), float(self.entry3.get_text()), float(self.entry4.get_text()), \
			int(self.entry5.get_text()), int(self.entry6.get_text()))
			micursor.execute(query)
			Conexion.commit()
		elif activo == 1 and entrada!="":  #obtener
			# Realizamos la selección					
			query= "SELECT * FROM planetas WHERE id= %i;" % int(entrada)
			micursor.execute(query)
			Conexion.commit()
			# obtenemos el registro y rellenamos los 'text entry'
			registro = micursor.fetchall()
			self.entry1.set_text(registro[0]["nombre"])
			self.entry2.set_text(str(registro[0]["superficie"]))
			self.entry3.set_text(str(registro[0]["gravedad"]))
			self.entry4.set_text(str(registro[0]["temperatura_media"]))
			self.entry5.set_text(str(registro[0]["lunas"]))
			self.entry6.set_text(str(registro[0]["anillos"]))
		elif activo == 2 and entrada!="":  #actualizar
			# Realizamos la actualización					
			query= "UPDATE planetas SET nombre= '%s', superficie= %d, gravedad= %d, temperatura_media= %d,\
			lunas= %i , anillos= %i WHERE id=%i;" % (self.entry1.get_text(), float(self.entry2.get_text()), float(self.entry3.get_text()), float(self.entry4.get_text()), \
			int(self.entry5.get_text()), int(self.entry6.get_text()), int(entrada))
			micursor.execute(query)
			Conexion.commit()			
		elif activo == 3 and entrada!="":  #borrar
			# Realizamos el borrado					
			query= "DELETE FROM planetas WHERE id= %i;" % int(entrada)
			micursor.execute(query)
			Conexion.commit()

def main():		
	# Creamos la tabla e insertamos algunos planetas
	query = "CREATE TABLE planetas(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255) NOT NULL, superficie DOUBLE, gravedad DOUBLE, temperatura_media DOUBLE, lunas INT, anillos INT)"
	micursor.execute(query)
	# Insertamos un par de planetas a modo de ejemplo
	query = "INSERT INTO planetas (nombre, superficie, gravedad, temperatura_media, lunas, anillos) VALUES ('Mercurio', 75000000, 2.8, 166.85, 0, 0);"
	micursor.execute(query)
	query = "INSERT INTO planetas (nombre, superficie, gravedad, temperatura_media, lunas, anillos) \
    VALUES ('Tierra', 510000000, 9.81, 14.85, 1, 0);"
	micursor.execute(query)
	
	# Ejecutamos las inserciones		
	Conexion.commit()
    		
	# Instanciamos la clase interfaz
	window = interfaz()
	
	# Delegamos en GTK
	Gtk.main()

# Establecemos la conexión
Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
# Creamos el cursor, pero especificando que sea de la subclase DictCursor
micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)

# Ejecutamos el programa
main()
