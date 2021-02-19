from colored import stylize, fg

print(stylize("\n---- | Calculator | ----\n", fg("red")))

def power(base_num, pow_num):
    result = 1
    for index in range(int(pow_num)):
        result = result * base_num
    return result

op = input("please enter the operator: ")
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
elif op == "^":
    print(power(num1, num2))
    
else:
    print(stylize("\n---- | Invalid operation. Try something else. | ----\n", fg("red")))
