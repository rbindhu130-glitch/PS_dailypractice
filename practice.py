'''sentence = "Emma-is-a-data-scientist"
a = sentence.split('-')

for i in a:
    print(i)
'''



'''str1 = "Python"
reverse= str1[::-1]
print(reverse)'''

'''
string="Hello World"
string=string.lower()

vowels="aeiou"
count=0
for i in string:
    if i not in vowels and i!=" ":
        count=count+1
print(count)        
        '''

'''string = "Python is awesome"
no_speace=""
for i in string:
    if i !=" ":
        no_speace=no_speace+i
print(no_speace)    '''


special_char="!@#$%^&*"
password= input("enter a password:")
if len(password) >=8 and any(char in special_char for char in password):
    print("Password is strong")
else:
    print("Password is not strong")