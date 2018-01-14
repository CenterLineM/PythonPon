#-------------------------------------------------------------------------------
# Name:        數字系統運算
# Purpose:
#
# Author:      JovElien
#
# Created:     22/07/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print "OK"

    x=1
    y=0
    sumOR = x or y
    print sumOR
    z=1
    sumIF = x if y else z
    print sumIF
    sumT = x <> y
    print sumT
    x1 = 456
    y1 = 145
    sumBit = x1 & y1
    print sumBit

    pass

if __name__ == '__main__':
    main()
