# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 16:34:53 2022

@author: Luis Abaitua
"""
import numpy as np
from data_pack.datapack.attrutils import isattribute,attribute_type
class Attribute:
    'A class to work with attributes of different categories'
    def __init__(self,attribute,tipo=None):
        if isattribute(attribute):
            self.attribute=np.array(attribute)
        else:
            raise NameError('The list has elements of different types')
        if tipo=='Categorical':
            [str(x) for x in attribute]
        elif tipo=='Boolean':
            [x==attribute[0] for x in attribute]
        elif tipo=='Numeric':
            if attribute_type(attribute)!='Numeric':
                raise NameError('The attribute is not numeric')
        elif tipo==None:
            tipo=attribute_type(attribute)
        else:
            raise NameError('The type has to be Numeric Categorical or Boolean')
        self.tipo=tipo   
    def __str__(self):
        return str(self.attribute)
    def __repr__(self):
        return str(self.attribute)+' , '+str(self.tipo)
    def __len__(self):
        return(len(self.attribute))
