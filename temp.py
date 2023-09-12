#! /usr/bin/python
TEMP_PATH="/sys/class/thermal/thermal_zone0/"

def readTemp():

    fo = open(TEMP_PATH + "temp" , "r")
    temp = fo.read()
    return int(temp)*0.001
 
print(readTemp())
