import sys
from PyQt4 import QtGui, uic
from conv_temp_logica import ConvTemp

app = QtGui.QApplication(sys.argv)
MyApp = ConvTemp()
MyApp.show()
sys.exit(app.exec_())