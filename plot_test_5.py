## PyQt5 version of plot_test.py ##
import sys, os, random
from PyQt5 import QtWidgets, QtGui, QtCore

import matplotlib
matplotlib.use('QT5Agg')   ###
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas   ###
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar  ###
from matplotlib.figure import Figure
import numpy as np

class AppForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.create_main_frame()
        self.on_draw()

    def on_draw(self):
        # Plot three functions
        t = np.arange(0, 5, .2)
        # Plot some functions and change the range of axes
        self.axes.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
        self.axes.axis([0, 6, 0, 150])
        # Update canvas by redrawing with current state of figure
        self.canvas.draw()

    def create_main_frame(self):
        self.main_frame = QtWidgets.QWidget()
        # Create new figure to put plots on
        self.fig = Figure()
        # Create canvas to draw figure on
        self.canvas = FigureCanvas(self.fig)
        # Canvas is a child on main_frame
        self.canvas.setParent(self.main_frame)
        
        # self.axes now references the first subplot
        self.axes = self.fig.add_subplot(111)
        # Create a matplotlib toolbar for the canvas. Set parent to main_frame
        self.mpl_toolbar = NavigationToolbar(self.canvas, self.main_frame)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.mpl_toolbar)

        self.main_frame.setLayout(vbox)
        self.setCentralWidget(self.main_frame)



app = QtWidgets.QApplication(sys.argv)
form = AppForm()
form.show()
app.exec_()
