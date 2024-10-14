people = [
    {"name":"harry", "house":"Gryffindor"},
    {"name":"Cho", "house":"Ravenclaw"},
    {"name":"Draco", "house":"Slytherin"}
]

#one line function: in python we can represent it using a lambda function
# def f(person):
#     return person["house"]
    
people.sort(key=lambda person:person["name"])

print(people)