#!/usr/bin/env python
# -*- coding: 850 -*-
'''
Created on 13 oct. 2017

@author: Rafael Cisneros
'''

from ClassCredito import Credito
from ClassDebito import Debito

class BilleteraElectronica(object):

    def __init__(self, identificador, nombres, apellidos, CI, PIN):
        self.id = identificador
        self.nombresDue¤o = nombres
        self.apellidosDue¤o = apellidos
        self.CIDue¤o = CI
        self.PIN = PIN
        self.creditos = []
        self.debitos = []
        self.saldo = 0
        
    def saldo(self):
        pass
    
    def recargar(self):
        pass
    
    def consumir(self):
        pass
        