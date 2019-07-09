d=str(input());
if ((d>='a') & (d<='z')or (d>='A') & (d<='Z')): 
    if d=='a'or d=='e'or d=='i'or d=='o'or d=='u'or d=='A'or d=='E'or d=='I'or d=='O'or d=='U':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
