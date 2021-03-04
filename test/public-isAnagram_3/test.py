import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..')))

from p0 import isAnagram

ofile = open('output', 'w')
ofile.write(str(isAnagram("RAMPET123456", "")))
ofile.close()
