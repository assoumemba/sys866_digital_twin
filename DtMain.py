"""
https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/
https://www.pythonguis.com/tutorials/pyqt6-embed-pyqtgraph-custom-widgets-qt-app/
command: pyqt6-tools designer
         pyqt6-tools --help
         pyuic6 -x gui_main.ui -o DtMainWindow.py

This example demonstrates many of the 2D plotting capabilities
in pyqtgraph. All of the plots may be panned/scaled by dragging with 
the left/right mouse buttons. Right click on any plot to show a context menu.
"""

import sys
import numpy as np
from Visualization.DtMainWindow import Ui_MainWindow

import pyqtgraph as pg
from PyQt6 import QtWidgets


# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)

def setup_ui(ui):

    #graph 1
    ui.stat_graph_1.plot(y=np.random.normal(size=100))
    

    #Multiple curves
    ui.stat_graph_2.plot(np.random.normal(size=100), pen=(255,0,0), name="Red curve")
    ui.stat_graph_2.plot(np.random.normal(size=110)+5, pen=(0,255,0), name="Green curve")
    ui.stat_graph_2.plot(np.random.normal(size=120)+10, pen=(0,0,255), name="Blue curve")

    #Drawing with points
    ui.stat_graph_3.plot(np.random.normal(size=100), pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')



if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    setup_ui(ui)
    
    MainWindow.show()
    sys.exit(app.exec())



