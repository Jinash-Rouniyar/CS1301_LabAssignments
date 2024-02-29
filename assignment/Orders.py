from Order import *


class Orders():

    # constructor
    def __init__(self):
        self.orders = {}

    # add order to dictionary; do not add if ono already exists.
    def add_order(self,o):
        if o.get_ono() not in self.orders:
            self.orders[o.get_ono()] = o

    # return Order object for ono; return None if no Order with ono
    def get_order(self,ono):
        if ono in self.orders:
            return self.orders.get(ono)
        else:
            return None

    # delete order with order number ono; return True
    # if ono not in dictionary do nothing and return False
    def delete_order(self,ono):
        if ono in self.orders:
            del self.orders[ono]
            return True
        else:
            return False

    # return a list of order numbers for orders placed by customer number cno
    def get_orders_for_customer(self,cno):
        list = []
        for key,value in self.orders.items():
            if value.get_placed_by().get_cno() == cno:
                list.append(key)
        return list
        
    
    # return a list of all order numbers
    def get_onos(self):
        o_list = []
        for keys in self.orders.keys():
            o_list.append(keys)
        return o_list
    


    # return string representation of Orders object
    def __str__(self):
        return "\n".join(str(order) for order in self.orders.values())