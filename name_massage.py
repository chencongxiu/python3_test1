#!/usr/bin/env python3
name = input("Please Enter your name: ")
print("Hello "+ name+", would you like to learn some Python today?")

#让字符串首字母大写
print(name.title())
#让字符串都是小写
print(name.lower())
#让字符串都是大写
print(name.upper())
print("Albert Einstein once said, \"A person who never made a mistake never tried anything new.\"")

famous_person = "Albert Einstein"
message = "\"A person who never made a mistake never tried anything new.\""
print(famous_person+" once said,"+message)
name1 = "\tBesea\n"
print(name1)
#让字符串首尾空格去掉
print(name1.strip())
#去掉字符串前面的空格
print(name1.lstrip())
#去掉字符串后面的空格
print(name1.rstrip())
