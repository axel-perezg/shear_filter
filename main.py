import numpy as np
import cv2
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QToolBar, QMenuBar, QFileDialog,
    QGridLayout, QHBoxLayout, QWidget, QPushButton, QDoubleSpinBox
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QKeySequence, QAction, QPixmap
import sys


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Filtro Oblicuo")
        self.setWindowIcon(QIcon('images/shear.png'))

        # Boton
        boton_abrir = QAction(QIcon('images/icons/open.png'), "Abrir", self)
        boton_abrir.setToolTip("Abrir archivo")
        boton_abrir.triggered.connect(self.botonAbrirClic)
        boton_abrir.setShortcut(QKeySequence('Ctrl+a'))

        boton_guardar = QAction(QIcon('images/icons/save.png'), "Guardar", self)
        boton_guardar.setToolTip("Guardar imagen con filtro")
        boton_guardar.triggered.connect(self.botonGuardarClic)
        boton_guardar.setShortcut(QKeySequence('Ctrl+s'))

        toolbar = QToolBar("Mi toolbar")
        self.addToolBar(toolbar)
        toolbar.addAction(boton_abrir)
        toolbar.addAction(boton_guardar)

        labelA = QLabel("Factor de corte horizontal: ")
        labelB = QLabel("Factor de corte vertical: ")
        labelA.setFixedWidth(140)
        labelB.setFixedWidth(140)

        self.original = QLabel("Imagen Original")
        self.original.setFixedWidth(480)
        self.original.setFixedHeight(480)

        self.conFiltro = QLabel("Imagen con Filtro")
        self.conFiltro.setFixedWidth(480)
        self.conFiltro.setFixedHeight(480)

        # Crear menuBar
        barra_menu = QMenuBar()
        menu_archivo = barra_menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_abrir)
        menu_archivo.addAction(boton_guardar)

        # LAYOUTS
        layout = QHBoxLayout()
        derecho = QHBoxLayout()
        izquierdo = QGridLayout()

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        layout.addLayout(izquierdo)
        layout.addLayout(derecho)

        # Botones de filtro
        boton = QPushButton("Aplicar Filtro")
        boton.clicked.connect(self.botonFiltros)
        boton.setFixedHeight(40)

        # Edit para elementos matrices
        self.elem_a = QDoubleSpinBox()
        self.elem_a.setRange(-10, 10)
        self.elem_a.setSingleStep(0.1)
        self.elem_a.setFixedWidth(160)
        self.elem_a.setFixedHeight(40)

        self.elem_b = QDoubleSpinBox()
        self.elem_b.setRange(-10, 10)
        self.elem_b.setSingleStep(0.1)
        self.elem_b.setFixedWidth(160)
        self.elem_b.setFixedHeight(40)

        izquierdo.addWidget(labelA, 0, 0)
        izquierdo.addWidget(labelB, 1, 0)
        izquierdo.addWidget(self.elem_a, 0, 1)
        izquierdo.addWidget(self.elem_b, 1, 1)
        izquierdo.addWidget(boton, 2, 0, 1, 2)

        derecho.addWidget(self.original)
        derecho.addWidget(self.conFiltro)

        self.pixmap = QPixmap()
        self.setMenuBar(barra_menu)

    def botonAbrirClic(self, s):
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        self.file_name = fname[0]
        print(fname, self.file_name)

        # Cuando se seleccione una imagen
        if self.file_name:
            img = cv2.imread(self.file_name)

            # Poner la Imagen en label
            self.pixmap = QPixmap(self.file_name)
            scaled_img = self.pixmap.scaled(QSize(500, 500), Qt.AspectRatioMode.KeepAspectRatio)
            self.original.setPixmap(scaled_img)

    def botonGuardarClic(self):
        cv2.imwrite('imagenfiltro.png', self.sheared_img)

    def botonFiltros(self):
        if self.file_name:
            img = cv2.imread(self.file_name)
            rows, cols, dim = img.shape

            # Transformation matrix for shearing
            # Shearing applied to both axes
            M = np.float32([
                [1, self.elem_a.value(), 0],
                [self.elem_b.value(), 1, 0],
                [0, 0, 1]
            ])

            self.sheared_img = cv2.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))

            _, imag = cv2.imencode('.jpg', self.sheared_img)

            self.pixmap = QPixmap()
            self.pixmap.loadFromData(imag, 'JPG')
            scaled_img = self.pixmap.scaled(QSize(500, 500), Qt.AspectRatioMode.KeepAspectRatio)
            self.conFiltro.setPixmap(scaled_img)


app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
sys.exit(app.exec())




