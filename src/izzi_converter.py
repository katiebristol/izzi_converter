import os.path
from os import path
from pathlib import Path

headers = ["specimen", "treatment", "treatment_type", "moment", "dec_s", "inc_s"]
rootPath = Path('./input')
inputList = [e for e in os.listdir(rootPath) if not os.path.isdir(e)]
for currentInput in inputList:
    line_number = 0
    header = ''
    add_header = False
    with open('./input/' + currentInput, "r") as a_file:
        write_file = open('output/' + currentInput, 'a+')
        headers = str(headers).replace("'", "").replace(",","").replace("[", "").replace("]","")
        
        write_file.write(str(headers.replace(' ', '\t'))+'\n')
        for line in a_file:
            line_number+=1
            next_line = " ".join(line.strip().split()) #Remove duplicate spaces
            next_line = next_line.replace(" ", ",") #Convert spaces to commas

            next_line_array = next_line.split(",")
            
            
            if line_number < 6: #Still ignore header
                header = header + next_line + '\n'
                continue

            try:
                #Edit array
                next_line_array = next_line_array[0:7] 
                del next_line_array[3]
                print(next_line_array)
                next_line_array[3] = float(next_line_array[3])*10**-3
                #stop editing the array
                next_line = str(next_line_array).replace("'", "").replace(",","").replace("[", "").replace("]","").replace("Cm","T") #Array to string
                write_file.write(str(next_line.replace(' ', '\t'))+'\n') #generic_izzi.txt is like a csv but tabs instead of commas replace space with tab
            except IndexError:
                print("Index out of range error on this:")
                print(next_line_array)
print("Conversion finished. Check the /output/ folder for your converted files. ")
