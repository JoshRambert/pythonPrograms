#Fileref is the name assingned to the file yo want to open and close
#User assigns the name of the fileref 
fileref = open(filename,'r') #Opens a file called filename for reading

fileref = open(filename, 'w') #Opens a file for writing
 
filevariable.close() #Closes the file 

#Iteration and Data files 
qbfile = open("qbdata.txt", "r")

for aline in qbfile:
    values = aline.split() #Splits certain parts of the file for specific use using the 'values' variable
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )

qbfile.close() 

#a differnt way of doing the same function above
qbfile = open("qbdata.txt", "r")

for aline in qbfile:
    values = aline.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10] )

qbfile.close()

#An example of using the writing function
infile = open("qbdata.txt", "r")
outfile = open("qbnames.txt", "w")

aline = infile.readline()
while aline:
    items = aline.split()
    dataline = items[1] + ',' + items[0]
    outfile.write(dataline + '\n')
    aline = infile.readline()

infile.close()
outfile.close() 