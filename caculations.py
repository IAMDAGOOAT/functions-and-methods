def add(num1,num2):
    print("Number 1:", num1)
    print("Number 2:", num2)
    addition = num1 + num2
    return addition

res = add(2, 4)
print(res)

def negative(num1,num2):                 
    print("Number 1:", num1)
    print("Number 2:", num2)
    neg =num1-num2                   
    return neg                     

res = negative(5,6)                  
print(res)

def multiply(num1, num2):          
    print("Number 1:", num1)
    print("Number 2:", num2)
    product = num1 * num2          
    return product                

res = multiply(3, 4)               
print(res)

def divide(num1, num2):            
    print("Number 1:", num1)
    print("Number 2:", num2)
    if num2 == 0:
        return "Cannot divide by zero"
    result = num1 / num2           
    return result                  

res = divide(10, 2)               
print(res)