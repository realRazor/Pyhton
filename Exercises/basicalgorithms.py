#  Adding two number provided by user input
# num1 = input("First number : ")
# num2 = input("Second number :")
# total = float(num1) + float(num2)

# print("The total is {}".format(total) )
# coin = 1000
# day = 7
# coin = coin*1.07**2
# print("The current amount : "+ str(coin))
#
# print("Muhammet Talha Yeşilyurt")

# coin = 1000  # The coin value
# day = 7
# percent = 7  # fixed profit daily
# coin = coin*((1+percent/100)**day)  # We calculate 7 percent seven times(number of days)
# print(coin)
total = 0
person = 4
for i in range(person):
    print(str(i+1) + ". " + "kişinin notu : ")              # Döngü her çalıştığında sıradaki kişinin notunu sorar
    total += int(input())                                      # Her yeni girilen notu bir önceki total değere ekler

print("The Average is " + str(total/person))         # Ortalamayı yazdırır

