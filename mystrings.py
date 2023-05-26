#strings are alphanumeric characters. Alphabets and numbers and characters. UTF8
#Certain operations are done on strings only
#1Converting casing
#2Splitting values
#3.count the number of times a word appears
#...etc
#to access these operations or methods we use a .after the variable name.

first_name ="Leo"
first_name =first_name.lower()
#print(first_name)

last_name=" doe "
last_name=last_name.strip()



email = "     Mail2@Mail.com"
email = email.strip().lower()
#print(email.count("m"))

mypara ="the day has started well. i woke up at 5. My schedule is packed"
#mysent = mypara.split(".")
#print(type(mysent))

#mypara2 = "the day has ended well. i went back home at 6. Ate my supper and went back to sleep "

#indexing is accesing a character in a variable by counting starting from 0
#myname = "John Doe"
#print(myname[2])
 
#Slicing is when you want to access multiple characters  in a variable
#First part is using the index of where to start
#Second part is the count of where to stop
#print(myname[0.4])

#Display Doe using slicing. Try with both negative and positive numbers
myname = "John Doe"
print(myname[0:5])
print(myname[0:3])

#function = a reusable piece of code that carries out a task
#space is considered as a character

#len  = length of a string 
#len(course)

course ="Pthyon programming"
print (len(course))
print(course[0]) #0 means first character which is p
print(course[-1])
print(course[0:3]) 


myname = "John Doe"
print(len(myname))
print(myname[2])
print(myname[-1])#when strating from left you start with negative undlike from the positive side
print(myname[0:3]) 


#\" used to escape double quote character
#others include #\'
#\n new line

myname ="John \"programmer" 
print(myname)

myname = "John \'programmer"
print(myname)

myname ="John \\programmer"
print(myname)
#print(len(myname))

#combine both str use {}{}
first = "John"
last = "programmer"
full = f"{first}{last}"
full =f"{len(first)}{last}"
print(full)
#lengh of the str


myname = "John programmer"
print(myname.upper())

print(myname.lower())
print(myname.title())
print(myname.rstrip())

#find = returns the index of these characters in our string 
print(myname.find("pro")) 
print(myname.replace("o","j"))
print("swift" not in myname)
#bolian is a true or false statment
print("joh" in myname) 


myname = "John Doe"
print(myname[0:5])
print(myname[0:3])
print(myname[-3:])