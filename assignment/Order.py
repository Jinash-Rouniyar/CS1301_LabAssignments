from Parts import *
class Order():

    # constructor
    def __init__(self,ono,cust,d):
        self.ono = ono
        self.placed_by = cust
        self.order_date = d
        self.items = []

    # add item (triple made up of part, quantity, and discount) to self.items
    def add_item(self,item):
        self.items.append(item)

    # getters
    def get_ono(self):
        return self.ono
    
    def get_placed_by(self):
        return self.placed_by
    
    def get_order_date(self):
        return self.order_date
    
    def get_items(self):
        return self.items
    
    # setters
    def set_ono(self,ono):
        self.ono = ono
    
    def set_placed_by(self,cust):
        self.placed_by = cust
        
    
    def set_order_date(self,d):
        self.order_date = d
    
    def set_items(self,items):
        self.items = items

    # update discount value for a give part number pno in order to discount; return True
    # do nothing if pno is not in items; return False
    def update_discount(self,pno,discount):
        for index, element in enumerate(self.items):
            if element[0].get_pno() == pno:
                self.items[index] = [element[0],element[1],int(discount)]
                return True
        return False


    # delete part with part number pno from items and return True; 
    # do nothing if pno is not in items; return False
    def delete_part(self,pno):
        for element in self.items:
            if element[0].get_pno() == pno:
                self.items.remove(element)
                return True
        return False

    # return True if order contains no parts; False otherwise
    def empty_order(self):
        if not self.items:
            return True
        else:
            return False
        
    def writable_output(self):
        item_str = ":".join(f"{item[0].get_pno()},{item[1]},{item[2]}" for item in self.items)                
        return f"{self.ono}:{self.placed_by.get_cno()}:{self.order_date}:{item_str}"
    

    # return string representation of the order (see output for format!)
    def __str__(self):
        item_str = ':'.join(f"{item[0]},{item[1]},{item[2]}" for item in self.items)
        return f"{self.ono}:{self.placed_by}:{self.order_date}:{item_str}"
        
