#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:24:40 2021

@author: himajav
"""

import izhikevich_cells as izh
# nickname for class
class ccCell(izh.izhCell):
    def __init__(self, stimVal):
        """Call super constructor from izhCell cless and redefine parameter values """
        super().__init__(stimVal)
        self.celltype = "Chattering"
        self.C = 50
        self.vr = -60 
        self.vt = -40 
        self.k = 1.5
        self.a = 0.03 
        self.b = 1
        self.c = -40
        self.d = 150 
        self.vpeak = 25 
        
def createCell():
    """Create an ccCell and call the simulate function"""
    myCell = izh.izhCell(stimVal=4000)        
    myCell.simulate()
    izh.plotMyData(myCell)
        
x = ccCell(4000)
        