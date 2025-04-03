persons = [
    { "first_name": "John", "last_name": "Doe" }
]

user_input_first_name = input("Enter the first name: ")
user_input_last_name = input("Enter the last name: ")

#We ask the user to input a new person
new_person = {
    "first_name": user_input_first_name,
    "last_name": user_input_last_name
}

persons.append(new_person)

for person in persons:
    print("Person :", person["first_name"], person["last_name"])

