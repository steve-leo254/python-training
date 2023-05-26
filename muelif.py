#If we have multiply conditions then If else wont work for us,if elif else.
#It picks the first true one and ignores the other elif.
#Find the grade of the mark below using the below table.
# >= 70 - A
# < 70 and >=60 - B
# < 60 and >=50 - C
# < 50 and >=40 - D
# < 40 - E
marks = 70

if marks >= 70:
    print("A")
elif marks < 70 and marks >= 60:
    print("B")
elif marks < 60 and marks>= 50 :
    print("C")
elif marks < 50 and marks>= 40 :
    print("D")

#take three inputs from a user,separatly.print the largest of the numbers.
#Hint.Determine what type of data is taken in as input

num = int(input("Enter a value1:"))
numtwo =int(input("enter a value2:"))
numthree=int(input("Enter a value3"))

largest_number = max(num,numtwo,numthree)
largest_number1=("The largest number is:",largest_number)
print(largest_number1)

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
num3 = int(input("enter num3: "))

if num1 > num2 and num1 > num3:
    print("num1 is the largest")
elif num2 > num1 and num2 > num3:
    print("num2 is the largest")
else:
    print("num3 is the largest")


