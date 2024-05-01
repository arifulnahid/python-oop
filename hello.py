class User:
    def __init__(self, name, email, age):
        self.name = name
        self.age = age
        self.email = email

userList = []
userList.append(User('Ariful', 'ariful@mail.com', 24))
userList.append(User('Nahid', 'nahid@mail.com', 24))
userList.append(User('Nahid', 'nahid@mail.com', 24))
userList.append(User('Islam', 'islam@mail.com', 24))

find = filter(lambda x: x.email == 'islam@mail.com', userList)
print(find)
print(list(find))
print(find)

