'''
Created on 13 oct. 2017

@author: Rafael Cisneros
'''
from pip._vendor.pyparsing import ident
from Creditos import *
from Debitos import *

class BilleteraElectronica(object):
    '''
    classdocs
    '''


    def __init__(self, identificador, nombres, apellidos, CI, PIN):
        self.id = identificador
        self.nombresDue�o = nombres
        self.apellidosDue�o = apellidos
        self.CIDue�o = CI
        self.PIN = PIN
        self.creditos = []
        self.debitos = []
        self.saldo = 0
        
    def saldo(self):
        pass
        