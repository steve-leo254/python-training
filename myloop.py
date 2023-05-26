#Loop is used to get values from inside a data structure like a lost
#or tuple.
#if i want to repeat a task 10 times i will store num one - 10 (i will store num 1 - 10 in a list then
#looop through that list. In the body of the loop you can execute any other code 
#Like IF, indexing, Slicing, access oprations or methods or a loop.)

# ls1 = list(range(0,10))
# for i in ls1:
#      if  i%3 == 0:
#       print(i)
#only display numbers divisible by 3

#Display only city that have letter a
ls1=["Nairobi","Mombasa","Kisumu","Nakuru","Eldoret"]
res =[]

for city in ls1:
    if "a" in city.lower():
      res.append(city)
print(res)