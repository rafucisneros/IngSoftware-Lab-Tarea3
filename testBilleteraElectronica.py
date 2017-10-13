'''
Created on 13 oct. 2017

@author: Rafael Cisneros
'''
from unittest import *
from BilleteraElectronica import *


class TestBilleteraElectronica(unittest.TestCase):


    def setUp(self):
        self.billetera = BilleteraElectronica()        
        

    def tearDown(self):
        self.billetera = None
        

    def testBilletera(self):
        billetera = billeteraElectronica()
        assertEqual(billetera.saldo, 0,"La billetera deberia tener saldo 0")
        
    def testSaldo(self):
        pass
        
    def testConsumir(self):
        pass
    
    def testRecargar(self):
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()