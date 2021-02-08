import csv
from collections import Counter

with open("heightWeight.csv", newline="")as f :
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data = []

for i in range(len(file_data)):
    n_num = file_data[i][2]
    new_data.append(n_num)

#calculating the mode
data = Counter(new_data)
mode_data_for_range = {
    "70-80": 0,
    "80-90": 0,
    "90-100": 0,
    "100-110": 0,
    "110-120": 0,
    "120-130": 0,
    "130-140": 0,
    "140-150": 0,
    "150-160": 0,
    "160-170": 0,
    "170-180": 0
}
for height,occurence in data.items() : 
    if 70 < float(height) < 80 :
        mode_data_for_range["70-80"] += occurence
    
    elif 80 < float(height) < 90 :
        mode_data_for_range["80-90"] += occurence

    elif 90 < float(height) < 100 :
        mode_data_for_range["90-100"] += occurence
    
    elif 100 < float(height) < 110 :
        mode_data_for_range["100-110"] += occurence

    elif 110 < float(height) < 120 :
        mode_data_for_range["110-120"] += occurence

    elif 120 < float(height) < 130 :
        mode_data_for_range["120-130"] += occurence

    elif 130 < float(height) < 140 :
        mode_data_for_range["130-140"] += occurence

    elif 140 < float(height) < 150 :
        mode_data_for_range["140-150"] += occurence

    elif 150 < float(height) < 160 :
        mode_data_for_range["150-160"] += occurence

    elif 160 < float(height) < 170 :
        mode_data_for_range["160-170"] += occurence

    elif 170 < float(height) < 180 :
        mode_data_for_range["170-180"] += occurence 

mode_range,mode_occurence = 0, 0

for range,occurence in mode_data_for_range.items() :
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])], occurence

mode = float((mode_range[0] + mode_range[1])/2)
print("Mode is " + str(mode))