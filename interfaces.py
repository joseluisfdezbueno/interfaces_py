#!/usr/python
# -*- coding: utf-8 -*-

import MySQLdb
from gi.repository import Gtk

class interfaz:
	def __init__(self):
		# Iniciamos GTK
		self.builder = Gtk.Builder()
		# Leemos nuestro diseño hecho en glade
		self.builder.add_from_file("diseño.glade")
		# Asociamos eventos a señales
		self.handlers = {"onDeleteWindow": Gtk.main_quit,
						"onButtonPressed": self.onButtonPressed,
						"onCircuitActivate": self.onCircuitActivate,
						"onAboutDialog": self.onAboutDialog,
						"onCloseAbout": self.onCloseAbout,}
        
        # Conectamos las señales
		self.builder.connect_signals(self.handlers)
		# Obtenemos los objetos de la interfaz
		self.window = self.builder.get_object("window")
		self.button1 = self.builder.get_object("button1")
		self.about = self.builder.get_object("aboutdialog")
		
		# Mostramos los objetos de la interfaz
		self.window.show_all()
		# Redimensionamos la pantalla
		self.window.resize(500,500)	

		# Definimos las funciones de los manejadores
	
	

def main():
	# Establecemos la conexión
	Conexion = MySQLdb.connect(host='localhost', user='conan',passwd='crom', db='DBdeConan')
	
	# Creamos el cursor, pero especificando que sea de la subclase DictCursor
	micursor = Conexion.cursor(MySQLdb.cursors.DictCursor)
	
	# Creamos la tabla
	consulta = "CREATE TABLE planetas( \
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, \
    nombre VARCHAR(255) NOT NULL, \
    superficie(km^2) DOUBLE, \
    gravedad(m/s^2) DOUBLE, \
    temperatura_media(Cº) DOUBLE, \
    lunas INT,  \
    anillos INT \
    )"
    		
	# Instanciamos la clase interfaz
	window = interfaz()
	
	# Delegamos en GTK
	Gtk.main()


# Ejecutamos el programa
main();
