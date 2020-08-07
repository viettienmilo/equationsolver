# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:02:46 2020

@author: MILOWORK
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

class EquationSolver():
    
    def __init__(self, expr='', start=-5, stop=5, prec=3):
        self.__expr = expr
        self.__start = start
        self.__stop = stop
        self.__prec = prec
        
    @property
    def expr(self):
        return self.__expr
        
    @property
    def precision(self):
        return self.__prec
    
    @property
    def delta(self):
        return 1/10**self.__prec
    
    def expr_convert(self, x):
        return eval(self.__expr)
    
    def diff_convert(self):
        x = sp.Symbol('x')
        diff = sp.diff(self.__expr,x)
        return str(diff)
    
    def f(self, x):
        return self.expr_convert(x)

    def diff(self,x):
        return eval(self.diff_convert())
        
    def condition_check(self):
        a = self.__start
        b = self.__stop
        
        if self.f(a) == 0:
            return a
        elif self.f(b) == 0:
            return b
        elif self.f(a)*self.f(b) > 0:
            return False
        else:
            return True
        
    def bisection(self):
        a = self.__start
        b = self.__stop
        counter = 0
        chk = self.condition_check()
        
        if chk and isinstance(chk,bool):
            while True:
                counter += 1
                c = (a+b)/2
                if abs(self.f(c)) <= self.delta:
                    break
                else:
                    if self.f(c) > 0:
                        b = c
                    else:
                        a = c
            return c, counter
        else:
            return chk, counter
        
    def newton_raphson(self):
        x = self.__stop
        counter = 0
        chk = self.condition_check()
        
        if chk and isinstance(chk,bool):
            while True:
                counter += 1
                y = x
                x = y - self.f(y)/self.diff(y)
                if abs(x-y) <= self.delta:
                    break
            return x, counter
        else:
            return chk, counter
    
    def secant(self):
        a = self.__start
        b = self.__stop
        counter = 0
        chk = self.condition_check()
        
        x = a-(b-a)*self.f(a)/(self.f(b)-self.f(a))
        
        if chk and isinstance(chk,bool):
            while True:
                counter += 1
                if self.f(a)*self.f(x) < 0:
                    b = x
                    x = a-(b-a)*self.f(a)/(self.f(b)-self.f(a))
                    if abs(x-b) <= self.delta:
                        break
                else:
                    a = x
                    x = a-(b-a)*self.f(a)/(self.f(b)-self.f(a))
                    if abs(x-a) <= self.delta:
                        break
            return x, counter
        else:
            return chk, counter
        
    def plot_graph(self, ax=None, start=None, stop=None, res=0.01):
        if ax == None:
            ax = plt.axes()
        if start == None:
            start = self.__start
        if stop == None:
            stop = self.__stop
        x = np.arange(start, stop, res)
        y = self.f(x)
        ax.plot(x, y, 'b-', label = self.__expr)
        ax.plot(x,np.zeros(len(x)), 'r-', label = 'y=0')
        ax.plot(self.newton_raphson()[0], np.zeros(1),'ko', label='solution')
        return ax

