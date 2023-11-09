import numpy as np
import cv2
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, \
    QToolBar, QMenuBar, QFileDialog, QVBoxLayout, QGridLayout, QHBoxLayout, QWidget, QPushButton, QDoubleSpinBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QKeySequence, QAction, QPixmap


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi ventana")
        # etiqueta = QLabel()
        # etiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.setCentralWidget(etiqueta)

        #BOTON
        boton_abrir = QAction(QIcon('images/animal.png'), "Abrir", self)
        boton_abrir = QAction("Abrir", self)
        boton_abrir.setToolTip("Abrir archivo")
        boton_abrir.triggered.connect(self.botonAbrirClic)
        #Crear atajo de teclado
        boton_abrir.setShortcut(QKeySequence('Ctrl+a'))

        toolbar = QToolBar("Mi toolbar")
        self.addToolBar(toolbar)
        toolbar.addAction(boton_abrir)

        # Crear label para las imagenes
        ecuaciones = QLabel("x = v + Bw \n y = Av + w")
        labelA = QLabel("A = ")
        labelB = QLabel("B = ")
        self.original = QLabel("Imagen Original")
        self.conFiltro = QLabel("Imagen con Filtro")
        #self.conFiltro.resize(200, 200)



        #Crear menuBar
        barra_menu = QMenuBar()
        menu_archivo = barra_menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_abrir)

        layout = QHBoxLayout()
        derecho = QVBoxLayout()
        izquierdo = QGridLayout()

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        layout.addLayout(izquierdo)
        layout.addLayout(derecho)


        #botones de filtro
        boton = QPushButton("Aplicar Filtro")
        boton.clicked.connect(self.botonFiltros)
        # boton_y = QPushButton("Filtro Y")
        # boton_y.clicked.connect(self.botonFiltroY)

        #edit para elementos matrices
        self.elem_a = QDoubleSpinBox()
        self.elem_a.setRange(-10,10)
        self.elem_a.setSingleStep(0.1)
        self.elem_b = QDoubleSpinBox()
        self.elem_b.setRange(-10,10)
        self.elem_b.setSingleStep(0.1)

        izquierdo.addWidget(ecuaciones, 0, 0, 1 ,2)
        izquierdo.addWidget(labelA, 1, 0)
        izquierdo.addWidget(labelB, 2, 0)
        izquierdo.addWidget(self.elem_a, 1, 1)
        izquierdo.addWidget(self.elem_b, 2, 1)
        izquierdo.addWidget(boton, 3, 0, 1, 2)
        
        derecho.addWidget(self.original)
        derecho.addWidget(self.conFiltro)
        
        self.pixmap = QPixmap()
        self.setMenuBar(barra_menu)

    def botonAbrirClic(self, s):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        self.file_name = fname[0]
        print(fname, self.file_name)

        #cuando se seleccione una imagen
        if self.file_name:
            img = cv2.imread(self.file_name)

            #poner la Imagen en label
            self.pixmap = QPixmap(self.file_name)
            self.original.setPixmap(self.pixmap)
            self.original.resize(200, 200)


    def botonFiltros(self):
        if self.file_name:
            img = cv2.imread(self.file_name)
            rows, cols, dim = img.shape

            # transformation matrix for shearing
            # shearing applied to   both axis

            M = np.float32([[                  1, self.elem_a.value(),  0],
                            [self.elem_b.value(),                   1,  0],
                            [                  0,                   0,  1]]) 
            
            sheared_img = cv2.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))

            
            _, aaa = cv2.imencode('.jpg', sheared_img)

            self.pixmap = QPixmap()
            self.pixmap.loadFromData(aaa, 'JPG')
            self.conFiltro.setPixmap(self.pixmap)
            


    # def botonFiltroX(self):
    #     if self.file_name:
    #         img = cv2.imread(self.file_name)
    #         rows, cols, dim = img.shape
            
    #         # transformation matrix for shearing
    #         # shearing applied to x-axis

    #         M = np.float32([[1, self.elem_a.value(), 0],
    #                         [0, 1  , 0],
    #                         [0, 0  , 1]])
            
    #         sheared_img = cv2.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))

    #         cv2.imshow('Imagen Original', img)
    #         cv2.imshow('Imagen Sesgada',  sheared_img)
    #         cv2.waitKey(0)

    # def botonFiltroY(self):
    #     if self.file_name:
    #         img = cv2.imread(self.file_name)
    #         rows, cols, dim = img.shape
            
    #         # transformation matrix for shearing
    #         # shearing applied to x-axis

    #         M = np.float32([[1  , 0, 0],
    #                         [0.5, 1, 0],
    #                         [0  , 0, 1]])
            
    #         sheared_img = cv2.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))

    #         cv2.imshow('Imagen Original', img)
    #         cv2.imshow('Imagen Sesgada',  sheared_img)
    #         cv2.waitKey(0)
             

app = QApplication([])
ventana = VentanaPrincipal()
ventana.show()

app.exec()



# imagen en interfaz cuando la selecciono
# Las ventanas que salen deben ser de la main windows
# pend m = cot(\phi)
 
# POR HACER
#   Escribir las ecuaciones perronas
#   Fijar el tamaño de la ventana y de los botones



