try:
    f = open('simple.txt', 'r')
    f.write("Test write to simple text")

except IOError:
    print("ERROR: COULT NOT FIND FILE OR READ DATA")

else:
    print("Success")
    f.close()
print('Hello World')
