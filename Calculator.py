#CALCULATOR PROJECT
def get_number(number):
    while True:
        operand = input ("Number " + str(number) + ":")
        try:
            return float(operand)
        except:
            print("invalid number")
      

operand1 = get_number(1)
operand2 = get_number(2)
sign =input("sign: ")



result = 0
if sign == "+":
    result = operand1 + operand2
    
elif sign =="-":
    result = operand1 - operand2
    
elif sign =="*":
    result = operand1 * operand2
    
elif sign =="/":
    if operand2 == 0:
        print ("divisor cannot be zero")
    else :
        result = operand1 / operand2
    
elif sign =="%":
    result = operand1 % operand2
    
else:
    print("you can only use +/-/*///% ")
print("RESULT= "+ str(result))
