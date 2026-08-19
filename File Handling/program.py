# add 1 to Numbers in output.txt file
file = None
try:
    open("output.txt", 'w')
    n = 10
    for num in range(1, n+1):
        file.write(str(num)) 
except:
    print("Something Wrong")
finally:
    if file is not None:
        file.close()