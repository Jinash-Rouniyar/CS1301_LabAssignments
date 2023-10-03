import sys

def read_data(fname):
    with open(fname) as f:
        data = f.read().splitlines()
        f.close()
        return data
    
def menu():
    print("\n(s) Standings")
    print("(t) Team results")
    print ("(q) Quit\n")
    user_input = str(input("What do you want to see: "))
    return user_input

def extract_data_parts(data):
    new_list = []
    for datum in data:
        filtered_list = datum.split(":")
        new_list.append(filtered_list)
    return new_list
def calculate_team_standings(g1data,team_code):
    wins = 0
    loss = 0
    tie = 0
    team_specific_data = []
    for records in g1data:
        if records[1] == team_code or records[2] == team_code:
            team_specific_data.append(records)
    
    for data in team_specific_data:
        if data[3] == data[4]:
            tie = tie+1
        else:
            if data[1] == team_code and int(data[3])>int(data[4]):
                wins = wins +1
            elif data[1] == team_code and int(data[4])>int(data[3]):
                loss = loss + 1
            if data[2] == team_code and int(data[4])>int(data[3]):
                wins = wins +1
            elif data[2] == team_code and int(data[3])>int(data[4]):
                loss = loss +1
    return wins,loss,tie

def standings(t1_data,g1_data):
    temp_data = []
    final_records = []
    for teams in t1_data:
        team_code = str(teams[1])
        wins,loss,tie = calculate_team_standings(g1_data,team_code)
        percent = (wins+(tie*0.5))/(wins+loss+tie)
        percent = round(float(percent),3)
        temp_data = [team_code,wins,loss,tie,percent]
        final_records.append(temp_data)
    return final_records

def calculate_team_results(g1_data, team_code):
    record = []
    for games in g1_data:
        if games[1] == team_code or games[2] == team_code:
            record.append(games.copy())  # Create a copy of the game data to avoid modifying the original

    # Adding "at" to separate home and away games
    for specific_games in record:
        if specific_games[1] != team_code and "at" not in specific_games[1]:
            specific_games[1] = "at " + specific_games[1]

    # Add a new column for win/loss/tie
    for data in record:
        if data[3] == data[4]:
            data.append("TIE")
        else:
            if data[1] == team_code and int(data[3]) > int(data[4]):
                data.append("WIN")
            elif data[1] == team_code and int(data[4]) > int(data[3]):
                data.append("LOSS")
            elif data[2] == team_code and int(data[4]) > int(data[3]):
                data.append("WIN")
            elif data[2] == team_code and int(data[3]) > int(data[4]):
                data.append("LOSS")
    return record
    
def team_results(t1_data,g1_data,team_code):
    win,loss,tie = calculate_team_standings(g1_data,team_code)
    flag=0
    final_record = calculate_team_results(g1_data,team_code)
    for teams in t1_data:
        if team_code == str(teams[1]):
            print("Team: ",teams[0],"\n")
            flag = 1
    if flag==0: 
        print("Invalid team code:")
    else:
        print("{:>10s}{:>10s}{:>4s}{:>6s}{:>7s}".format("DATE","OPPONENT","US","THEM","RESULT")) 
        for records in final_record:
            if records[1] == team_code:
                print("{:>10s}{:>10s}{:>4s}{:>6s}{:>7s}".format(records[0],records[2],records[3],records[4],records[5]))
            else:
                print("{:>10s}{:>10s}{:>4s}{:>6s}{:>7s}".format(records[0],records[1],records[4],records[3],records[5]))
        print(f"\nOverall Record: {win}-{loss}-{tie}")
def main():
    dname = sys.argv[1]
    tname = dname + "/teams.dat"
    gname = dname + "/games.dat"
    teams_data = read_data(tname)
    games_data = read_data(gname)
    t1_data = extract_data_parts(teams_data)
    g1_data = extract_data_parts(games_data)

    while True:
        user_input = str(menu()).lower()
        if user_input == "s":
            final_record = standings(t1_data,g1_data)
            final_record.sort(key=lambda x: x[4], reverse=True)
            print("{:12s}{:>5s}{:>7s}{:>7s}{:>8s}".format("TEAM","WINS","LOSSES","TIES","PERCENT"))
            print("----------","------","------","------","-------")
            for records in final_record:
                print("{:0s}{:>14d}{:>7d}{:>7d}{:7.3f}".format(records[0],records[1],records[2],records[3],records[4]))

        elif user_input == "t":
            team_code = str(input("Enter team code (e.g. ARI, ATL, CHC, CLE, STL): "))
            team_results(t1_data,g1_data,team_code.upper())
        elif user_input == "q":
            break
        else:
            print("Wrong input. Please try again(s/t/q)")
        
if __name__ == "__main__":
    main()






