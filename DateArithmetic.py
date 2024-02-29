import sys
from Date import *

def extract_data(fname):
    celebrity = []
    fname_length = []
    lname_length = []
    with open(fname) as f:
        data = f.read().strip().splitlines()
        for datum in data:
            info = datum.split(":")
            temp_dob = info[2].split("/")
            dob = Date(int(temp_dob[0]),int(temp_dob[1]),int(temp_dob[2]))
            if info[3] == "":
                dod = None
            else:
                temp_dod = info[3].split("/")
                dod = Date(int(temp_dod[0]),int(temp_dod[1]),int(temp_dod[2]))

            celebrity.append([info[0],info[1],dob,dod])
            fname_length.append(len(info[0]))
            lname_length.append(len(info[1]))

    return celebrity,fname_length,lname_length

def main():
    fname = sys.argv[1]
    celebrity_data,fname_length,lname_length = extract_data(fname)
    max_fname = max(fname_length)
    max_lname = max(lname_length)
    days = []
    bad_data = []

    for celebrity in celebrity_data:
        dob = celebrity[2]
        dod = celebrity[3]
        day_of_birth = dob.day_of_weekS()
        if dod != None:
            day_of_death = dod.day_of_weekS()
            n = dob.days_between(dod)
        else:
            day_of_death = "ALIVE"
            n = dob.days_between(dob.today())

        celebrity.append(day_of_birth)
        celebrity.append(day_of_death)

        if n > 0:
            celebrity.append(n)
            days.append(n)
        else:
            bad_data.append(celebrity)
            
    for element in bad_data:
        celebrity_data.remove(element)
    
    days.sort()
    final_data = []
    for i in range(len(days)):
        for j in celebrity_data:
            if j[-1] == days[i] and not j in final_data:
                final_data.append(j)
                break

    print("BAD DATA: ", end="")
    for element in bad_data:
        print(f"{element[0]}:{element[1]}:{element[2].month}/{element[2].day}/{element[2].year}:{element[3].month}/{element[3].day}/{element[3].year}")
        print()

    print(f"%-{max_fname}s %-{max_lname}s %-18s %-9s %-18s %-9s %-8s" % ("FNAME","LNAME","DOB","DAY","DOD","DAY","NUM_DAYS"))
    print("-"*(max_fname + max_lname + 18 + 9 + 18 + 9 + 8 + 6))
    for final_celeb in final_data:
        print(f"%-{max_fname}s %-{max_lname}s %-18s %-9s %-18s %-9s %-8d" % (final_celeb[0],final_celeb[1],final_celeb[2],final_celeb[4],final_celeb[3],final_celeb[5],final_celeb[6]))
    print("-"*(max_fname + max_lname + 18 + 9 + 18 + 9 + 8 + 6))

if __name__ == "__main__":
    main()
