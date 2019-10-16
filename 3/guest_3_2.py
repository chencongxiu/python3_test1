#!/usr/bin/env python3
guests = ['Hawking','Galileo','Einstein']
message = "I am very honored to "+guests[0]+", "+guests[1]+" and "+guests[2]+" for dinner."
print(message)
no_attend = guests.pop(1)
message1 = no_attend+" can\'t attend."
print(message1)
guests.insert(1,'Edison')
message2 = "I am very honored to "+guests[0]+", "+guests[1]+" and "+guests[2]+" for dinner."
print(message2)
print("I found a bigger table")
guests.insert(0,'Platon')
guests.insert(2,'hugo')
guests.append('Dumas')
message3 = "I am very honored to "+guests[0]+","+guests[1]+","+guests[2]+","+guests[3]+" and "+guests[4]+" for dinner."
print(message3)
print("sorry,I can only invite two to dinner")
no_attend = guests.pop(0)
print(no_attend+" can\'t attend.")
no_attend = guests.pop(0)
print(no_attend+" can\'t attend.")
no_attend = guests.pop(0)
print(no_attend+" can\'t attend.")
no_attend = guests.pop(0)
print(no_attend+" can\'t attend.")

print(guests[0]+",welcome to dinner tonight")
print(guests[1]+",welcome to dinner tonight")
print(guests)

del guests[0]
del guests[0]
print(guests)
