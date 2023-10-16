'''# Declaring a function 
b1 = 10
_b = 15
def add(): 
        # Defining local variables.  
        global a
        a = 20 
        c = a + _b
        print("The sum is:" , c)

#add()
print(a)
print(_b)
#print("The sum is:" , c)


a = 4 
A = "Sally" 
# A will not overwrite a

print(a,A)
'''
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))


