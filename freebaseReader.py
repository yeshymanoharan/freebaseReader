with open("aptamerbase.freebase.extract.nt") as fileobject:
    result = open("result.txt", 'w')
    
    for line in fileobject:
        try:
            if (line.split()[1].split('/')[4].split('.')[3]== "sequence>"):
                if(line.split()[2] != "\"n/a\""):
                    result.write(line.split()[2] + '\n')
        except:
            pass