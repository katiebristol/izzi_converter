import os.path
from math import pi
from os import path
from pathlib import Path

headers = ["specimen", "treatment", "treatment_type", "moment", "dec_s", "inc_s"]
headers = " ".join(headers)
rootPath = Path('./input')
inputList = [e for e in os.listdir(rootPath) if not os.path.isdir(e)]
for currentInput in inputList:
    line_number = 0
    header = ''
    add_header = False
    with open('./input/' + currentInput, "r") as a_file:
        write_file = open('output/' + currentInput, 'a+')
        write_file.write(str(headers.replace(' ', '\t'))+'\n')
        for line in a_file:
            line_number+=1
            next_line = " ".join(line.strip().split()) #Remove duplicate spaces
            next_line = next_line.replace(" ", ",") #Convert spaces to commas

            next_line_array = next_line.split(",")
            
            if line_number < 6: #Ignore header lines (lines 0-5)
                 continue
            try:
                #Remove excess columns
                del next_line_array[3] #Delete CD column
                next_line_array = next_line_array[0:6] #Remove trailing columns

                next_line_array[3] = float(next_line_array[3])*25/pi #Convert from Oe to A/m (Cryo assumes 10cc vol.)
                next_line = " ".join(str(x) for x in next_line_array).replace("Cm","T") #Array to string, replacing Cm with T
                write_file.write(str(next_line.replace(' ', '\t'))+'\n') #output format is tab-delimited
            except IndexError:
                print("Index out of range error on this:")
                print(next_line_array)
print("Conversion finished. Check the /output/ folder for your converted files. ")
