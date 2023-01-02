# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:38:13 2022

@author: Luis Abaitua
"""
import numpy as np
def isattribute(lst):
#Checks if all the elements in a list are of the same type
    if all(elem_type(x) == elem_type(lst[0]) for x in lst):
       return True
    else:
       return False
def elem_type(elem):
    '''Returns the type of the attribute looking at the type of the first element in the list.'''
    if (type(elem)==int or type(elem)==float or type(elem)==np.int8 or type(elem)==np.float64):
        tipo='Numeric'
    elif (type(elem)==str):
        tipo='Categorical'
    elif (type(elem)==bool):
        tipo='Boolean'
    else:
        raise('The type is not valid')
    return(tipo)

def attribute_type(attribute):
    '''Returns the type of the attribute looking at the type of the first element in the list.'''
    if (type(attribute[0])==int or type(attribute[0])==float or type(attribute[0])==np.int8 or type(attribute[0])==np.float64):
        tipo='Numeric'
    elif (type(attribute[0])==str):
        tipo='Categorical'
    elif (type(attribute[0])==bool):
        tipo='Boolean'
    else:
        raise('The type is not valid')
    return(tipo)
