# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:02:46 2020

@author: MILOWORK
"""

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavTBar
from equationsolver import EquationSolver
from mainui import Ui_mWin
from mplcanvas import MplCanvas

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    
class mWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mui = Ui_mWin()
        self.mui.setupUi(self)
        self.setFixedSize(730,450)
        self.setWindowIcon(QIcon('app.png'))

        self.plot_canvas = MplCanvas()     
        self.navTBar = NavTBar(self.plot_canvas,self)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.navTBar)
        layout.addWidget(self.plot_canvas)
        self.mui.wgPlot.setLayout(layout)
        
        self.mui.btnSolve.clicked.connect(self.solve)
        
    def solve(self):
        expr = self.mui.txtExpr.text()
        start = self.mui.dsbStart.value()
        stop = self.mui.dsbStop.value()
        precision = self.mui.sbPrecision.value()

        solver = EquationSolver(expr, start, stop, precision)
        
        bs, bssteps = solver.bisection()
        if bs:
            res = str(round(bs,solver.precision))
            st = str(bssteps)
        else:
            res = 'no solutions'
            st = 'N/a'
        self.mui.lblBi.setText(res)
        self.mui.lblBiSteps.setText(st)
        
        nr, nrsteps = solver.newton_raphson()
        if bs:
            res = str(round(nr,solver.precision))
            st = str(nrsteps)
        else:
            res = 'no solutions'
            st = 'N/a'
        self.mui.lblNr.setText(res)
        self.mui.lblNrSteps.setText(st)
        
        se, sesteps = solver.secant()
        if se:
            res = str(round(se,solver.precision))
            st = str(sesteps)
        else:
            res = 'no solutions'
            st = 'N/a'
        self.mui.lblSe.setText(res)
        self.mui.lblSeSteps.setText(st)
        
        ax = self.plot_canvas.axes
        ax.clear()
        solver.plot_graph(ax)
        ax.legend(loc='best')
        ax.set_title('SOLUTION IN RANGE [{}, {}]'.format(start,stop))
        ax.grid()
        self.plot_canvas.draw()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mWin = mWindow()
    mWin.show()
    
    sys.exit(app.exec_())
