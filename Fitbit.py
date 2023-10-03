import sys
import math
def read_data(fname):
  with open(fname) as f:
        data = f.read().splitlines()
        f.close()
        return data
  
def remove_comment_lines(data):
    new_data = []
    for line in data:
        if "#" not in line:
            new_data.append(line)
    return new_data

def extract_data_parts(data):
   new_list = []
   for lines in data:
       filtered_data = lines.split(":") 
       new_list.append(filtered_data)
   
   for time in new_list:
       time[0] = int(generate_minutes_since_midnight(time[0]))
       time[1] = int(generate_minutes_since_midnight(time[1]))
       time[2] = int(time[2])

   return new_list

def generate_minutes_since_midnight(time):
      time = time.upper()
      hours = int(time[0:int(time.index("."))])
      if "AM" in time:
          mins = int(time[int(time.index(".")+1):int(time.index("A"))])
          if hours!=12:
              hours = hours*60
          else:
              hours = 0
          total_time = int(hours + mins)
          return total_time
      if "PM" in time:
          mins = int(time[int(time.index(".")+1):int(time.index("P"))])
          if hours!=12:
              hours = (hours+12)*60
        
          else:
              hours = 12*60
          total_time = int(hours + mins)
          return total_time
      
def remove_bad_data(output_data):
    bad_data = []
    for date in output_data:
        if(date[0]>=date[1]):
            output_data.remove(date)
            bad_data.append(date)
    return output_data,bad_data

def compute_stats(data):
    total_steps = 0
    minutes = 0
    for steps in data:
        total_steps = total_steps + steps[2]
        minutes = minutes + int(steps[1]-steps[0])
    print("Total Steps:", total_steps)
    hours = minutes/60
    print("Hourly Step Rate:", math.floor(total_steps/hours))

def convert_triple_to_string(bad_data):
        hours = int(bad_data//60)
        mins = int(bad_data%60)
        if hours<12:
            time = "AM"
        else:
            time = "PM"
        if hours>12:
            hours-=12
        elif hours == 0:
            hours = 12
        return f"{hours:02d}:{mins:02d}{time}"

def main():
    fname = sys.argv[1]
    data = read_data(fname)
    data1 = remove_comment_lines(data)
    data2 = extract_data_parts(data1)
    data3, bad_data = remove_bad_data(data2)
    for entry in bad_data:
        first_part = convert_triple_to_string(entry[0])
        second_part = convert_triple_to_string(entry[1])
        print("Invalid Data: "+ str(first_part)+":"+str(second_part)+":"+str(entry[2]))
    compute_stats(data3)
    
if __name__ == "__main__":
    main()


