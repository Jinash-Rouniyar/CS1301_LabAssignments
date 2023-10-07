import sys

def read_data(fname):
    with open(fname) as f:
        data = f.read().splitlines()
        f.close()
        return data
    
def extract_data_parts(data):
        new_list = []
        for datum in data:
            filtered_list = datum.split(" ")
            new_list.append(filtered_list)
        return new_list  
def convert_str_list(s):
    result = []
    xs = s.split(",")
    for x in xs:
        ys = x.split(":")
        result.append((int(ys[0]), int(ys[1])))
    return result

def dict_to_list(d):
    result = []
    for x in d:
        result.append((d[x], x))
    return result

def convert_str_dict(s): 
    d = {}
    xs = s.split(",")
    for info in xs:
        y = info.split(":")
        if y[1] not in d:
            d[y[1]] = int(y[0])
        else:
            d[y[1]] += int(y[0])
    return d

def organize_data(list_of_data):
    list = []
    for datum in list_of_data:
            dict = {"operation": datum[0]}
            for i in range(1,len(datum)):
                dict["value" + str(i)] = datum[i]
            list.append(dict)  
    return list

def add(data):
        String_data = ""
        for i in range(1,len(data)):
            String_data = String_data + str(data["value" + str(i)]) + ","
            dict = convert_str_dict((String_data[:len(String_data)-1]))
        return dict
def format_output(list):
    output = ""
    flag = 0
    for data in list:
        if flag ==1 and data[0]>0:
            output += " + "
            flag=1
        elif flag == 1 and data[0]<0:
            output += " - "
        if int((data[0]))>1 or int((data[0]))<-1:
            if(int(data[1]))>1:
                if(data[0]>0) or flag == 1:
                 output +=str(abs(data[0])) + "x^" + str(data[1]) 
                else:
                    output +=str((data[0])) + "x^" + str(data[1])
            if(int(data[1]))==1:
                output += str(abs(data[0])) + "x" 
            if(int(data[1]))==0:
                output += str(abs(data[0])) 
            flag = 1
        if int((data[0]))==1:
            if(int(data[1]))>1:
                output += "x^" + str(data[1]) 
            if(int(data[1]))==1:
                output += "x" 
            if(int(data[1]))==0:
                output += "1" 
            flag = 1
    return output   

def multiply(input1,input2):
     result = {}
     for t1 in input1:
          for t2 in input2:
            new_term = (t1[0] * t2[0], t1[1] + t2[1])
            if new_term[1] not in result:
                result[new_term[1]] = new_term[0]
            else:
                result[new_term[1]] += new_term[0]
     return dict_to_list(result)

def list_to_string(list):
    output = ""
    for data in list:
        output += str(data[0]) + ":" + str(data[1]) + ","
    return output[:-1]

def write_data_file(s,t):
    with open("poly_answers.dat",t) as f:
      f.writelines(s + "\n") 
      f.close()

def main():
    flag = 0
    fname = sys.argv[1]
    data = read_data(fname)
    list_of_data = extract_data_parts(data)
    organized_list = organize_data(list_of_data)
    for data in organized_list:
        if data["operation"] == "add":
            input1 = convert_str_list(data["value1"])
            input2 = convert_str_list(data["value2"])
            input1.sort(reverse = True, key=lambda x: x[1])
            input2.sort(reverse = True, key=lambda x: x[1])
            sum = add(data)
            final_list =  dict_to_list(sum)
            final_list.sort(reverse = True, key=lambda x: x[1])
            formatted_input1 = format_output(input1)
            formatted_input2 = format_output(input2)
            formatted_sum = format_output(final_list)
            print(f'( {formatted_input1} ) + ( {formatted_input2} ) =  {formatted_sum}')
            output_string1 = list_to_string(final_list)
            if flag == 0:
                write_data_file(output_string1,"w")
                flag =1
            else:
                write_data_file(output_string,"a")
        elif data["operation"] == "mul":
            input1 = convert_str_list(data["value1"])
            input2 = convert_str_list(data["value2"])
            input1.sort(reverse = True, key=lambda x: x[1])
            input2.sort(reverse = True, key=lambda x: x[1])
            product = multiply(input1,input2)
            formatted_input1 = format_output(input1)
            formatted_input2 = format_output(input2)
            formatted_product = format_output(product)
            print(f'( {formatted_input1} ) * ( {formatted_input2} ) =  {formatted_product}')
            output_string = list_to_string(product)
            if flag == 0:
                write_data_file(output_string1,"w")
                flag =1
            else:
                write_data_file(output_string,"a")

if __name__ == '__main__':
    main()
