class Customer:
    def __init__(self,cnum,name,city):
        self.cno = cnum
        self.name = name
        self.city = city
    
    #getter
    
    def get_cno(self):
        return self.cno

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    # setter
    def set_cno(self,cnum):
        self.cno = cnum

    # setter
    def set_name(self,name):
        self.name = name

    # setter
    def set_city(self,city):
        self.cty = city

    # return string representation of Customer object
    def __str__(self):
        return f"{self.cno}:{self.name}:{self.city}"
