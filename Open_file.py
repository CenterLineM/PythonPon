__author__ = 'Administrator'
f = open('data.txt', 'w')
f.write('Hello\n')
f.write('Cpmputer\n')
f.close()

f  = open('data.txt')
bytes = f.read()
bytes
print bytes
bytes.split()