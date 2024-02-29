class Part:

    # constructor
    def __init__(self,pnum,name,price):
        self.pno = pnum
        self.pname = name
        self.price = price
    
    # getter
    def get_pno(self):
        return self.pno

	# getter
    def	get_pname(self):
        return self.pname

	# getter
    def get_price(self):
        return self.price

    # setter
    def set_pno(self,pnum):
        self.pno = pnum

	# setter
    def set_pname(self,name):
        self.pname = name

	# setter
    def set_price(self,price):
        self.price = price

	# return string representation of Part object
    def __str__(self):
        return f"{self.pno}:{self.pname}:{self.price}"