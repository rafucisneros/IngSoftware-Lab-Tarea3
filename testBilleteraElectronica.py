#/!usr/bin/env python
# -*- coding: 850 -*-
'''
Created on 13 oct. 2017

@author: Rafael Cisneros
'''

import unittest
from ClassBilleteraElectronica import BilleteraElectronica
from ClassCredito import Credito
from ClassDebito import Debito

class TestBilleteraElectronica(unittest.TestCase):

    def setUp(self):
        self.billetera = BilleteraElectronica(1,"Rafael","Cisneros",24759502,123)        
        

    def tearDown(self):
        self.billetera = None
        
    def testBilletera(self):
        self.assertEqual(self.billetera.saldo, 0,"La billetera deberia tener saldo 0")
        self.assertEqual(len(self.billetera.debitos), 0,"La billetera no deberia tener debitos")
        self.assertEqual(len(self.billetera.debitos), 0,"La billetera no deberia tener debitos")
        self.assertEqual(self.billetera.nombresDue¤o, "Rafael","Error con los nombres del due¤o de la billetera")
        self.assertEqual(self.billetera.nombresDue¤o, "Rafael","Error con los apellidos del due¤o de la billetera")

                
    def testConsumir(self):
        saldoActual = self.billetera.saldo
        cantidadActualDebitos = len(self.billetera.debitos)
        consumo = Debito(100.00, 13/10/2017, 1)
        self.billetera.consumir(consumo)
        self.assertEqual(len(self.billetera.debitos), cantidadActualDebitos+1, "Error en la cantidad total de debitos")
        self.assertEqual(self.billetera.saldo, saldoActual - consumo.monto, "Error en el nuevo saldo total")
    
    def testRecargar(self):
        saldoActual = self.billetera.saldo
        cantidadActualCreditos = len(self.billetera.creditos)
        recarga = Credito(100.00, 13/10/2017, 1)
        self.billetera.recargar(recarga)
        self.assertEqual(len(self.billetera.creditos), cantidadActualCreditos+1, "Error en la cantidad total de creditos")
        self.assertEqual(self.billetera.saldo, saldoActual + recarga.monto, "Error en el nuevo saldo total")
 
    def testSaldo(self):
        saldoActual = self.billetera.saldo
        recarga1 = Credito(122.00, 13/10/2017, 1)
        self.billetera.recargar(recarga1)
        recarga2 = Credito(982.00, 13/10/2017, 1)
        self.billetera.recargar(recarga2)
        consumo1 = Debito(123.00, 13/10/2017, 1)
        self.billetera.consumir(consumo1)
        consumo2 = Debito(642.00, 13/10/2017, 1)
        self.billetera.consumir(consumo2)
        consumo3 = Debito(132.00, 13/10/2017, 1)
        self.billetera.consumir(consumo3)
        consumo4 = Debito(1011.00, 13/10/2017, 1)
        self.billetera.consumir(consumo4)
        recarga3 = Credito(323.00, 13/10/2017, 1)
        self.billetera.recargar(recarga3)   
        self.assertEqual(self.billetera.saldo, (saldoActual + recarga1.monto + recarga2.monto + recarga3.monto - consumo1.monto - 
                                                consumo2.monto - consumo3.monto - consumo4.monto), "Error en el nuevo saldo total") 
    if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
        unittest.main()