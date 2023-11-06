import numpy as np
import cv2
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, \
    QToolBar, QMenuBar, QFileDialog, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QKeySequence, QAction, QPixmap


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi ventana")
        # etiqueta = QLabel("Otro texto")
        # etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.setCentralWidget(etiqueta)

        boton_abrir = QAction(QIcon('images/animal.png'), "Abrir", self)
        boton_abrir.setToolTip("Abrir archivo")
        boton_abrir.triggered.connect(self.botonAbrirClic)
        #Crear atajo de teclado
        boton_abrir.setShortcut(QKeySequence('Ctrl+a'))

        toolbar = QToolBar("Mi toolbar")
        self.addToolBar(toolbar)
        toolbar.addAction(boton_abrir)

        #Crear menuBar
        barra_menu = QMenuBar()
        menu_archivo = barra_menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_abrir)

        layout = QVBoxLayout()
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        boton_x = QPushButton("Filtro X")
        boton_x.clicked.connect(self.botonFiltroX)
        boton_y = QPushButton("Filtro Y")
        boton_y.clicked.connect(self.botonFiltroY)

        layout.addWidget(boton_x)
        layout.addWidget(boton_y)
        
        self.pixmap = QPixmap()
        self.setMenuBar(barra_menu)

    def botonAbrirClic(self, s):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        self.file_name = fname[0]
        print(fname, self.file_name)

        #cuando se seleccione una imagen
        if self.file_name:
            img = cv2.imread(self.file_name)

            
            # sheared_img = cv2.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))

            # cv2.imshow('original', img)
            # cv2.imshow('sesgada',  sheared_img)
            # cv2.waitKey(0)

            # #poner la Imagen?
            # label = QLabel(self)
            # self.pixmap = QPixmap(self.file_name)
            # label.setPixmap(self.pixmap)
            # self.setCentralWidget(label)

    def botonFiltroX(self):
        if self.file_name:
            img = cv2.imread(self.file_name)
            rows, cols, dim = img.shape
            
            # transformation matrix for shearing
            # shearing applied to x-axis

            M = np.float32([[1, 0.5, 0],
                            [0, 1  , 0],
                            [0, 0  , 1]])
            
            sheared_img = cv2.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))

            cv2.imshow('original', img)
            cv2.imshow('sesgada',  sheared_img)
            cv2.waitKey(0)

    def botonFiltroY(self):
        if self.file_name:
            img = cv2.imread(self.file_name)
            rows, cols, dim = img.shape
            
            # transformation matrix for shearing
            # shearing applied to x-axis

            M = np.float32([[1  , 0, 0],
                            [0.5, 1, 0],
                            [0  , 0, 1]])
            
            sheared_img = cv2.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))

            cv2.imshow('original', img)
            cv2.imshow('sesgada',  sheared_img)
            cv2.waitKey(0)
             

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()

app.exec()



#Errores, se tiene que definir con el self en la funcion principal.
