names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)

# Use a list comprehension to create a list of lowercased names
lowercased = [name.lower() for name in names ]

# @TODO: Use a list comprehension to create a list of title cased names
# https://www.tutorialspoint.com/python/string_title.htm
title_cased = [name.title() for lowercase in lowercased]

invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in title cased]

for invitation in invitations:
    print(invitation)
