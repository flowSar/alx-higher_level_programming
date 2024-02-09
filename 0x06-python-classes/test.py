#!/usr/bin/python3

class User:
    id = 1


u = User()
u.id = 100
User.id = 10
print(User.id)
print(u.id)