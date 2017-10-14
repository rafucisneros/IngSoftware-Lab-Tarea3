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
        return self.saldo
    
    def recargar(self, *args): # args es un objeto Credito o un conjunto de elementos [monto, fecha, idEstablecimiento]
        if len(args) == 3:
            recarga = Credito(args[0], args[1], args[2]) #(monto, fecha, idEstablecimiento)
        elif len(args) == 1:
            recarga = args[0]
        else:
            print("Error en la cantidad de argumentos")
            
        self.creditos.append(recarga)
        self.saldo = self.saldo + recarga.monto       
    
    def consumir(self, *args): # args es un objeto Credito o un conjunto de elementos [monto, fecha, idEstablecimiento]
        if len(args) == 3:
            consumo = Debito(args[0], args[1], args[2])
        elif len(args) == 1:
            consumo = args[0]
        else:
            print("Error en la cantidad de argumentos")
            
        self.debitos.append(consumo)
        self.saldo = self.saldo - consumo.monto