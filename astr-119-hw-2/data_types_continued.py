#Python Data Types Continued

#string

s = "I am a string."
print(type(s))

#Boolean

yes = True #Boolean True
print(type(yes))

no = False #Boolean False
print(type(no)) 

#List -- ordered and changable

alpha_list = ["a", "b", "c"] #list initialization
print(type(alpha_list)) #will say tuple
print(type(alpha_list[0])) #will say string
alpha_list.append("d") #will add "d" to the list end
print(alpha_list) #will print last

#Tuple -- ordered and unchangable

alpha_tuple = ("a", "b", "c") #tuple initialization
print(type(alpha_tuple)) #will say tuple

try:
	alpha_tuple[2] = "d" #attempt the following line
except TypeError: #when we get a TypeError
	print("We can't add elements to tuples!") #print this message
print(alpha_tuple) #will print tuple