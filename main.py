print("welcome to my computer quiz!")
sire = input("Do you want to continue with this quiz? (yes or no) ")

if sire != "yes":
    quit()

print("Okay! Let's continue :)")
score = 0
q1 = input("What is the most widely used programming language? ")
if q1 == "Python":
    print("correct!")
    score = score+1
else:
    print("incorrect!")


q2 = input("This is the on-screen work area on which windows, icons, menus, and dialog boxes appear. ")
if q2 == "desktop":
    print("correct!")
    score = score+1
else:
    print("incorrect!")


q3 = input("The physical components of a computer are called ____ ")
if q3 == "hardware":
    print("correct!")
    score = score+1
else:
    print("incorrect!")


q4 = input("The bar in the bottom of a window is called the ____ bar ")
if q4 == "Task":
    print("correct!")
    score = score+1
else:
    print("incorrect!")

q5 = input("The Full form of CD is: ")
if q5 == "Compact Disc":
    print("correct!")
    score = score+1
else:
    print("incorrect!")

strscore = str(score)
print("Thank you for playing my quiz :) your score is: "+strscore+"/5")
