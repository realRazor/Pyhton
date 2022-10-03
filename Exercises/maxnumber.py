#  Given to numbers, write a Python code to find the Maximum of these two numbers
# num1 = input("First number : ")
# num2 = input("Second number : ")
# if float(num1)>float(num2):
#     print(num1+" is greater than "+num2)
# else:
#     print(num2+" is greater than "+num1)
# --------------------------------

# def maximum(a, b):
#     if a >=b:
#         return a
#     else:
#         return b
# print(maximum(3, 4))

# ----------------------------------
# We can also use max() function. This way is easiest.

# a = int(input())
# b = int(input())
# maximum = max(a, b)
# print(maximum)
def find_prime(num):
    case1 = False
    for i in range(num):
        if i == 0 or i == 1:
            continue
        if num%i==0:
            break
    else:
        case1=True
    return case1
cnt = 0
j = 2
while True:
    if find_prime(j)==True:
        cnt+=1
    if cnt == 3:
        print(j)
        break
    j+=1