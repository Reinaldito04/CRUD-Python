import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QMessageBox,QLabel
from PyQt5.QtCore import QPoint,Qt,QByteArray,QIODevice,QBuffer,QRect,Qt
import sqlite3
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage,QPixmap,QIntValidator,QMovie
from PyQt5.QtCore import QSize
from PyQt5.QtCore import QTimer

class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen , self). __init__()
        loadUi("./login.ui", self)
        self.loginboton.clicked.connect(self.gui_login)
        self.registroboton.clicked.connect(self.gui_register)
        self.bt_salir.clicked.connect(self.close_application)
        self.passwordboton.clicked.connect(self.gui_password)
        self.bt_kirby.clicked.connect(self.gui_kirby)
    
        
        # Crear la animación de carga
        self.loading_movie = QMovie("./capibara.gif")
        self.loading_movie.setScaledSize(QSize(100, 100))
        # Crear la etiqueta para mostrar la animación
        self.loading_label = QLabel(self.Gif)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setFixedSize(100, 100)
         # Crear temporizador para ocultar la animación después de 2 segundos
        self.loading_timer = QTimer()
        self.loading_timer.setInterval(3500)
        self.loading_timer.timeout.connect(self.hide_loading)
    
    def gui_kirby(self):
        kirby = Kirby_access()
        widget.addWidget(kirby)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(800)
        
    def close_application(self):
        QApplication.quit()
   
        
    def gui_login(self):
        name = self.user.text()
        password = self.password.text()
        
        if not name or not password:  # Verificar si los campos están vacíos
            QMessageBox.warning(self, "Error", "Por favor ingrese usuario y contraseña.")
            return
        
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE user = ? AND password = ?', (name, password))
        resultado = cursor.fetchone()

        
        conexion.close()
        if resultado is not None :
            self.show_loading()
            self.loading_timer.start()  # Iniciar el temporizador
        
        else:
            QMessageBox.warning(self, "Error", "Nombre de usuario o contraseña incorrectos.")

    def window_access(self):
        ventana_2 = Menu_access()
        widget.addWidget(ventana_2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(800)
        
    def gui_register(self):
        ventana_3 = Registro_access()
        widget.addWidget(ventana_3)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(450)
        widget.setFixedWidth(500)
    def show_loading(self):
        self.loginboton.setEnabled(False)
        self.loading_label.setMovie(self.loading_movie)
        self.loading_movie.start()
        self.loading_label.show()
    def hide_loading(self):
        self.loading_movie.stop()
        self.loading_label.hide()
        self.loginboton.setEnabled(True)
        self.loading_timer.stop()  # Detener el temporizador
        QMessageBox.information(self, "login", "Entrando... ")
        self.window_access()
        
        
    def gui_password(self):
        ventana_4 = Password_access()
        widget.addWidget(ventana_4)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(450)
        widget.setFixedWidth(500)
        
class Menu_access(QMainWindow):
    def __init__(self):
        super(Menu_access,self).__init__()
        loadUi("./menu.ui",self)
        self.bt_salir.clicked.connect(self.close_application)
        self.bt_becas.clicked.connect(self.becas_gui)
        self.bt_volver.clicked.connect(self.volver)
        self.bt_estudiantes.clicked.connect(self.estudiantes)
    def estudiantes(self):
        crud = Estudiantes_access()
        widget.addWidget(crud)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(800)
    def volver(self):
        login = WelcomeScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(800)  
        
    def close_application(self):
        QApplication.quit()
    
    def becas_gui(self):
        becas = Becas_access()
        widget.addWidget(becas)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(600)
        widget.setFixedWidth(900)
        
class Estudiantes_access(QMainWindow):
    def __init__(self):
        super(Estudiantes_access,self).__init__()
        loadUi("./CRUD.ui",self)
        self.bt_salir.clicked.connect(self.close_application)
        self.bt_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_database))
        self.bt_registrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_register))
        self.bt_foto.clicked.connect(self.img)
        self.bt_load.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_reload))
        self.bt_eliminar.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_buscar))
        self.bt_guardar.clicked.connect(self.load_data)
        self.bt_busqueda.clicked.connect(self.buscar)
        self.bt_refrescar.clicked.connect(self.mostrardatos)
        self.bt_volver.clicked.connect(self.volver)
        self.bt_delete.clicked.connect(self.delete)
        self.bt_buscar.clicked.connect(self.busqueda)
        self.bt_city.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_city))
        self.bt_buscarcity.clicked.connect(self.city)
        self.bt_img.clicked.connect(self.imagen)
        self.bt_actualizar.clicked.connect(self.actualizar)
         # Crear la animación de carga
        self.loading_movie = QMovie("carga.gif")
        self.loading_movie.setScaledSize(QSize(100, 100))
        self.loading_movie1 = QMovie("carga.gif")
        self.loading_movie1.setScaledSize(QSize(100, 100))
        # Crear la etiqueta para mostrar la animación
        self.loading_label = QLabel(self.Gif)
        self.loading_label1 = QLabel(self.Gif_2)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setFixedSize(100, 100)
        self.loading_label1.setAlignment(Qt.AlignCenter)
        self.loading_label1.setFixedSize(100, 100)
         # Crear temporizador para ocultar la animación después de 2 segundos
        self.loading_timer = QTimer()
        self.loading_timer.setInterval(2000)
        self.loading_timer.timeout.connect(self.hide_loading)
        self.loading_timer2 = QTimer()
        self.loading_timer2.setInterval(2000)
        self.loading_timer2.timeout.connect(self.hide_loading_2)
       
    def show_loading(self):
        self.bt_busqueda.setEnabled(False)
        self.loading_label.setMovie(self.loading_movie)
        self.loading_movie.start()
        self.id.hide()
        self.cedula.hide()
        self.genero.hide()
        self.carrera.hide()
        self.ciudad.hide()
        self.foto.hide()
        self.loading_timer.start()

    def hide_loading(self):
        self.bt_busqueda.setEnabled(True)
        self.loading_movie.stop()
        self.loading_label.setMovie(None)
        self.id.show()
        self.cedula.show()
        self.genero.show()
        self.carrera.show()
        self.ciudad.show()
        self.foto.show()
    def hide_loading_2(self):
        self.bt_buscar.setEnabled(True)
        self.loading_movie1.stop()
        self.loading_label1.setMovie(None)
        self.ID.show()
        self.Cedula.show()
        self.Genero.show()
        self.Carrera.show()
        self.Ciudad.show()
        self.label_imagen.show()
    def show_loading_2(self):
        self.bt_buscar.setEnabled(False)
        self.loading_label1.setMovie(self.loading_movie1)
        self.loading_movie1.start()
        self.ID.hide()
        self.Cedula.hide()
        self.Genero.hide()
        self.Carrera.hide()
        self.Ciudad.hide()
        self.label_imagen.hide()
        self.loading_timer2.start()
        
    def city(self):
        ciudad = self.City.text()
        if not ciudad:
            QMessageBox.warning(self, "Error", "Tienes que ingresar una ciudad para poder realizar la consulta ")
            return
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Alumnos WHERE Ciudad = ?", (ciudad,))
        resultados = cursor.fetchall()
    
        if not resultados:
            QMessageBox.warning(self,"Error","no hay alumnos que viva en esa ciudad")
        else:
            self.tabla_ciudad.setRowCount(len(resultados))
            tablerow = 0
            for row in resultados:
                self.tabla_ciudad.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                self.tabla_ciudad.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.tabla_ciudad.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.tabla_ciudad.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
                self.tabla_ciudad.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
                self.tabla_ciudad.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
                tablerow += 1
        conexion.close()
    
        
    def close_application(self):
        QApplication.quit()
    def img(self):
    # Abrir un diálogo de selección de archivo para que el usuario pueda seleccionar una imagen
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Archivos de imagen (*.png *.jpg *.bmp)")
    
    # Verificar si el usuario seleccionó un archivo y mostrar la imagen en el QLabel
        if filename:
            pixmap = QPixmap(filename)
            self.Img.setPixmap(pixmap)
    def imagen(self):
    # Abrir un diálogo de selección de archivo para que el usuario pueda seleccionar una imagen
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Archivos de imagen (*.png *.jpg *.bmp)")
    
    # Verificar si el usuario seleccionó un archivo y mostrar la imagen en el QLabel
        if filename:
            pixmap = QPixmap(filename)
            self.label_imagen.setPixmap(pixmap)
    def load_data(self):
        identidad = self.ln_id.text()
        nombre= self.ln_nombre.text()
        cedula = self.ln_cedula.text()
        genero = self.ln_genero.text()
        carrera = self.ln_carrera.text()
        ciudad = self.ln_ciudad.text()
        if not identidad:
            QMessageBox.warning(self, "Advertencia", "Debes ingresar el ID antes de guardar")
            return
        if not nombre:
            QMessageBox.warning(self, "Advertencia", "Debes ingresar el nombre para guardar")
            return
        if not cedula:
            QMessageBox.warning(self, "Advertencia", "Debes ingresar su cedula antes de guardar")
            return
        if not genero:
            QMessageBox.warning(self, "Advertencia", "Debes ingresar su genero antes de guardar")
            return
        if not carrera:
            QMessageBox.warning(self, "Advertencia", "Debes ingresar su carrera antes de guardar")
            return
        if not ciudad:
            QMessageBox.warning(self, "Advertencia", "Debes ingresar su ciudad antes de guardar")
            return
        
        foto_pixmap  = self.Img.pixmap()
        
        if foto_pixmap is None:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una imagen antes de guardar los datos")
            return
        
        
        # Convertir la imagen en un objeto de bytes
        foto_image = foto_pixmap.toImage()
       
        buffer = QBuffer()
        buffer.open(QIODevice.WriteOnly)
        foto_image.save(buffer, "PNG")
        foto_bytes = buffer.data()
        buffer.close()
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor() 
        cursor.execute("INSERT INTO Alumnos (ID, Nombre, Cedula, Genero, Carrera, Ciudad, Foto) VALUES (?, ?, ?, ?, ?, ?,?)",
               (identidad, nombre, cedula, genero, carrera, ciudad , foto_bytes))
        alumno = cursor.fetchall()
       
        QMessageBox.information(self, "Exito", "Datos Guardados Correctamente ")
        conexion.commit()
        conexion.close()
        
    def buscar(self):
        nombre = self.Nombre.text()
        if not nombre:
            QMessageBox.warning(self, "Error", "Tienes que ingresar un nombre para poder realizar la consulta ")
            return
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Alumnos WHERE Nombre = ?", (nombre,))
        alumno = cursor.fetchone()
        
        if alumno:  
            self.show_loading()
            self.id.setText(alumno[0])
            self.cedula.setText(alumno[2])
            self.genero.setText(alumno[3])
            self.carrera.setText(alumno[4])
            self.ciudad.setText(alumno[5])
            pixmap = QPixmap()
            pixmap.loadFromData(alumno[6])
            self.foto.setPixmap(pixmap)
            
            
            
        else:
            self.hide_loading()
            QMessageBox.warning(self, "Error", "El alumno no se encuentra en la base de datos")
            
    def mostrardatos(self):
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor() 
        cursor.execute("SELECT ID,Nombre,Cedula,Genero,Carrera,Ciudad FROM Alumnos")
        registro = cursor.fetchall()
        i = len(registro)
        self.tabla_estudiantes.setRowCount(i)
        tablerow = 0
        for row in registro :
            self.Id= row[0]
            self.tabla_estudiantes.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_estudiantes.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_estudiantes.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_estudiantes.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_estudiantes.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            self.tabla_estudiantes.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
            tablerow +=1
            
    def delete(self):
        nombre = self.Nombre.text()
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor() 

        # Mostrar mensaje de confirmación y obtener respuesta del usuario
        respuesta = QMessageBox.question(self, "Confirmar eliminación", "¿Está seguro de que desea eliminar el alumno?",
                                  QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if respuesta == QMessageBox.Yes:
            cursor.execute("DELETE FROM Alumnos WHERE Nombre = ?", (nombre,))
            conexion.commit()
            conexion.close()
            if cursor.rowcount > 0:
                self.id.clear()
                self.cedula.clear()
                self.genero.clear()
                self.carrera.clear()
                self.foto.clear()
                self.Nombre.clear()
                self.ciudad.clear()
                QMessageBox.information(self,"Exito","El alumno fue eliminado correctamente")
            else:
                QMessageBox.warning(self, "Error", "El alumno no se encuentra en la base de datos")
        elif respuesta == QMessageBox.No:
            QMessageBox.information(self, "Waos", "Se canceló la operación")
            return
    def busqueda (self):
        nombre = self.alumno.text()
        if not nombre:
            QMessageBox.warning(self, "Error", "Tienes que ingresar un nombre para poder realizar la consulta ")
            return
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Alumnos WHERE Nombre = ?", (nombre,))
        alumno = cursor.fetchone()
        
        if alumno: 
            self.show_loading_2()
            self.ID.setText(alumno[0])
            self.Cedula.setText(alumno[2])
            self.Genero.setText(alumno[3])
            self.Carrera.setText(alumno[4])
            self.Ciudad.setText(alumno[5])
            pixmap = QPixmap()
            pixmap.loadFromData(alumno[6])
            self.label_imagen.setPixmap(pixmap)
            
        else:
            self.hide_loading_2()
            QMessageBox.warning(self, "Error", "El alumno no se encuentra en la base de datos")
      
    
    def volver(self):
        menu = Menu_access()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(800)  
    def actualizar(self):
        alumno = self.alumno.text()
        identidad = self.ID.text()
        cedula = self.Cedula.text()
        genero = self.Genero.text()
        carrera = self.Carrera.text()
        ciudad = self.Ciudad.text()
        foto_pixmap = self.label_imagen.pixmap()
        if foto_pixmap is None:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una imagen antes de guardar los datos")
            return
    
    # Convertir la imagen en un objeto de bytes
        foto_image = foto_pixmap.toImage()
        buffer = QBuffer()
        buffer.open(QIODevice.WriteOnly)
        foto_image.save(buffer, "PNG")
        foto_bytes = buffer.data()
        buffer.close()
    
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor()

    # Ejecutar una consulta UPDATE en la tabla de alumnos
        cursor.execute("""UPDATE Alumnos SET ID=?, Cedula=?, Genero=?, Carrera=?, Ciudad=?, Foto=? WHERE Nombre=?""",
               (identidad, cedula, genero, carrera, ciudad, foto_bytes, alumno))
    
    # Verificar si se actualizó algún registro
        if cursor.rowcount > 0:
        # Confirmar los cambios en la base de datos
            conexion.commit()
            conexion.close()
            QMessageBox.information(self, "Actualización exitosa", "El registro del alumno ha sido actualizado correctamente.")
        else:
        # No se actualizó ningún registro, no es necesario confirmar cambios
            conexion.close()
            QMessageBox.warning(self, "Error de actualización", "No se pudo actualizar el registro del alumno.")

    
       
        
class Kirby_access(QMainWindow):
    def __init__(self):
        super(Kirby_access, self).__init__()
        loadUi("./pajuo.ui", self)
        self.bt_salir.clicked.connect(self.close_application)
    def close_application(self):
        QApplication.quit()
        
        
class Becas_access(QMainWindow):
    def __init__(self):
        super(Becas_access, self).__init__()
        loadUi("./BECAS.ui", self)
        self.bt_salir.clicked.connect(self.close_application)
        self.buscardatos.clicked.connect(self.gui_datas)
        self.bt_adddata.clicked.connect(self.load_data)
        self.bt_img.clicked.connect(self.img)
        self.bt_clear.clicked.connect(self.limpiar)
        self.bt_volver.clicked.connect(self.volver)
        
    
    def volver(self):
          
        
        menu = Menu_access()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(800)  
       

    
    def limpiar(self):
        alumno = self.alumno.clear()
        nota1 = self.nota1.clear()
        nota2 = self.nota2.clear()
        nota3 = self.nota3.clear()
        promedio = self.promedio.clear()
        foto_pixmap  = self.label_imagen.clear()
    
    def img(self):
    # Abrir un diálogo de selección de archivo para que el usuario pueda seleccionar una imagen
        filename, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Archivos de imagen (*.png *.jpg *.bmp)")
    
    # Verificar si el usuario seleccionó un archivo y mostrar la imagen en el QLabel
        if filename:
            pixmap = QPixmap(filename)
            self.label_imagen.setPixmap(pixmap)
    def load_data(self):
        alumno = self.alumno.text()
        if not alumno:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el nombre del alumno antes de guardar los datos")
            return

        try:
            nota1 = float(self.nota1.text())
            nota2 = float(self.nota2.text())
            nota3 = float(self.nota3.text())
        except ValueError:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar valores numéricos para las notas antes de guardar los datos")
            return
        promedio = ((nota1 + nota2 + nota3) / 3)
        self.promedio.setText(str(promedio))
        
            
        if promedio >=20:
            QMessageBox.information(self, "Promedio", "Descuento del 100% ")
        elif promedio >=18 and promedio <=19:
            QMessageBox.information(self, "Promedio", "Descuento del 50% ")
        elif promedio >=15 and promedio <=17:
            QMessageBox.information(self, "Promedio", "Descuento del 25% ")
        elif promedio >=10:
            QMessageBox.information(self, "Promedio", "No tienes descuento")
        elif promedio <9:
            QMessageBox.information(self, "Promedio", "Reprobó")
       
         
        foto_pixmap  = self.label_imagen.pixmap()
        if foto_pixmap is None:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una imagen antes de guardar los datos")
            return
        
        # Convertir la imagen en un objeto de bytes
        foto_image = foto_pixmap.toImage()
       
        buffer = QBuffer()
        buffer.open(QIODevice.WriteOnly)
        foto_image.save(buffer, "PNG")
        foto_bytes = buffer.data()
        buffer.close()
        
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor() 
        cursor.execute("INSERT INTO Data (Alumno, Nota1, Nota2, Nota3, Promedio, Foto) VALUES (?, ?, ?, ?, ?, ?)",
               (alumno, nota1, nota2, nota3, promedio, foto_bytes))
        QMessageBox.information(self, "Exito", "Datos Guardados Correctamente ")
        conexion.commit()
        conexion.close()
      
     
        
        
    def close_application(self):
        QApplication.quit()
        
    def gui_datas(self):
        ventana_5 = Data_access()
        widget.addWidget(ventana_5)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(560)
        widget.setFixedWidth(600)
        
    
    
class Registro_access(QMainWindow):
    def __init__(self):
        super(Registro_access, self).__init__()
        loadUi("./registro.ui", self)
        self.bt_salir.clicked.connect(self.close_application)
        self.bt_volver.clicked.connect(self.volver)
        self.bt_adduser.clicked.connect(self.add)
        
        
        
    
    def add(self):
        username= self.user.text()
        password =self.password.text()
        passwordRepeat = self.password_repeat.text()
        if not username:
            QMessageBox.warning(self, "Advertencia", "Debes ingresar un usuario para poder guardarlo")
            return
        if not password:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una contraseña para poder guardarla")
            return
        if not passwordRepeat:
            QMessageBox.warning(self,"Error","Debes ingresar su contraseña nuevamente")
            return
        if password != passwordRepeat:
            QMessageBox.warning(self, "Error", "Las contraseñas no son iguales")
            return
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor() 
        cursor.execute("SELECT User FROM Usuarios WHERE User = ?", (username,))
        result = cursor.fetchone()
        
        if result is not None:
            QMessageBox.warning(self,"Alerta","el usuario ya esta registrando en la base de datos \n ,por favor ingrese uno distinto")
            return
        
        cursor.execute("INSERT INTO Usuarios (User, Password) VALUES (?, ?)",
               (username,password))
        QMessageBox.information(self, "Exito", "Registro exitoso ")
        conexion.commit()
        conexion.close()
        
        
    def volver(self):
          
        login = WelcomeScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(800) 
        
    def close_application(self):
        QApplication.quit()
        
class Password_access(QMainWindow):
    def __init__(self):
        super(Password_access, self).__init__()
        loadUi("./password.ui", self)
        self.bt_salir.clicked.connect(self.close_application)
        self.bt_volver.clicked.connect(self.volver)
        self.bt_passwordnew.clicked.connect(self.update_password)
        
    def update_password(self):
        username = self.usuario.text()
        old_password = self.passwordold.text()
        new_password = self.passwordnew.text()
        
        if not username:
            QMessageBox.warning(self, "Error", "Tienes que ingresar un usuario para \n poder cambiar los datos de acceso ")
            return
        if not old_password:
            QMessageBox.warning(self,"Error","Tienes que ingresar la contraseña para poder verificarla")
            return
        if not new_password:
            QMessageBox.warnings("Error","Tienes que ingresar la contraseña nueva para poder guardarla")
            return
        

    
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor()
        
        # Consultar la contraseña actual del usuario en la base de datos
        cursor.execute("SELECT Password FROM Usuarios WHERE User = ?", (username,))
        result = cursor.fetchone()
        if result is None:
            QMessageBox.warning(self, "Error", "El usuario no existe en la base de datos")
            return
        
        # Verificar que la contraseña antigua ingresada por el usuario sea igual a la contraseña actual en la base de datos
        current_password = result[0]
        if old_password != current_password:
            QMessageBox.warning(self, "Error", "La contraseña antigua no es correcta")
            return
        
        # Verificar que la contraseña nueva y antigua sean diferentes
        if old_password == new_password:
            QMessageBox.warning(self, "Error", "La contraseña nueva es igual a la antigua")
            return
        
        # Actualizar la contraseña en la base de datos
        cursor.execute("UPDATE Usuarios SET Password = ? WHERE User = ?", (new_password, username))
        conexion.commit()
        
        QMessageBox.information(self, "Actualización exitosa", "La contraseña se ha actualizado correctamente.")
    
    def volver(self):
          
        
        login = WelcomeScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(800) 
        
    def close_application(self):
        QApplication.quit()
        
class Data_access(QMainWindow):
    def __init__(self):
        super(Data_access, self).__init__()
        loadUi("./busqueda.ui", self)
        self.bt_salir.clicked.connect(self.close_application)
        self.bt_busqueda.clicked.connect(self.buscar_alumno)
        self.bt_volver.clicked.connect(self.volver)
        self.bt_clear.clicked.connect(self.limpiar)
        self.bt_database.clicked.connect(self.database_entrada)
        # Crear la animación de carga
        self.loading_movie = QMovie("carga.gif")
        self.loading_movie.setScaledSize(QSize(100, 100))
        # Crear la etiqueta para mostrar la animación
        self.loading_label = QLabel(self.Gif)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setFixedSize(100, 100)
         # Crear temporizador para ocultar la animación después de 2 segundos
        self.loading_timer = QTimer()
        self.loading_timer.setInterval(2000)
        self.loading_timer.timeout.connect(self.hide_loading)
    def limpiar(self):
        nombre = self.Nombre.clear()
        nota1 = self.nota1.clear()
        nota2 = self.nota2.clear()
        nota3 = self.nota3.clear()
        promedio = self.promedio.clear()
        foto_pixmap  = self.foto.clear()
        
    def database_entrada(self):
        database = Database_access()
        widget.addWidget(database)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(800)
        widget.setFixedWidth(1000) 
        
    def volver(self):
        becas = Becas_access()
        widget.addWidget(becas)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(800) 

    def buscar_alumno(self):
        nombre = self.Nombre.text()
        if not nombre:
            QMessageBox.warning(self, "Error", "Tienes que ingresar un nombre para poder realizar la consulta ")
            return
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Data WHERE Alumno = ?", (nombre,))
        alumno = cursor.fetchone()
        
        if alumno:  
            self.show_loading()
            self.nota1.setText(str(alumno[1]))
            self.nota2.setText(str(alumno[2]))
            self.nota3.setText(str(alumno[3]))
            self.promedio.setText(str(alumno[4]))
            pixmap = QPixmap()
            pixmap.loadFromData(alumno[5])
            self.foto.setPixmap(pixmap)
            
            
        else:
            self.hide_loading()
            QMessageBox.warning(self, "Error", "El alumno no se encuentra en la base de datos")
            
            
    def show_loading(self):
        self.bt_busqueda.setEnabled(False)
        self.loading_label.setMovie(self.loading_movie)
        self.loading_movie.start()
        self.nota1.hide()
        self.nota2.hide()
        self.nota3.hide()
        self.promedio.hide()
        self.foto.hide()
        self.loading_timer.start()

    def hide_loading(self):
        self.bt_busqueda.setEnabled(True)
        self.loading_movie.stop()
        self.loading_label.setMovie(None)
        self.nota1.show()
        self.nota2.show()
        self.nota3.show()
        self.promedio.show()
        self.foto.show()
        
    def close_application(self):
        QApplication.quit()
        
class Database_access(QMainWindow):
    def __init__(self):
        super(Database_access, self).__init__()
        loadUi("./promedios.ui", self)
        self.bt_salir.clicked.connect(self.close_application)
        self.bt_refrescar.clicked.connect(self.notas)
        self.bt_aprobados.clicked.connect(self.aprobados)
        self.bt_datos.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_database))
        self.bt_promedio.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_promedios))   
        self.bt_reprobados.clicked.connect(self.reprobados)
        self.bt_volver.clicked.connect(self.volver)
        
    def volver(self):
          
        busqueda=Data_access ()
        widget.addWidget(busqueda)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(800) 
    
    def close_application(self):
        QApplication.quit()
    def reprobados(self):
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor() 
        cursor.execute("SELECT Alumno,Promedio FROM DATA WHERE CAST(Promedio AS REAL) < 10")
        registro = cursor.fetchall()
        i = len(registro)
        self.tabla_promedios.setRowCount(i)
        tablerow = 0
        for row in registro :
            self.Id= row[0]
            self.tabla_promedios.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_promedios.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            tablerow +=1
    def aprobados(self):
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor() 
        cursor.execute("SELECT Alumno, Promedio FROM DATA WHERE CAST(Promedio AS REAL) >= 10")
        registro = cursor.fetchall()
        i = len(registro)
        self.tabla_promedios.setRowCount(i)
        tablerow = 0
        for row in registro :
            self.Id= row[0]
            self.tabla_promedios.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_promedios.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            tablerow +=1
    def notas(self):
        conexion = sqlite3.connect('./database.db')
        cursor = conexion.cursor() 
        cursor.execute("SELECT Alumno,Nota1,Nota2,Nota3,Promedio FROM DATA")
        
        registro = cursor.fetchall()
        i = len(registro)
        self.tabla_notas.setRowCount(i)
        tablerow = 0
        for row in registro :
            self.Id= row[0]
            self.tabla_notas.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tabla_notas.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tabla_notas.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tabla_notas.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.tabla_notas.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            tablerow +=1
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.move(400, 80)
widget.setFixedHeight(500)
widget.setFixedWidth(500)
widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("saliendo")
    
    