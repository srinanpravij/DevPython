# Compute Tutions till double

year = 0
tutions = 10000
for i in year:
    newTutions = tutions * 1.07
    print(newTutions)
    year+=1
    if(newTutions == (tutions * 2)):
        print("It took {} years".format(year))
    else:
        exit()



