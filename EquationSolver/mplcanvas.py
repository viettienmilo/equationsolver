# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:02:46 2020

@author: MILOWORK
"""

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

colors =  {
            'lightest':"#eeeeee",
            'lighter':"#e5e5e5",
            'light':"#effffb",
            'himid':"#50d890",
            'midmid':"#1089ff",
            'lomid':"#4f98ca",
            'dark' :"#272727",
            'darker' :"#23374d",
            'darkgrey' :"#030303",
}

size_mid = {'stick': 9, 'axlabel': 10, 'axtitle': 12, 'legend': 9}
size_sm = {'stick': 6, 'axlabel': 7, 'axtitle': 9, 'legend': 6}

plt.rc('figure',figsize=(5,5),dpi=100)
plt.rc('axes',edgecolor = colors['dark'])
plt.rcParams['figure.facecolor'] = colors['lightest']
plt.rcParams['text.color'] = colors['dark']
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = colors['dark']
plt.rcParams['xtick.color'] = colors['dark']
plt.rcParams['ytick.color'] = colors['dark']
plt.rcParams['xtick.labelsize']= size_sm['stick']
plt.rcParams['ytick.labelsize']= size_sm['stick']
plt.rcParams['axes.titlesize']= size_sm['axtitle']
plt.rcParams['axes.labelsize']= size_sm['axlabel']
plt.rcParams['legend.fontsize']= size_sm['legend']
plt.rcParams['grid.alpha'] = 0.1
        
class MplCanvas(FigureCanvas):
    '''
    Class MplCanvas tạo đối tượng Figure của matplotlib
    cùng với các subplot cần thiết (có thể thêm hoặc bớt các subplot này)
    '''
    def __init__(self, parent=None):
        
        fig = Figure()
        self.axes = fig.add_subplot(111)  
        self.axes.grid()
        self.tight_layout = fig.set_tight_layout(True)
        
        super(MplCanvas, self).__init__(fig)

        