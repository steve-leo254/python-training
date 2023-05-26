# Task 1
# base = float(input("Enter the base:",))
# height = float(input("Enter the Height:",))
# area = 0.5 * base * height
# print("The area of the triangle is",area)

# Task 2
# num = int(input("Enter a num:"))
# if num % 2 == 0:
#     print("The num is even.")
# if num % 4 == 0:
#     print("The num is divisible by 4")
# else:
#     print("The num is odd")

# Task 3
# phone_number = input("Enter a phone number: ")

# if phone_number.startswith("+254"):
#     print("Phone number is already in the correct format.")
# else:
#     if phone_number.startswith("07"):
#         phone_number = "+254" + phone_number[1:]
#     elif phone_number.startswith("71"):
#         phone_number = "+254" + phone_number[1:]
#     elif phone_number.startswith("254"):
#         phone_number = "+254" + phone_number[3:]
#     elif phone_number.startswith("01"):
#         phone_number = "+254" + phone_number[1:]
#     else:
#         print("Invalid phone number format.")
#         exit()

#     print("Converted phone number:", phone_number)

# Task 4
# def validate_email(email):
#     if "@" in email and "." in email:
#         valid_email = True
#     else:
#         valid_email = False

#     if valid_email:
#         print("Valid email address")
#     else:
#         print("Invalid email address")


# email = input("Enter an email address: ")

# validate_email(email)

# Task 5
# num = float(input("Enter the first number: "))
# num1 = float(input("Enter the second number: "))
# num2 = float(input("Enter the third number: "))
# largest = num
# if num1 > largest:
#     largest = num1
# if num2 > largest:
#     largest = num2
# print("The largest value is:", largest)

# Task 6
# password = "admin@123"
# attempts = 4
# while attempts > 0:
#     user_passcode = input("Enter the password:")
#     if user_passcode == password:
#         print("Access grandted.")
#         break
#     else:
#         attempts-=1
#         print("Incorrect password.Attempts left:",attempts)
#         if attempts == 0:
#             print("Account blocked.")

# Task 7 50,40 els
# marks = float(input("Enter the student marks(between 0 and 100): "))
# if marks > 100 or marks < 0:
#     grade ="Invalid"
# elif marks >=80:
#     grade = "A"
# elif marks >=60:
#     grade = "B"
# elif marks >=50:
#     grade = "C"
# elif marks >=40:
#     grade = "D"
# else:
#     grade = "E"
# print("Grade:",grade)

# Task 8
# speedkms = float(input("Enter the cars's speed:"))
# if speedkms <70:
#     print("Ok")
# else:
#     demerit_points=(speedkms-70)//5
#     if demerit_points >12:
#         print("License suspended")
#     else:
#         print("License suspended")

# Task9
# rows = int(input("Enter the number of rows: "))

# for i in range(1, rows + 1):
#    print("*" * i)

# Task10
# prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]

# total_stock = 0
# for product in prods:
#    stock = int(product[2][-1])
#    total_stock += stock

# print("Total stock in the company:", total_stock)

# Task11
# import datetime

# def calculate_age(date_of_birth):
#     today = datetime.date.today()
#     age = today.year - date_of_birth.year
#     if today.month < date_of_birth.month or (today.month == date_of_birth.month and today.day < date_of_birth.day):
#         age -= 1

#     if today.month > date_of_birth.month:
#         months = today.month - date_of_birth.month
#     elif today.month < date_of_birth.month:
#         months = 12 - (date_of_birth.month - today.month)
#         age -= 1
#     else:
#         months = 0

#     if today.day >= date_of_birth.day:
#         days = today.day - date_of_birth.day
#     else:
#         months -= 1
#         if months == -1:
#             months = 11
#         last_month = today.month - 1 if today.month > 1 else 12
#         _, last_day = monthrange(today.year, last_month)
#         days = last_day - (date_of_birth.day - today.day)

#     return age, months, days

# year = int(input("Enter the year of birth (YYYY): "))
# month = int(input("Enter the month of birth (MM): "))
# day = int(input("Enter the day of birth (DD): "))

# date_of_birth = datetime.date(year, month, day)
# age, months, days = calculate_age(date_of_birth)

# print("Age: {} years, {} months, {} days".format(age, months, days))

#Task 12
# num = float(input("Enter the first number:"))
# num2 = float(input("Enter the second number:"))
# num3 = float(input("Enter the third number:"))
# num4 = float(input("Enter the fourth number:"))

# largest= max(num,num2,num3,num4)
# largest_number1 =("The largest number is",largest)
# print(largest_number1)

#Task 13
# attempts = 3

# while attempts > 0:
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")

#     if email == "admin@mail.com" and password == "Admin@123":
#         print("Login is Successful")
#         break
#     else:
#         attempts -= 1
#         print("Invalid username or password. Attempts remaining:", attempts)

# if attempts == 0:
#     print("You have been blocked.")

#Task 14
#def get_valid_number(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             return value
#         except ValueError:
#             print("Invalid character entered. Please enter a valid number or float.")

# num1 = get_valid_number("Enter the first number: ")
# num2 = get_valid_number("Enter the second number: ")

# result = num1 + num2

# print("The sum is:", result)

#Task 15
def calculate_nhif(gross_salary):
    if gross_salary < 6000:
        nhif_contribution = 150
    elif gross_salary < 8000:
        nhif_contribution = 300
    elif gross_salary < 12000:
        nhif_contribution = 400
    elif gross_salary < 15000:
        nhif_contribution = 500
    elif gross_salary < 20000:
        nhif_contribution = 600
    elif gross_salary < 25000:
        nhif_contribution = 750
    elif gross_salary < 30000:
        nhif_contribution = 850
    elif gross_salary < 35000:
        nhif_contribution = 900
    elif gross_salary < 40000:
        nhif_contribution = 950
    elif gross_salary < 45000:
        nhif_contribution = 1000
    else:
        nhif_contribution = 1100

    return nhif_contribution

basic_salary = float(input("Enter the basic salary: "))
benefits = float(input("Enter the benefits: "))

gross_salary = basic_salary + benefits


nhif = calculate_nhif(gross_salary)

print("Gross Salary: ", gross_salary)
print("NHIF Contribution: ", nhif)



#Quiz

# user_input = input("Enter a number between 0 and 100: ")
# #valitating input
# try:
#     # Converting the input to an integer
#     number = int(user_input)

#     # Checking if the number is between 0 and 100
#     if number >= 0 and number <= 100:
#         # Comparing the number to 50 and printing the result
#         if number > 50:
#             print("Pass")
#         else:
#             print("Fail")
#     else:
#         print("Invalid")
# except ValueError:
#     print("Invalid input. Please enter a valid number.")

#valitating a number
# def validate_number(input_number):
#     try:
#         number = float(input_number)  

#         if number < 0 or number > 100:
#             return False

#         return True
#     except ValueError:
#         return False
    
# user_input = input("Enter a number between 0 and 100: ")
# if validate_number(user_input):
#     print("Valid number!")
# else:
#     print("Invalid number!")


#T
# User_input= int(input("Enter the number:"))
# if 0 <= User_input <=100:
#     if User_input >=50:
#         print("Pass")
#     else:
#         print("Fail")
# else:
#     print("invalid")