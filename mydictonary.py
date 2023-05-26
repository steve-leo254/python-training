#Dictionaries are value defined using key : value pairs. you access values
#using key instead of an index. This makes sense when you have a lot of data.

#person = {"name": "John", "Age" :30,"country":"kenya","city":"Nairobi"}
#print(person["age"])

#keys are case sentitive i.e "Name" is different from "name"
#please note that a key can not be repeated in a dictionary.If you define a key and try to create another, the previous valie will be replaced
#b1 = "ages" in person.keys()
#print(b1)

#create a dictonary replica of IEBC votes with there personal info

votes = {
    "Voter1": {
        "name": "John Doe",
        "age": 35,
        "gender": "Male",
        "address": "123 Main Street",
        "constituency": "Nairobi",
        "candidate": "Candidate A"
    },
    "Voter2": {
        "name": "Lorna Wanjiru",
        "age": 23,
        "gender": "Female",
        "address": "505 london Avenue",
        "constituency": "Kiambu",
        "candidate": "Candidate B"
    }
    # Add more voters as needed
 
    }

print(votes["Voter2"])


