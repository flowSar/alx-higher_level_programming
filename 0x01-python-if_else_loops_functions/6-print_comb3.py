#!/usr/bin/python3
for n in range(0, 80, 10):
    for n2 in range(n+int((n/10+1)), n + 10):
        print("{:02d}, ".format(n2), end='')
print("89")
