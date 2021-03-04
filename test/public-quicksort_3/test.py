import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import QuickSort

array = [100002,1000000,0,0,0,0,99,999,9901,9932,8,7,6,5,0,1,2,3,4,5,6,7,8,9,10,11,100,10000, 100002,1000000,0,0,0,0,99,999,9901,9932,8,7,6,5,0,1,2,3,4,5,6,7,8,9,10,11,100,10000, 100002,1000000,0,0,0,0,99,999,9901,9932,8,7,6,5,0,1,2,3,4,5,6,7,8,9,10,11,100,10000, 999,767,543,555,678,890];
index = QuickSort(array, 0, len(array) - 1);

addresult = ""
for i in range(len(array)):
    addresult = addresult+" "+str(array[i])

ofile = open('output', 'w')
ofile.write(addresult)
ofile.close()
