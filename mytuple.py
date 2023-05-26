days = ("Mon", "tue", "Wed", "Thur", "Fri", "Sat", "Sun")
days2= days[2:5]
print(days2)
t = list(days)
t[5]="Saturday"
days=tuple
print(days)
print(t)

#repetition
tuple1 = ('a', 'b')
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: ('a', 'b', 'a', 'b', 'a', 'b')

#
my_tuple = (1, 2, 3, 'a', 'b', 'c')
print(len(my_tuple))  # Output: 6

task_list=[23,"Jane",(560),["Lesson","Maths",{"currency":"KES"}],987,(76,"John")]
no = 987
r_no = 0
r_no = (r_no * 10) + (no % 10)
no = no // 10
r_no = (r_no * 10) + (no % 10)
no = no // 10
r_no = (r_no * 10) + (no % 10)
print(r_no)



#Display Doe using slicing. Try with both negative and positive numbers
#myname = "John Doe"
#print(myname[0:5])
#print(myname[0:3])

