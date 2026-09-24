'''
Task: Convert c to f
Name: c_to_f
Input: degrees_c
side effects: none
return: degrees_f

'''

def c_to_f(degrees_c):
    degrees_f = ((degrees_c * 1.8) + 32)
    return degrees_f

'''
Task: tell the user the current temperature
Name: print_temp
Input: temp_in_f
side effects: "The Temperature is: X"
return:  no
'''

def print_temp(temp_in_f):
    print("The Temperature is : ", temp_in_f)
    return None

def main():
    temp_in_c = input("What is the temp in c? ") #asks for temp
    f_degrees = c_to_f(temp_in_c) #converts to f
    print_temp(f_degrees) # calls the function to tell the user the temp)