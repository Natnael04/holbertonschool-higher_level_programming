#!/usr/bin/python3
for i in range(1, 90):
  if i % 10 != 0 and i % 11 != 0:
    if i < (i % 10) * 10 + i // 10:
      print("{:02d}".format(i), end=', ')
    
print("{:02d}\n".format(i), end=' ')