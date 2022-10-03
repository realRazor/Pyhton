# customer_Id = [345, 123, 789, 234, 567, 8910]
# customer_name = ["Ali", "Veli", "Deli", "Ahmet", "Mehmet", "Zeki"]
# id = int(input("Please enter ID number: "))
# for i in range(len(customer_Id)):
#     if id == customer_Id[i]:  # if the id number equals to customer id then execute
#         print("Hello " + customer_name[i])
#         break
# else:
#     print("Invalid ID! Please enter valid ID number !")


num = int(input("Please enter number that you want to query: "))

def find_prime(num):
    case1 = False
    for i in range(num):
        if i == 0 or i == 1:
            continue
        if num % i == 0:
            break
    else:
        case1 = True
    return case1
count = 0
if find_prime(num) == True:
    count +=1

print(find_prime(num),count)