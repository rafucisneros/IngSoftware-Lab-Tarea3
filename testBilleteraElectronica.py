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
        self.billetera = BilleteraElectronica()        
        

    def tearDown(self):
        self.billetera = None
        
    def testBilletera(self):
        billetera = BilleteraElectronica()
        self.assertEqual(billetera.saldo, 0,"La billetera deberia tener saldo 0")
        
    def testConsumir(self):
        pass
    
    def testRecargar(self):
        pass
 
    def testSaldo(self):
        self.assertEqual(self.billetera.saldo, 0,"La billetera deberia tener saldo 0")
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()