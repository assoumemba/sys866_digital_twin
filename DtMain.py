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
from pyqtgraph.Qt import QtCore

from utils import ROOT_DIR
from DT.DtModelController import DtModelController

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)
dt_controller = DtModelController()

def setup_ui(ui):
    _translate = QtCore.QCoreApplication.translate

    #Sensor Data - Canopy cover
    global sensor_cc_curve
    ui.gb_stat_1.setTitle(_translate("MainWindow", "Capteurs - Canopy cover"))
    sensor_cc_curve = ui.stat_graph_1.plot()
    

    #Modele numerique
    global dt_cc_curve, dt_cc_max_curve, dt_depletion_curve
    ui.gb_stat_2.setTitle(_translate("MainWindow", "Modele numerique - Canopy Cover / Max / Humidite du sol"))

    dt_cc_curve= ui.stat_graph_2.plot(pen=(255,0,0), name="Canopy Cover")
    dt_cc_max_curve = ui.stat_graph_2.plot(pen=(0,255,0), name="Canopy Maximale")
    dt_depletion_curve = ui.stat_graph_2.plot(pen=(0,0,255), name="Humidite")

    #Drawing irrigation_curve
    global irrigation_curve
    ui.gb_stat_3.setTitle(_translate("MainWindow", "Periodes irrigation"))
    irrigation_curve = ui.stat_graph_3.plot(pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')

    #Progress bar
    global progress_bar
    progress_bar = ui.progressBar
    progress_bar.setProperty("value", 0)
    


def update():
    global sensor_cc_curve
    global irrigation_curve
    global dt_cc_curve, dt_cc_max_curve, dt_depletion_curve
    global progress_bar

    #advance one day
    dt_controller.run_step()

    #irrigation
    irrigation_data_points = dt_controller.get_irrigation_points()
    irrigation_curve.setData(irrigation_data_points)

    #Sensor Data - Canopy cover
    sensor_cc_points = dt_controller.get_sensor_cc_points()
    sensor_cc_curve.setData(sensor_cc_points)

    #Modele numerique
    dt_cc_points = dt_controller.get_dt_cc_points()
    dt_cc_curve.setData(dt_cc_points)

    dt_max_cc_points = dt_controller.get_dt_max_cc_points()
    dt_cc_max_curve.setData(dt_max_cc_points + 5)

    dt_depletion_points = dt_controller.get_dt_depletion_points()
    dt_depletion_curve.setData(dt_depletion_points + 10)

    #progression
    progress_bar.setProperty("value", dt_controller.get_progression_rate() + 1)
    


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    setup_ui(ui)

    #Update every period
    timer = QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(1000)
    
    MainWindow.show()
    sys.exit(app.exec())



