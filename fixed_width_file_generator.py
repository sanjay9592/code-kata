import pathlib as pl
def readSpecificationFile(fileName) :
    specs = {}
    with open(fileName, 'r') as file:
        for line in file:  
            fieldVal = line.strip().split(":")
            specs[fieldVal[0].lower()] = fieldVal[1]
    print(specs)
    return specs

def generateFixedWidthFile(data,specs,ouptufile):
    with open(ouptufile, 'w') as file:
        for row in data:
            line = ''
            row_keys = [ key.lower() for key in row.keys()]
            row_dict = dict(zip(row_keys, list(row.values())))
            
            for k, v in specs.items():
                
                if row_dict.get(k) is not None:
                    if(len(row_dict.get(k)) > int(specs[k])):
                        line += row_dict.get(k)[:int(specs[k])]
                    elif(len(row_dict.get(k)) < int(specs[k])):
                        line += row_dict.get(k).ljust(int(specs[k]))
                    else:
                        line +=row_dict.get(k)    
            print(line)
            file.write(line+"\n")   
        

specs = readSpecificationFile("specification.txt")
data = [
    {"Name": "Aliceishappygirl", "Age": "30", "City": "New York"},
    {"Name": "Bob", "Age": "22", "City": "Los Angeles"},
    {"Name": "Charlie", "Age": "25", "City": "Chicago"}
]
outputfile = "final_file.txt"
            
generateFixedWidthFile(data,specs,outputfile)