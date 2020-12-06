# Print the first 20 prime numbers
start = 1
end = 20
for i in range(start,end):
    if i > 1:
        for k in range(2,i):
            if(i == k):
                break
        else:
            print(i)
