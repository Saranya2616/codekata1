d = input()
alphabets = digits = special = 0

for i in range(len(d)):
    if(d[i].isalpha()):
        alphabets = alphabets + 1
    elif(d[i].isdigit()):
        digits = digits + 1
    else:
        special = special + 1
print(special)        

        
