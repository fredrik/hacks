import fileinput

for line in fileinput.input():
  print "'{}'".format(line)

