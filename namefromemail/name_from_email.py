# Create a function that takes email address as input in the following format:
# firstName.lastName@exam.com
# and returns a string that represents the user name in the following format:
# last_name first_name
# example: "elek.viz@exam.com" for this input the output should be: "Viz Elek"
# accents does not matter

#print(name_from_email("elek.viz@exam.com"))

def creating_email():
    email = input("Give me your email address (firstName.lastName@exam.com) ")
    name_from_email = email.split('.')
    first_name = name_from_email[0]
    create_last_name = name_from_email[1].split('@')
    last_name = create_last_name[0]
    name = []
    name.insert(1, first_name.title())
    name.insert(0, last_name.title())
    print(name)
    created_name = ' '.join(name)
    print(created_name)

creating_email()   

    
