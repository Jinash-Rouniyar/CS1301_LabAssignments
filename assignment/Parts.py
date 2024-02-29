from Part import *

class Parts():

    # constructor
    def __init__(self):
        self.parts = {}

    # add Part object p to dictionary; do not add if part number already exists
    def add_part(self, p):
        if p.get_pno() not in self.parts:
            self.parts[p.get_pno()] = p

    # return Part object for pno; return None if no part with pno
    def get_part(self,pno):
        return self.parts.get(pno,None)

    # return a list of all part numbers
    def get_pnos(self):
        pno_list = []
        for keys in self.parts.keys():
            pno_list.append(keys)
        return pno_list
        
    # return string representation of Parts object
    def __str__(self):
        return '\n'.join(str(part) for part in self.parts.values())