import re
import numpy
lines = []
c = 0
with open('result.txt') as f:
    lines = f.readlines()

def getError(txt, regex):
    x = re.match(regex, txt)
    if  x:
        global c
        c = c+1
        print("Fehler\t"+str(c)+":\t"+txt)

for line in lines:
    x = re.match("NOK", line)
    if x:
        print(x)
    