from Customer import *

class Customers:
    def __init__(self):
        self.customers = {}
    
    def setCustomer(self, cno, c):
        if cno not in self.customers:
            self.customers[cno] = c
    
    def getCustomer(self,cno):
        if cno in self.customers:
            return self.customers.get(cno,None)
        
    def get_cnos(self):
        customer_numbers = []
        for keys in self.customers.keys():
            customer_numbers.append(keys)
        return customer_numbers
    def __str__(self):
        return "\n".join(str(customer) for customer in self.customers.values())
        