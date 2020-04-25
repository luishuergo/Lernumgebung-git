# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 15:07:52 2020

@author: saturn
"""

def add(x,y):
    #Die Funktion add addiert
    #hier werde ich ein paar Änderungen vornehmen
    
    xplusy = x + y
    
    return xplusy
    
def subtract(x,y):
    #Die Funktion subtract subtrahiert
    return x-y

def multiply(x,y):
    #Die Funktion multiply multiplizert
    return x*y

def divide(x,y):
    #Die Funktion divide dividiert,falls y ungleich Null
    if y != 0:
		div = x/y
	else:
		div = 0
	
    return div
