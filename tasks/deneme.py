number = 40
while True:
    tahmin = int(input("Please enter number that you think: "))
    if tahmin < number:
        print("Go ahead! Write again! Your number was smaller!")
    elif tahmin > number:
        print("Write again! Your number was bigger!")
    else:
        print("Congrats! Your number was equal!")
        break
