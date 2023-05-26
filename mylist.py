#list
#list is a data container that holds more than 1 variable.They need not be of the same Datatype
person = ["John Doe",30,"john@mail","Nairobi"]
person = person[3]
print(person)

days =["monday","tuesday","wednesday","thursday","friday","satraday","sunday"]
days = days[1]
print(len(days))
print(days)

# + = concatenate two list(combining) 
mylist = days + days
print(mylist)
print(len(mylist))

#repetition
mylist = days * 4
print(mylist)
print(len(mylist))

days =["monday","tuesday","wednesday","thursday","friday","satraday","sunday"]
#days3 =days [2:5]
#print(days3)
 
#del days[0]
#print(days)

days[3] = "thru"
print(days)
days.append
days.extend(["son","jon"])

print(days)



