import sys
def read_data(fname):
    with open(fname) as f:
        data = f.read().splitlines()
        return data
def remove_comments(data):
    result = []
    for line in data:
        if line.strip() != "":
            if line[0] != "#":
                result.append(line.upper())
    return result

def create_registers(data):
    registers = {}
    for line in data:
        xs = line.split()
        if len(xs) > 1 and xs[1] == "=":    
            registers[xs[0]] = int(xs[2])
        else:
              for x in xs:
                    if x[0] == "R" and x not in registers:
                          registers[x] = 0
    return registers
def create_input_registers(data):
    input_registers = {}
    for line in data:
        xs = line.split()
        if len(xs) > 1 and xs[1] == "=":    
            input_registers[xs[0]] = int(xs[2])
    return input_registers

def create_labels(data):
    labels = {}
    ino = 0
    for line in data:
        xs = line.split()
        if xs[0][-1] == ":":
            labels[xs[0][:-1]] = ino
        if len(xs) == 1 or (len(xs) > 1 and xs[1] != "="):
            ino = ino + 1     
    return labels

def create_code(data):
    code = []
    for line in data:
        xs = line.split()
        if "INC" in xs:
            if len(xs) == 1 or len(xs) > 3:
                print("INVALID INSTRUCTION")
                return []
            elif len(xs) == 2:
                code.append({'opcode':"INC","register1":xs[1]})
            else:
                code.append({'labeldef':xs[0][:-1].upper(),'opcode':"INC","register1":xs[2].upper()})
        elif "DEC" in xs:
            if len(xs) ==1 or len(xs)>3:
                print("Invalid Instruction")
                return []
            elif len(xs) == 2:
                code.append({'opcode': "DEC", 'register1': xs[1]})
            else:
                code.append({'labeldef': xs[0][:-1].upper(), 'opcode': "DEC", 'register1': xs[2].upper()})
        elif "CLR" in xs:
            if len(xs) ==1 or len(xs)>3:
                print("Invalid Instruction")
                return []
            elif len(xs) == 2:
                code.append({'opcode': "CLR", 'register1': xs[1]})
            else:
                code.append({'labeldef': xs[0][:-1].upper(), 'opcode': "CLR", 'register1': xs[2].upper()})
        elif "MOV" in xs:
            if len(xs)<=2 or len(xs)>4:
                print("Invalid Instruction")
                return []
            elif len(xs) == 3:
                code.append({'opcode': 'MOV', 'register1': xs[1], 'register2' : xs[2]})
            else:
                code.append({'labeldef': xs[0][:-1].upper(),'opcode': 'MOV', 'register1': xs[2].upper(), 'register2' : xs[3].upper()})
        elif "JMP" in xs:
            if len(xs)<2 or len(xs)>4:
                print("Invalid Instruction")
                return []
            elif len(xs) == 2:
                code.append({'opcode': 'UJMP','jmplabel': xs[1].upper()})
            elif len(xs) == 3:
                if xs[0][0] != "N":
                    code.append({'register1': xs[0].upper(),'opcode':'CJMP','jmplabel':xs[2].upper()})
                else:
                    code.append({'labeldef': xs[0][:-1].upper(), 'opcode': 'UJMP','jmplabel': xs[2].upper()})
            elif len(xs) == 4:
                code.append({'labeldef': xs[0][:-1].upper(),'register1':xs[1],'opcode':'CJMP','jmplabel':xs[3].upper()})
        elif "CONTINUE" in xs:
            if len(xs)>2:
                print("Invalid Instruction")
                return []
            elif len(xs) == 1:
                code.append({'opcode':'CONTINUE'})
            elif len(xs) == 2:
                code.append({'labeldef': xs[0][:-1].upper(), 'opcode': 'CONTINUE'})
    return code

def run_ram_program(registers,code,labels, debug = False):
    pc = 0
    while pc< len(code):
        rec = code[pc]
        if debug:
              print("Executing:", ' '.join(map(str, rec.values())))
        if rec['opcode'] == "INC":
            value = str(rec['register1'])
            registers[value]+=1

        elif rec['opcode'] == "DEC":
            value = rec['register1']
            if registers[value] !=0:
                registers[value] -= 1

        elif rec['opcode'] == "CLR":
            value = rec['register1']
            registers[value] = 0

        elif rec['opcode'] == "MOV":
            register1 = rec['register1']
            register2 = rec['register2']
            registers[register1] = registers[register2]

        elif rec['opcode'] == "UJMP":
            jmplabel = rec['jmplabel']
            pc = labels[jmplabel] - 1

        elif rec['opcode'] == "CJMP":
            jmplabel = rec['jmplabel']
            register1 = rec['register1']
            if registers[register1] == 0:
                pc = labels[jmplabel] - 1

        elif rec['opcode'] == "CONTINUE":
            break

        pc +=1
    return registers        


def main():
    args = sys.argv[1:]
    debugging = False
    fname = ""
    if len(args) == 1:
        fname = args[0]
    elif len(args) == 2 and args[0] == "-d":
        debugging = True
        fname = args[1]
        
    else:
        print("Usage: python3 RAM.py [-d] filename")
        sys.exit(1)
    data = read_data(fname)
    data = remove_comments(data)
    #print(data)
    registers = create_registers(data)
    input_register = create_input_registers(data)
    labels = create_labels(data)
    code = create_code(data)
    #print(labels)

    if debugging:
        print("Input:")
        for key,value in input_register.items():
            print(f'{key} ==> {value}')
        output = run_ram_program(registers,code,labels,debug = True)
        print("\nOutput:")
        print(f'R1 = {output["R1"]}\n')
    else:
        output = run_ram_program(registers,code,labels, debug = False)
        print("Input:")
        for key,value in input_register.items():
            print(f'{key} ==> {value}')
        print("\nOutput:")
        print(f'R1 = {output["R1"]}\n')

if __name__ == "__main__":
    main()
