import sys

from Customer import *
from Customers import *
from Part import *
from Parts import *
from Order import *
from Orders import *

# Open three files, customers.dat, parts.dat, and orders.dat, 
# present in directory dname.
# Read the data and construct the customers, parts, and orders objects
# Return the three objects as a tuple (see main() for the order)
def load_data(dname):
	# load customers data
    cfname = dname + "/customers.dat"
    pfname = dname + "/parts.dat"
    ofname = dname + "/orders.dat"
    c2 = Customers()
    p2 = Parts()
    o2 = Orders()
    with open(cfname) as f:
        data = f.read().splitlines()
        for lines in data:
            records = lines.split(":")
            c1 = Customer(int(records[0]),records[1],records[2])
            c2.setCustomer(int(records[0]),c1)
            # c2.customers.update({int(c1.get_cno()): c1.__str__()})
			  
    # load parts data      
    with open(pfname) as f:
        data = f.read().splitlines()
        for lines in data:
            records = lines.split(":")
            p1 = Part(int(records[0]),records[1],float(records[2]))
            p2.add_part(p1)
            # p2.parts.update({p1.get_pno(): p1.__str__()})	
            
    with open(ofname) as f:
            data = f.read().splitlines()
            for lines in data:
                records = lines.split(":")    
                customer = c2.getCustomer(int(records[1]))
                o1 = Order(records[0],customer,records[2])
                for i in range(3,len(records)):
                    items = records[i].split(",")
                    part = p2.get_part(int(items[0]))
                    o1.add_item((part,items[1],items[2]))
                o2.add_order(o1) 


    return c2, p2, o2

# Store data from customers, parts, and orders objects into three files, 
# customers.dat, parts.dat, and orders.dat in the folder named dname; 
# Use same format as when you loaded the data
def store_data(customers,parts,orders,dname):
    with open(f"{dname}/customers.dat", "w") as file:
        for cno in customers.get_cnos():
            customer = customers.getCustomer(cno)
            file.write(f"{customer}\n")
    
    with open(f"{dname}/parts.dat", "w") as file:
        for pno in parts.get_pnos():
            part = parts.get_part(pno)
            file.write(f"{part}\n")

    with open(f"{dname}/orders.dat", "w") as file:
        for ono in orders.get_onos():
            order = orders.get_order(ono)
            file.write(f"{order.writable_output()}\n")

def main():
	customers,parts,orders = load_data(sys.argv[1])
	print("\nWelcome to Orders Database Program\n")
	while True:
		command = input("c, c cno, o ono, u ono pno discount, d ono pno, q: ").strip()
		if len(command) < 1:
			print("\nInvalid command!\n")
			continue
		elif command[0] == 'c' and len(command) == 1:
			print()
			lines = customers.__str__().splitlines()
			for elements in lines:
				element = elements.split(":")
				print(f"CNO: {element[0]}")
				print(f"CNAME: {element[1]}")
				print(f"CITY: {element[2]}\n")

		elif command[0] == 'c' and len(command) > 1:
			cno = int(command[1:].strip())
			c = customers.getCustomer(cno)
			print()
			print(f"CNO: {c.get_cno()}")
			print(f"CNAME: {c.get_name()}")
			print(f"CITY: {c.get_city()}\n")
			onos = orders.get_orders_for_customer(cno)
			print("ORDERS: ",end="")
			for ono in onos:
				print(ono," ",end="")
			print("\n")
		elif command[0] == 'o':
			ono = command[2:].strip().upper()
			o = orders.get_order(ono)
			if o != None:
				print()
				#formatted output
				output_list = o.__str__().split(":")
				print(f"Order no: {output_list[0]}")
				print(f"Placed by: CNO: {output_list[1]}")
				print(f"CNAME: {output_list[2]}")
				print(f"City: {output_list[3]}\n")
				print(f"Order date: {output_list[4]}")
				print(f"{'PNO':<5}{'PNAME':<18}{'PRICE':<8}{'QTY':<5}{'%DISCOUNT':<10}{'COST':>9}")
				receipt = output_list[5:]
				total_cost = 0
				for i in range(0,len(receipt),3):	
					p_number,p_name,small_parts = receipt[i],receipt[i+1],receipt[i+2].split(",")
					cost = float((float(small_parts[0])*int(small_parts[1]))*(1-float(small_parts[2])/100))
					print(f"{p_number:<5}{p_name:<20}{small_parts[0]:<7}{small_parts[1]:<10}{small_parts[2]:<8}{cost:>4.2f}")
					total_cost +=cost
				print(f"TOTAL{'':<45}{total_cost:.2f}\n")
			else:
				print("\n"+ono+" NOT FOUND\n")
		elif command[0] == 'u':
			ono, pno, discount = command[2:].split()
			pno = int(pno)
			discount = int(discount)
			o = orders.get_order(ono)
			if o != None:
				print()
				if o.update_discount(pno,discount):
					print("Discount updated!\n")
				else:
					print("No such part in order!\n")
			else:
				print("\n"+ono+" NOT FOUND\n")
		elif command[0] == 'd':
			ono, pno = command[2:].split()
			pno = int(pno)
			o = orders.get_order(ono)
			if o != None:
				print()
				if o.delete_part(pno):
					print("Part deleted from order!\n")
					if o.empty_order():
						if orders.delete_order(o):
							print("Empty order deleted!")
						else:
							print("Something went wrong!")
				else:
					print("No such part in order!\n")
			else:
				print("\n"+ono+" NOT FOUND\n")
		elif command[0] == 'q':
			break
		else:
			print("\nInvalid command\n")
	store_data(customers,parts,orders,sys.argv[1])
	print("\nBye!\n")
 
main()