import csv
filename1 = "pitch_arsenals.csv"
filename2 = "strikeout_percentage.csv"

database = {}

with open(filename1, 'r') as file_in:
    file_in.readline()
    csv_reader = csv.reader(file_in)
    
    for line in csv_reader:
        unparsed_name = line[0]
        name_list = unparsed_name.split()
        full_name = name_list[1] + ' ' + name_list[0][:-1]

        fastball_speed = line[2]
        sinker_speed = line[3]
        
        if fastball_speed == "":
            fastball_speed = sinker_speed
        
        try:
            database[full_name] = [fastball_speed]
        except KeyError:
            pass

       
with open(filename2, 'r') as file_in:
    file_in.readline()
    csv_reader = csv.reader(file_in)
    for line in csv_reader:
        name = line[1]
        if name[-1] == "*":
            name = name[:-1]

        so_percent = line[10]
        
        
        try:
            database[name].append(so_percent)
        except KeyError:
            pass

with open('baseball_data.csv' , 'w') as file_out:
    csv_writer = csv.writer(file_out)
    write_lines = []
    for i in database:
        write_line = []
        if len(database[i]) < 2:
            pass
        else:
            pitch_velocity = database[i][0]
            strikeout_percent = database[i][1]

            temp_line = [pitch_velocity, strikeout_percent]
            write_lines.append(temp_line)
    csv_writer.writerows(write_lines)


        
        
