# Create a function that takes a list of GitHub handles as input and returns a
# list of strings that represents
# GitHub url's under Green Fox Academy organization in the following format:
# "https://github.com/greenfox-academy/teststudent"

# example:
# input: ["ghhandle1", "ghhandle2"]
# output: ["https://github.com/greenfox-academy/ghhandle1", "https://github.com/greenfox-academy/ghhandle2"]

names = ["ghhandle1", "ghhandle2"]
given_url = "https://github.com/greenfox-academy/teststudent"

def urls_from_handles(names):
    given_url1 = given_url.split('/')
    print(given_url1.index("teststudent"))
    names1 = given_url1.insert(3, names(0))
    print(names1)
    names2 = given_url1.insert(3, names(1))
    print(names2)
print(urls_from_handles(names))
