def power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

op = input("please enter the operator: ")

if op == "^":
    pow1 = int(input("please enter your first power number: "))
    pow2 = int(input("please enter your second power number: "))
    print(power(pow1, pow2))
else :

    num1 = float(input("please enter your first number: "))
    num2 = float(input("please enter you second number: "))

    if op == "+":
        print (num1 + num2)
    elif op == "-":
        print (num1 - num2)
    elif op == "/":
        print (num1 / num2)
    elif op == "*":
        print (num1 * num2)
    
    else:
        print ("Invalid operation. Try something else.")
