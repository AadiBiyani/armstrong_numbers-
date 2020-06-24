

number = int(input("Enter a number"))
power = len(str(number))
def is_armstrong_number(number):
    number1 = 0 
    index= 0
    my_list = [int(d) for d in str(number)]
    for i in range(power):
        number2 = number1 + (pow(my_list[index],power))
        number1 = 0 + number2
        index = index+1
    if number1 == number:
            print ("It is an armstrong number")
    else:
            print ("It is not an armstrong number")      
            pass
is_armstrong_number(number)
        

