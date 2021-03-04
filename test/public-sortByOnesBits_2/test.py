import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import sortByOnesBits


array = sortByOnesBits([4096,8192,1,1024,2,512,256,128,64,32,16,8,4, 2048])

addresult = ""
for i in range(len(array)):
    addresult = addresult+" "+str(array[i])

ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
