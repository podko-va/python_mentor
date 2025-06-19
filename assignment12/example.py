class User:
    count = 1
    pass

user1 = User()
user1.name = "Kate"
print(user1.name)

user2 = User()
user2.name = "Ivan"
print(user2.name)


print(User.count)