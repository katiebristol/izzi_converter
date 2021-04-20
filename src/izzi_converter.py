# TODO: Improve this script by:
# Making it run every file in /input/ 

import os.path
from os import path

line_number = 0
header = ''
add_header = False

headers = ["specimen", "treatment", "treatment_type", "moment", "dec_s", "inc_s"]


with open("input/I92-2B.txt", "r") as a_file:
    write_file = open('output/' + 'IZZI_I92-2B' + '.txt', 'a+')
    headers = str(headers).replace("'", "").replace(",","").replace("[", "").replace("]","")
    
    write_file.write(str(headers.replace(' ', '\t'))+'\n')
    for line in a_file:
        
        line_number+=1
        next_line = " ".join(line.strip().split())#remove duplicate spaces
        next_line = next_line.replace(" ", ",") #convert spaces to commas

        next_line_array = next_line.split(",")

        if line_number < 6: #still ignore header
            header = header + next_line + '\n'
            continue

        #edit array
        next_line_array = next_line_array[0:7] #cut to 7 items to match header but you can re arrange it all you want
        del next_line_array[3]
        print(next_line_array)
        next_line_array[3] = float(next_line_array[3])*10**-3
        #stop editing the array
        next_line = str(next_line_array).replace("'", "").replace(",","").replace("[", "").replace("]","").replace("Cm","T") #array to string
        write_file.write(str(next_line.replace(' ', '\t'))+'\n') #generic_izzi.txt is like a csv but tabs instead of commas replace space with tab

print("Finished. Cowabunga, dude!")