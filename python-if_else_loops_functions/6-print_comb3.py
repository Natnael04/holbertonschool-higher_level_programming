#!/usr/bin/python3
for i in range(1, 89):
  if i % 10 != 0 and i % 11 != 0:
    if i < (i % 10) * 10 + i // 10:
      print("{:02d}".format(i), end=', ')
    
print("89")