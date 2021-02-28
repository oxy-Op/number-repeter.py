import time as t

print("\n Enter What You Want Me To Call You ")
g = str(input())
print("\n Hello " + str(g) + "\nWelcome To Oxy Py Program")
t.sleep(2)
print("\n Do You Want to Use Our Tool" + " Type [Y] or [n]")
var = input()

if var != "Y":
  print("Program Finished")
  exit()
else:
  t.sleep(1)
  print("\n")
t.sleep(1)
print("\n Select numbers between 1 to 10^10")
b= int(input())
t.sleep(1)
print("Checking...")
t.sleep(1)
i = 1
while i <= b:
  print(i)
  i = i +1
t.sleep(2)

print("Finished")
t.sleep(2)
print("You Can Contact Me:) https://alphaoxyop.wordpress.com/contact/")
t.sleep(3)
print("To Restart Type python repeater.py")
exit()