task_list=[23,"Jane",(560),["Lesson","Maths",{"currency":"KES"}],987,(76,"John")]

money= task_list[3][2]["currency"]
print(money)

money2 =(task_list[2])
print(money2)


money3 =(task_list[3][1])
print(money3)

task_list[3][2]["amount"] = 90
print(task_list)


#change name john to jane 
updated_tuple =list(task_list[5])
updated_tuple[1] = "Jane"
task_list[5] = tuple(updated_tuple)
print(task_list)


#reverse 987 to 789 without using an inbuilt-method or assigning 789 manualy
  
task_list[4] =int(str(task_list[4])[::-1])
print(task_list)


task_list[4] = str(task_list[-2])
task_list[4]=task_list[4][::-1]
print(task_list[4])




