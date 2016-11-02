# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui, uic

Ui_MainWindow = uic .loadUiType("conv_temp_gui.ui")[0]

class ConvTemp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.btnConvertir.clicked.connect(self.btn_convertir_clicked)
        self.btnSalir.clicked.connect(self.btn_salir_clicked)
        self.btnLimpiar.clicked.connect(self.btn_limpiar_clicked)

    def btn_convertir_clicked(self):
        try:
            flt_cel = float(self.txtCelcius.text())
            flt_kel = 273.15 + flt_cel
            self.lblKelvin.setText(self.lblKelvin.text())
        #self.lblKelvin.setText(str(fltKel) + "Kelvin")
            self.txtKelvin.setText(str(flt_kel))
        except:
            QtGui.QMessageBox.question(self,u"Infromación","El dato debe ser numerico")

    def btn_limpiar_clicked(self):
        self.txtCelcius.clear()
        self.txtKelvin.clear()

    def btn_salir_clicked(self):
        sys.exit()