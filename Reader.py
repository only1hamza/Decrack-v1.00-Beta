def reader()
    string1 = '0200='
    file = open(r"C:\Users\21262\Desktop\Project Programme Python\2022A03.P", "r")
    flag = 0
    index = 0
    for line in file:  
        index + = 1 
        if string1 in line:
            file.readlines(index)
            print(string1[5::])
            break 
    
    
    
    flie.close()
    