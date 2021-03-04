import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import QuickSort

array = [8,7,6,5,0,1,2,3,4];
index = QuickSort(array, 0, len(array) - 1);

addresult = ""
for i in range(len(array)):
    addresult = addresult+" "+str(array[i])

ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
