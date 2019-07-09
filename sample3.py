b=str(input());
if ((b>='a') & (b<='z')or (b>='A') & (b<='Z')): 
    if b=='a'or b=='e'or b=='i'or b=='o'or b=='u'or b=='A'or b=='E'or b=='I'or b=='O'or b=='U':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
