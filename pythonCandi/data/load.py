
import csv

def load(path, output):
    with open(path) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=';')
        im=0
        for row in csvReader:
            output.append(row)
        im=im+1
    return(output)
 

def loadread(path, output):
    with open(path) as f:
        output = [s for line in f.readlines() for s in line[:-1].split(';')]
        return(output)