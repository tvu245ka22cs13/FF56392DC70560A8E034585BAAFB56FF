# leap year
print("enter the year:")
y = int(input())
if y % 4 == 0 and y % 100 != 0:
  print("/n it is a leap year")
elif y % 400 == 0:
  print("/n it is a leap year")
else:
  print("/n it is not a leap year")
